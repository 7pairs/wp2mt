# -*- coding: utf-8 -*-

from nose.tools import *

from wp2mt import convert


def test_get_xml():
    """
    引数に有効なファイルパスを指定したとき、そのパスのXMLの内容を文字列として返すことを確認する。
    """
    xml = convert.get_xml('./test.xml')
    actual = ('1つ目の記事' in xml)
    assert_equal(True, actual)


def test_get_xml_02():
    """
    引数に無効なファイルパスを指定したとき、空文字列を返すことを確認する。
    """
    xml = convert.get_xml('./not_exists.xml')
    assert_equal('', xml)

