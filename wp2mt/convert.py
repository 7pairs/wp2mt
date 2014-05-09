# -*- coding: utf-8 -*-


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

