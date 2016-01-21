# SQLite

- 軽量のデータベース
- アプリケーションに組み込んで利用される

## データベースの作成・接続
```
$ sqlite3 example.db
```

## 終了
```
sqlite> .exit
```

## データベースの削除
'example.db' のファイルを削除

## テーブル
### テーブルの作成
```
sqlite> create table stocks(id, name);
```

### 型を指定してテーブルを作成
```
sqlite> create table stocks(id integer, name text);
```

型について
- null : NULL
- integer : 符号付整数
- real : 浮動小数点数
- text : テキスト
- blob : binary large object  入力データをそのまま


### テーブルのスキーマ情報の表示
```
sqlite> .schema
CREATE TABLE stocks(id, name);
```
- schema(概要；枠組み；概略図)

### テーブルの削除
```
sqlite> drop table stocks;
```

## データの追加・更新・削除
### データの追加
```
sqlite> insert into stocks values(1, 'inner');
```

### データの更新
id = 1 の name カラム 'penpen' に変更
```
sqlite> update stocks set name = 'penpen' where id = 1;
```

### データの削除
stocks テーブルの内容全て削除
```
sqlite> delete from stocks;
```
条件を指定して削除  
stocks テーブル内の id = 1 のデータを削除
```
sqlite> delete from stocks where id = 1;
```

## SELECT
### データの抽出
テーブル内の全てのデータを取得
```
sqlite> select * from stocks;
```
name カラムのみを抽出
```
sqlite> select name from stocks;
```

### Sort
昇順
```
sqlite> select * from stocks order by id asc;
```
降順
```
sqlite> select * from stocks order by id desc;
```

### 条件を設定
```
sqlite> select * from stocks where name = 'inner';
```

### Limit
データを10個取得
```
sqlite> select * from stocks limit 10;
```

## 設定の確認
```
sqlite> .show
```

## ヘルプ
```
sqlite> .help
```

## 参考
[SQLite 入門](http://www.dbonline.jp/sqlite/)
