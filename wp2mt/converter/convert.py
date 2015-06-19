# -*- coding: utf-8 -*-

#
# Copyright 2015 Jun-ya HASEBA
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

import datetime

from bs4 import BeautifulSoup


class ParseError(Exception):
    """
    文字列の解析に失敗したことを示す例外。
    """

# MovableTypeフォーマット出力用テンプレート
MT_TEMPLATE = """\
AUTHOR: %(author)s
TITLE: %(title)s
STATUS: publish
ALLOW COMMENTS: 0
CONVERT BREAKS: __default__
ALLOW PINGS: 0
PRIMARY CATEGORY: %(category)s
CATEGORY: %(category)s

DATE: %(date)s
-----
BODY:
%(body)s
-----
EXTENDED BODY:

-----
EXCERPT:

-----
KEYWORDS:

-----


--------
"""


def execute(in_file, out_file):
    """
    WordPress形式のXMLをMovableType形式のテキストに変換する。

    :param in_file: WordPress形式ファイルのパス
    :type in_file: str
    :param out_file: MovableType形式ファイルのパス
    :type out_file: str
    """
    # MovableType形式のテキストファイルを生成する
    xml = read_file(in_file)
    for entry in parse_xml(xml):
        mt_data = create_mt_data(entry)
        save_file(out_file, mt_data)


def read_file(file_path):
    """
    指定されたファイルの内容を文字列として返す。

    :param file_path: ファイルパス
    :type file_path: str
    :return: XML文字列
    :rtype: str
    """
    # 指定されたファイルの内容を返す
    try:
        with open(file_path) as f:
            return f.read()
    except getattr(__builtins__, 'FileNotFoundError', IOError):
        return ''


def parse_xml(xml):
    """
    指定されたXML文字列を解析し、エントリの情報を格納した辞書を返す。

    :param xml: XML文字列
    :type xml: str
    :return: エントリ情報
    :rtype: Iterator[Dict[str, str]]
    """
    # 引数をもとにBeautifulSoupオブジェクトを構築する
    soup = BeautifulSoup(xml)

    # XMLを解析する
    items = soup.find_all('item')
    for item in items:
        creator = item.find('dc:creator')
        title = item.find('title')
        category = item.find('category')
        post_date = item.find('wp:post_date')
        content = item.find('content:encoded')
        yield {
            'author': creator.string,
            'title': title.string,
            'category': category.string,
            'date': datetime.datetime.strptime(post_date.string, '%Y-%m-%d %H:%M:%S').strftime('%m/%d/%Y %I:%M:%S %p'),
            'body': content.string,
        }


def create_mt_data(data):
    """
    エントリ情報をもとにMovableType形式の文字列を構築する。

    :param data: エントリ情報
    :type data: Dict[str, str]
    :return: MovableType形式文字列
    :rtype: str
    """
    # MovableType形式に変換する
    return MT_TEMPLATE % data


def save_file(file_path, data):
    """
    文字列をファイルに保存する。

    :param file_path: ファイルパス
    :type file_path: str
    :param data: 保存する文字列
    :type data: str
    """
    # 文字列をファイルに保存する
    with open(file_path, 'a') as f:
        f.write(data)
