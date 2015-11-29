# configparser

## configparser とは
- Python の Module
- 設定言語を実装したクラス
- Windows の ini ファイルに似た構造を持っている。
- 簡易的な設定ファイルを作るときに便利

## Python version
- python 3.4.3

## 設定ファイルの構造例
設定ファイルの構造の例を示す。
記号は 「=」と「:」のどちらでも OK。
また、記号の前後にスペースを入れても入れなくてもどちらでもいい。

config.txt
```
[defalt]
user = inner

[info]
directory : dir
mode : 0
```

## ファイルの作成
config.txt と同じファイルを作成する。

config_write.py
```
import configparser

default = {'user': 'inner'}
info = {'directory': 'dir', 'mode': }

config = configparser.ConfigParser()
config['default'] = default
config['info'] = info

with open('config.txt', 'w') as configfile:
    config.write(configfile)
```

## ファイルの読み込み
作成したファイルを読み込んでいく。  
読み込むときは数値などは文字列として扱われるようです。  

config_read.py
```
import configparser

config = configparser.ConfigParser()
config.read('config.txt')

user = config['defalt']['user']
print(user)  # inner と表示される

# info の中の要素を全て取り出す
for i in config['info']:
    print(i)
    print(config.['info'][i])
```

実行結果
```
inner
directory
dir
mode
0
```
