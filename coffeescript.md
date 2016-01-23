# CoffeeScript
- コードは JavaScript に変換される。
- JavaScript に比べて簡潔で可読性が高い

[公式サイト](http://coffeescript.org)

## Version
CoffeeScript 1.10.0

## Hello world
var や ; ,カッコは不要  
コメントは # を使う
```
###
Hello world
###

# 変数
hello = 'Hello world'

# alert window で文章を表示
alert hello
```

## 変数
```
# 数値
num = 1

# bool　true or false
flag = true

# 文字列
name = 'inner'

# 複数行
html = """
       <html>
           contents
       </html>
       """
```

## 式展開
```
score = 80
alert "score: #{score}"
```

## 配列 と オブジェクト
```
# Array
a = [1, 3, 5]     # a = [1, 3, 5]
b = [0..5]        # b = [0,1,2,3,4,5]
c = [0...5]       # c = [0,1,2,3,4]

# object
aaa = name: 'inner', age: 24

# 複雑に書く
bbb =
    name: 'inner'
    score:
        ccc: 10
        ddd: 20
```

## 制御文
### 条件分岐 if
flag が true の時に OK を表示する
```
flag = true

# 一行で if else
if flag then alert "OK" else alert "NG"

# 複数行で if else
if flag
    alert "OK"
else
    alert "NG"

# 後置の if
alert "OK" if flag

# そのまま代入
msg = if flag then "OK" else "NG"
alert msg
```
複雑な条件分岐
```
color = "green"

if color == "red"
    alert "color is red"
else if color == "green"
    alert "color is green"
else
    alert "color ?"
```

### Switch
```
color = "green"

switch color
    when "red"
        alert "color is red"
    when "green" then alert "color is green"　　# then を使って一行でも書ける
    else
        alert "color ?"
```

### 繰り返し for while
```
# for
sum = 0
for i in [0..9]
    sum += i
alert sum

# while
j = 0
sum = 0
while j < 10
    sum += j
    j++
alert sum
```

## 関数
```
# 引数がない場合
hello = ->
    alert "hello"

# 引数と返り値
hello2 = (name) ->
    "I am #{name}."

# 関数の実行
hello()
result = hello2 "inner"
alert result
```

## クラス
```
class User
    constructor: (name) ->
        # 最初に呼ばれるメソッド
        this.name = name
    do: () ->
        alert "I am #{@name}"

tom = new User "Tom"
alert tom.name
tom.do()
```

## JavaScript の埋め込み
コードをバッククオートで囲む

## 参考
[CoffeeScript言語リファレンス-sappari wiki](http://memo.sappari.org/coffeescript/coffeescript-langref#TOC-5)
[ドットインストール](http://dotinstall.com)
