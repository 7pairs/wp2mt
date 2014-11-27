# -*- coding: utf-8 -*-

import datetime
import sys

from bs4 import BeautifulSoup


class ParseError(Exception):
    """
    文字列の解析に失敗したことを示す例外。
    """


def execute(in_file, out_file):
    """
    WordPress形式のXMLをMovableType形式に変換する。

    :param in_file: WordPress形式ファイルのパス
    :type in_file: str
    :param out_file: MovableType形式ファイルのパス
    :type out_file: str
    """
    # MovableType形式のテキストファイルを生成
    xml = get_xml(in_file)
    for entry in parse(xml):
        mt_data = create_mt_data(entry)
        save_file(out_file, mt_data)


def get_xml(file_path):
    """
    指定されたファイルパスからXMLを取得して文字列として返す。

    :param file_path: ファイルパス
    :type file_path: str
    :return: XML文字列
    :rtype: str
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
    指定されたxml文字列を解析し、エントリに関連する情報を格納した辞書を返す。

    :param xml: XML文字列
    :type xml: str
    :return: エントリ情報
    :rtype: Iterable[Dict[str, str]]
    """
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
        yield {
            'author': creator.string,
            'title': title.string,
            'category': category.string,
            'date': datetime.datetime.strptime(post_date.string, '%Y-%m-%d %H:%M:%S'),
            'body': content.string,
        }


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


def create_mt_data(data):
    """
    エントリ情報をもとにMovableType形式のインポート文字列を構築する。

    :param data: エントリ情報
    :type data: Dict[str, str]
    :return: インポート文字列
    :rtype: str
    """
    # MovableType形式に変換
    data['date'] = data['date'].strftime('%m/%d/%Y %I:%M:%S %p')
    retval = MT_TEMPLATE % data

    # 構築した文字列を返す
    return retval


def save_file(file_name, data):
    """
    文字列をファイルに保存する。

    :param file_name: ファイルパス
    :type file_name: str
    :param data: 保存する文字列
    :type data: str
    """
    # 文字列をファイルに保存
    with open(file_name, 'a') as f:
        f.write(data)


if __name__ == '__main__':
    # 引数をチェック
    if len(sys.argv) != 3:
        print('Usage: python %s input_file output_file' % sys.argv[0])
        quit()

    # スコアテーブルを出力
    execute(sys.argv[1], sys.argv[2])
