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

