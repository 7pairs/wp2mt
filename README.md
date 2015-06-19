# wp2mt

[![Build Status](https://travis-ci.org/7pairs/wp2mt.svg?branch=master)](https://travis-ci.org/7pairs/wp2mt)
[![Coverage Status](https://img.shields.io/coveralls/7pairs/wp2mt.svg)](https://coveralls.io/r/7pairs/wp2mt?branch=master)

## 概要

"wp2mt"は、WordPress形式のエクスポートファイルをMovable Type形式のエクスポートファイルに変換するツールです。

## バージョン

Python3.4での動作を確認しています。
また、Python3.2、3.3でもユニットテストを実施しています。

## インストール

同梱の `setup.py` を実行してください。

```console
$ python setup.py install
```

pipを利用し、GitHubから直接インストールすることもできます。

```console
$ pip install git+https://github.com/7pairs/wp2mt.git
```

## 実行方法

入力ファイルのパス、出力ファイルのパスを指定して実行してください。

```console
$ wp2mt <input-file-path> <output-file-path>
```

`<input-file-path>` にはWordPress形式のファイルを指定してください。

## ライセンス

wp2mtは [Apache License, Version 2.0](http://www.apache.org/licenses/LICENSE-2.0) にて提供します。
ただし、wp2mtが依存している [Beautiful Soup](http://www.crummy.com/software/BeautifulSoup/) は [The MIT License](http://opensource.org/licenses/mit-license.php) により提供されていますのでご注意ください。
