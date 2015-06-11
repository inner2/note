# CSS
## 基本となる書き方
```
セレクタ { プロパティ名:値;}
```
## セレクタ
### ユニバーサルセレクタ  
すべての要素を指定
```
* { color: skyblue; }
```
### 要素名を指定
pタグをを指定
```
p { color: skyblue; }
```
### id と class
```
#id { color: skyblue; }
.class { color: skyblue; }
```

## 外部ファイルから読み込む
外部のCSS ファイルを読み込んむ方法  
(HEADタグ内に挿入)
```
<link rel="stylesheet" href="cssfile.css">
```

## コメント化

```
/* コメント */
```
