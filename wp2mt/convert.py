# -*- coding: utf-8 -*-

import datetime

from bs4 import BeautifulSoup

try:
    from wp2mt.exception import ParseError
except ImportError:
    from exception import ParseError


def get_xml(file_path):
    """
    指定されたファイルパスからXMLを取得して文字列として返す。

    @param file_path: ファイルパス
    @type url: str
    @return: XML文字列
    @rtype: str
    """
    # 指定されたファイルを開く
    xml = ''
    try:
        with open(file_path) as f:
            xml = f.read()
    except Exception as e:
        pass

    # XMLを文字列として返す
    return xml


def parse(xml):
    """
    指定されたxml文字列を解析し、エントリに関連する情報を格納した辞書のリストを返す。

    @param html: XML文字列
    @type html: str
    @retrun: エントリ情報
    @rtype: list
    """
    # 戻り値用リスト
    retval = []

    # 引数をもとにBeautifulSoupオブジェクトを構築
    soup = BeautifulSoup(xml)

    # XMLを解析
    items = soup.find_all('item')
    for item in items:
        creator = item.find('dc:creator')
        title = item.find('title')
        category = item.find('category')
        post_date = item.find('wp:post_date')
        content = item.find('content:encoded')
        retval.append({
            'author': creator.string,
            'title': title.string,
            'category': category.string,
            'date': datetime.datetime.strptime(post_date.string, '%Y-%m-%d %H:%M:%S'),
            'body': content.string,
        })

    # 構築したリストを返す
    return retval


MT_TEMPLATE = """\
--------
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
"""


def create_mt_data(data_list):
    """
    エントリ情報の格納されたリストをもとにMovableType形式のインポート文字列を構築する。

    @param data: エントリ情報
    @type data: list
    @return: インポート文字列
    @rtype: str
    """
    # 戻り値用
    retval = ''

    # MovableType形式に変換
    for data in data_list:
        data['date'] = data['date'].strftime('%m/%d/%Y %I:%M:%S %p')
        retval += MT_TEMPLATE % data

    # 構築した文字列を返す
    return retval

