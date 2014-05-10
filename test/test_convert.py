# -*- coding: utf-8 -*-

import datetime
import textwrap

from nose.tools import *

from wp2mt import convert


def test_get_xml_01():
    """
    引数に有効なファイルパスを指定したとき、そのパスのXMLの内容を文字列として返すことを確認する。
    """
    xml = convert.get_xml('./test/test_01.xml')
    actual = ('1つ目の記事' in xml)
    assert_equal(True, actual)


def test_get_xml_02():
    """
    引数に無効なファイルパスを指定したとき、空文字列を返すことを確認する。
    """
    xml = convert.get_xml('./test/not_exists.xml')
    assert_equal('', xml)


def test_parse_01():
    """
    引数に有効なXML文字列を指定したとき、その内容を辞書のリストとして返すことを確認する。
    """
    with open('./test/test_01.xml') as test_file:
        xml = test_file.read()
    result = convert.parse(xml)
    assert_equal(1, len(result))
    assert_equal('7pairs', result[0]['author'])
    assert_equal('1つ目の記事', result[0]['title'])
    assert_equal('はてなダイアリー過去ログ', result[0]['category'])
    assert_equal(datetime.datetime(2004, 7, 14, 0, 0, 0), result[0]['date'])
    assert_equal(textwrap.dedent("""\
        1つ目の記事1行目
        1つ目の記事2行目
        1つ目の記事3行目
    """), result[0]['body'])


def test_parse_02():
    """
    引数に有効なXML文字列を指定したとき、その内容をすべてリストとして返すことを確認する。
    """
    with open('./test/test_02.xml') as test_file:
        xml = test_file.read()
    result = convert.parse(xml)
    assert_equal(2, len(result))

