# wp2mt

[![Build Status](https://travis-ci.org/7pairs/wp2mt.svg?branch=master)](https://travis-ci.org/7pairs/wp2mt)
[![Coverage Status](https://img.shields.io/coveralls/7pairs/wp2mt.svg)](https://coveralls.io/r/7pairs/wp2mt?branch=master)

## 概要

WordPress形式のエクスポートファイルをMovable Type形式のエクスポートファイルに変換するツールです。ブログシステムの移行時に利用することを想定しています。

## バージョン

Python3.4での動作を確認しています。また、3.2、3.3でもユニットテストを行っていますので、おそらく両バージョンでも動作するものと思われます。なお、Python2系には対応しておりません。ご了承ください。

## インストール

同梱の `setup.py` を実行してください。

```
python setup.py install
```

pipを導入している方は、GitHubから直接インストールすることもできます。

```
pip install git+https://github.com/7pairs/wp2mt.git
```

## 実行方法

入力ファイル（WordPress形式）、出力ファイル（Movable Type形式）を指定して実行してください。

```
wp2mt <input-file-path> <output-file-path>
```
