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
自分が使うかもしれないものだけをメモ
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

### データの挿入 INSERT
```
sqlite> insert into user (id, name) values (1, 'inner');
```

### データの更新 UPDATE
(nameカラム内のinnerをaaaに変更)
```
sqlite> select * from user;
1|inner
2|penpen
sqlite> update user set name = 'aaa' where name = 'inner';
sqlite> select * from user;
1|aaa
2|penpen
```

### データの抽出 SELECT
全てのデータの抽出
```
sqlite> select * from user;
```
指定したカラムだけを抽出
```
sqlite> select name from user;
```
順に並べて抽出
```
sqlite> select * from user order by id;
```
逆順に並べて抽出
```
sqlite> select * from user order by id desc;
```
id の小さいものから二つを抽出
```
sqlite> select * from user order by id limit 2;
```

データが一致するもののみを抽出
```
sqlite> select * from user where name = 'inner';
```
特定の文字列を頭に含むもののみを抽出  
(nameカラム内のデータで冒頭の文字列がinを含むものを抽出)
```
sqlite> select * from user where name like 'in%';
```
カウント
```
sqlite> select count(*) from user;
```
id カラムで最大の値を抽出
```
sqlite> select max(id) from user;
```
ランダムに一つ抽出
```
sqlite> select * from user order by random() limit 1;
```
name カラムと name の文字列の長さを取得
```
sqlite> select name, length(name) from user;
name|length(name)
inner|5
penpen|6
aaa|3
```
ユニークな値を抽出
```
sqlite> select distinct name from user;
```
同じ name カラム同士の 年齢(age)を足して集計
```
sqlite> select name, sum(age) from user group by name;
```

### データの削除 DELETE
```
sqlite> select * from user;
1|inner
2|penpen
3|aaa
sqlite> delete from user where id >= 3;  # (id が３以下のものを削除)
sqlite> select * from user;
1|inner
2|penpen
sqlite> delete from user;  # 全て削除
sqlite> select * from user;
```

### その他
設定の確認
```
sqlite> .show
```
HEADER ON
```
sqlite> .header on
```
ヘルプ
```
sqlite> .help
```

## Python モジュール

```
import sqlite3
conn = sqlite3.connect('example.db')
```
[sqlite3-python3.4](http://docs.python.jp/3.4/library/sqlite3.html)
