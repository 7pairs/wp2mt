# -*- coding: utf-8 -*-

import sys

try:
    # setup.py実行後
    from wp2mt.converter import convert
except ImportError:
    # 未インストール状態での動作確認時
    from converter import convert


def main():
    """
    WordPress形式のエクスポートファイルをMovableType形式に変換する
    """
    # 引数をチェックする
    if len(sys.argv) != 3:
        print('Usage:')
        print('wp2mt <input_file> <output_file>')
        quit()

    # 変換を実行する
    convert.execute(sys.argv[1], sys.argv[2])


if __name__ == '__main__':
    main()
