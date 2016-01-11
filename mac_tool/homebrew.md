# Home brew について

## 基本ていなコマンド

更新
```
$ brew doctor
```
アップデート
```
$ brew update
```
インストールしているアプリケーションの一覧を見る
```
$ brew list
```
インストール(gccのインストール例)
```
$ brew install gcc
```
アンインストール(gccのアンインストール例)
```
$ brew uninstall gcc
```
検索(gccの検索例)
```
$ brew search gcc
```


## Brew cask

コマンドはほとんど同じ。
$ brew cask ~ となる。


## Error

### リンク切れ
例) gcc のリング切れらしい
```
Warning: You have unlinked kegs in your Cellar
Leaving kegs unlinked can lead to build-trouble and cause brews that depend on
those kegs to fail to run properly once built. Run `brew link` on these:
    gcc
```
修正(gccの場合)
```
$ brew link gcc
```
[参考ページ](http://qiita.com/fumi_042/items/55be8fb37cc23325b7c2)

### 一覧に存在するが、アンインストールできない
例）brew cask list で arduino が存在するが、アンインストールできなかった。
```
$ brew cask list
appcleaner		   google-chrome	      mi
arduino			   google-japanese-ime	      pycharm-ce (!)
atom			   iterm2		      virtualbox
coteditor		   java			      xtrafinder
shibataisao-no-MacBook-Air:~ shibataisao$ brew cask uninstall arduino
Error: arduino is not installed
```
対策
```
$ brew cask uninstall arduino --force
```
