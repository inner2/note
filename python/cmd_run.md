# python でコマンドを実行する
## 環境
- MAC OS X EI Caption

## Python version
- python 3.5.0

## subprocess モジュールを利用してコマンドを実行

```python
import subprocess

cmd = 'ls -l'
result = subprocess.getoutput(cmd)
print(result)  # 実行結果の表示
```

## 参考ページ

[python3 - subprocess](http://docs.python.jp/3.5/library/subprocess.html)
