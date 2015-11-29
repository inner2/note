# Text file

## Python version
- python 3.4.3

## Write
```
write_file = 'hello.txt'
text = 'hello'
f = open(write_file, 'w')  # 'w' は書き込み専用
f.write(text)
f.close()
```

## Read
- read()
  - テキストファイルの全文を読み込む
- readline()
  - テキストファイルの内容を1行ずつ読み込む

```
readfile = 'hoge.txt'
f = open(readfile, 'r')  # 'r' は読み取りモード
str = f.read()  # readline を使うと1行ずつ読み込める
f.close()
print(str)
```

## mode 引数について

```
'w' : 書き込み専用（既存ファイルがあれば消去）
'r' : 読み取り専用
'a' : ファイルに追記する
'r+' : 読み書きの両方をする
省略も可能 : 省略時には 'r' と仮定される
```

## Encoding
Windows や Mac など環境が変わるとエンコードの違いでエラーがよく出る。  
そのため、書き込みや読み込み時に指定しておくと問題を回避できるだろう。  
以下に例を示すが、読み込みでも書き込みでも要領は同じである。  

```
file_name = 'hello.txt'
f = open(file_name, 'r', encoding='utf-8')
f.close()
```
