# SQLite について
## 概要

- データベース Database について
    - データを集めて管理し、容易に検索・抽出などの再利用をできるようにしたもの
    - データを格納するための構造などに工夫があり、データの再利用を高速で安定に行える
- SQLite について
    - パブリックドメインの軽量な関係データベース管理システム(RDBMS)
    - サーバーとしてではなくアプリケーションに組み込んで利用される
    - 大規模な仕事には不向き

## SQLite version
SQLite version 3.8.10.2

## SQLite の基本操作 コマンド
### データベースの接続と終了
データベースの作成と接続
```
$ sqlite3 [database filename].sqlite3
```
終了
```
sqlite> .exit
```
### table の操作
table の作成
```
sqlite> create table user(id, name);
```
上記の例はuserテーブルの中にid, nameの二つのカラムを作成

- user(table)
    - id(column)
    - name(column)

table の確認
```
sqlite> .table
user
```
table の構造を確認
```
sqlite> .schema user
CREATE TABLE user(id, name);
```
table の削除
(userテーブルを削除)
```
sqlite> drop table user;
```

###

### その他
ヘルプ
```
sqlite> .help
```


## Python モジュール
[sqlite3-python3.4](http://docs.python.jp/3.4/library/sqlite3.html)
