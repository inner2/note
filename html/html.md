# HTML 基本
## Hello world

<タグ 属性='値'>テキスト</タグ>

hello.html
```
<!DOCTYPE html>
<html lang="ja">
  <head>
    <meta charrset="utf-8">
    <title>Hello world</title>
  </head>
  <body>
    <p>Hello</p>
  </body>
</html>
```

## コメント
```
<!-- コメント -->
```

## グローバル属性
すべてのタグにつけられる属性  
その一部をメモ(id, class, style)
id: 一つしかない要素  
class: 複数ある要素  
style: スタイルを直接指定  

例
```
<p id="message">こんいちは</p>
<p class="message active">こんいちは</p>
<p class="message" style="background:skyblue;">こんいちは</p>
```

## よく使うタグ
body タグの中で使えるタグ
- h1-h6 : 見出し(Heading)
- p : 段落(paragraph)
  - pタグは空行が入る
- br : 改行
- strong : 調、太字
- span : なんらかの処理をしたいときに使われる
  - タグ自体にはあまり意味がない
- hr : 平線
- pre : 改行や字下げを保持
- blockquote : 引用
- div : スタイリング用途などで使われる

## リストを作成
### 番号の付いてない unordered list(ul)
li : list item
```
<ul>
  <li>Apple</li>
  <li>Banana</li>
</ul>
```
### 番号つきのリスト ordered list(ol)
```
<ol>
  <li>Apple</li>
  <li>Banana</li>
</ol>
```
### 定義リスト definition list(dl)

```
<dl>
  <dt>定義</dt>
  <dd>定義の説明</dd>
</dl>
```

## 表の作成
- tr: table row(行)
- th: table header(見出し)
- td: table data

```
<table>
  <thead>
    <tr><th>fruit</th><th>Price</th></tr>
  </thead>
  <tbody>
    <tr><td>Apple</td><td>120</td></tr>
    <tr><td>Orange</td><td><100/td></tr>
  </tbody>
</table>
```
## 説明
HEAD タグの中でよく入っている
```
<meta name="description" content="HTMLの説明">
```

## css ファイルを使用
スタイルの指定は長くなることが多いため、  
HTML とは別に CSS ファイルがよく作られる。  
HTML で CSS ファイルを使用するためのタグ
```
<link rel="stylesheet" href="mystyle.css">
```

## favicon
```
<link rel="shortcut icon" href="favicon.ico">
```

## リンクの貼り方
### リンク先のページを開く
```
<a href="http://google.com">Google</a>
```
### 別のタグでリンク先のページを開く(target 属性を使う)
```
<a href="http://google.com" target="_blank">Google</a>
```
### ページ内リンク
```
<a href="#message">idがmessageの要素に移動</a>
...
<p id="message">リンク先</p>
```

## 画像を表示
img属性について
- src : 画像ファイル名を指定
- width : 画像の幅を指定
- height : 画像の高さを指定
- alt : 画像が表示されない際の代替情報として入力される
```
<img src="image.jpg" width="150" height="100" alt="表示されないときの説明">
```

## 入力フォーム
