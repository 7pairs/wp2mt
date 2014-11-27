# -*- coding: utf-8 -*-

import datetime
import os
import textwrap

from nose.tools import *

from wp2mt.converter import convert


def test_get_xml_01():
    """
    引数に有効なファイルパスを指定したとき、そのパスのXMLの内容を文字列として返すことを確認する。
    """
    xml = convert.get_xml('./wp2mt/tests/test_01.xml')
    actual = ('1つ目の記事' in xml)
    assert_equal(True, actual)


def test_get_xml_02():
    """
    引数に無効なファイルパスを指定したとき、空文字列を返すことを確認する。
    """
    xml = convert.get_xml('./wp2mt/tests/not_exists.xml')
    assert_equal('', xml)


def test_parse_01():
    """
    引数に有効なXML文字列を指定したとき、その内容を辞書のリストとして返すことを確認する。
    """
    with open('./wp2mt/tests/test_01.xml') as test_file:
        xml = test_file.read()
    result = next(convert.parse(xml))
    assert_equal('7pairs', result['author'])
    assert_equal('1つ目の記事', result['title'])
    assert_equal('はてなダイアリー過去ログ', result['category'])
    assert_equal(datetime.datetime(2004, 7, 14, 0, 0, 0), result['date'])
    assert_equal(textwrap.dedent("""\
        1つ目の記事1行目
        1つ目の記事2行目
        1つ目の記事3行目
    """), result['body'])


def test_create_mt_data_01():
    """
    引数に辞書を指定したとき、MovableType形式の文字列を返すことを確認する。
    """
    data = {
        'author': '7pairs',
        'title': '1つ目の記事',
        'category': 'はてなダイアリー過去ログ',
        'date': datetime.datetime(2004, 7, 14, 0, 0, 0),
        'body': textwrap.dedent("""\
            1つ目の記事1行目
            1つ目の記事2行目
            1つ目の記事3行目
        """),
    }

    expected = textwrap.dedent("""\
        AUTHOR: 7pairs
        TITLE: 1つ目の記事
        STATUS: publish
        ALLOW COMMENTS: 0
        CONVERT BREAKS: __default__
        ALLOW PINGS: 0
        PRIMARY CATEGORY: はてなダイアリー過去ログ
        CATEGORY: はてなダイアリー過去ログ

        DATE: 07/14/2004 12:00:00 AM
        -----
        BODY:
        1つ目の記事1行目
        1つ目の記事2行目
        1つ目の記事3行目

        -----
        EXTENDED BODY:

        -----
        EXCERPT:

        -----
        KEYWORDS:

        -----


        --------
    """)

    actual = convert.create_mt_data(data)
    assert_equal(expected, actual)


def test_save_file_01():
    """
    引数に文字列とファイル名を指定したとき、文字列の内容をファイルに保存することを確認する。
    """
    data = textwrap.dedent("""\
        保存する文字列アルよー。
        これは2行目アルよー。
    """)
    convert.save_file('./wp2mt/tests/test.txt', data)

    with open('./wp2mt/tests/test.txt') as f:
        actual = f.read()

    assert_equal(data, actual)

    os.remove('./wp2mt/tests/test.txt')


def test_convert_01():
    """
    WordPress形式のファイルをMovableType形式に変換することを確認する。
    """
    convert.execute('./wp2mt/tests/test_02.xml', './wp2mt/tests/test.txt')

    with open('./wp2mt/tests/test.txt') as f:
        actual = f.read()

    expected = textwrap.dedent("""\
        AUTHOR: 7pairs
        TITLE: 1つ目の記事
        STATUS: publish
        ALLOW COMMENTS: 0
        CONVERT BREAKS: __default__
        ALLOW PINGS: 0
        PRIMARY CATEGORY: はてなダイアリー過去ログ
        CATEGORY: はてなダイアリー過去ログ
        
        DATE: 07/14/2004 12:00:00 AM
        -----
        BODY:
        1つ目の記事1行目
        1つ目の記事2行目
        1つ目の記事3行目
        
        -----
        EXTENDED BODY:
        
        -----
        EXCERPT:
        
        -----
        KEYWORDS:
        
        -----
        
        
        --------
        AUTHOR: 7pairs
        TITLE: 2つ目の記事
        STATUS: publish
        ALLOW COMMENTS: 0
        CONVERT BREAKS: __default__
        ALLOW PINGS: 0
        PRIMARY CATEGORY: はてなダイアリー過去ログ
        CATEGORY: はてなダイアリー過去ログ
        
        DATE: 07/15/2004 12:00:00 AM
        -----
        BODY:
        2つ目の記事1行目
        2つ目の記事2行目
        2つ目の記事3行目
        
        -----
        EXTENDED BODY:
        
        -----
        EXCERPT:
        
        -----
        KEYWORDS:
        
        -----


        --------
    """)

    assert_equal(expected, actual)

    os.remove('./wp2mt/tests/test.txt')
