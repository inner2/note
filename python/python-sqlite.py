# python で SQLite3 を使う
## python version
- python 3.5.0

## SQLite3 version
- 3.8.10.2

## python code

```Python
import sqlite3

# Connect database
conn = sqlite3.connect('example.db')
c = conn.cursor()

# テーブルの作成
c.execute("create table stocks(word1, word2")

# データの挿入
w1 = "hello"
w2 = "world"
c.execute("insert into stocks values(?, ?)", (w1, w2))

# データの抽出
c.execute("select * from stocks")
list = c.fetchall()
print(list)

# Save
conn.save()

# Close
conn.close()
```

## 参考
[python - sqlite3](http://docs.python.jp/3.5/library/sqlite3.html)
