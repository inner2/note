# Flask
- Python 用の web アプリケーションフレームワーク
- マイクロフレームワーク
- Jinja2 と WSGI をベースにしている

[flask](http://flask.pocoo.org/)

## Install
```
$ pip install flask
```

## Hello Flask!
シンプルに。
```
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello Flask!'

if __name__ == '__main__':
    app.run()
```
実行する。
```
$ python hello.py
```
実行後、[http://localhost:5000](http://localhost:5000)に接続する。  
Hello Flask! と表示される。

## ルーティング Routing
```
@app.route('/')
def index():
    return 'Index Page'

@app.route('/hello')
def hello():
    return 'Hello World'
```


## 変数
```
@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return 'User %s' % username

@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return 'Post %d' % post_id
```

## リダイレクション Redirection
web サイトにおけるリダイレクションは指定したウェブページから自動的に他のwebページに転送されることをいう。  
projects にスラッシュなしでアクセスした場合、末尾にスラッシュの付いたページに飛ばされる。  

```
app.route('/projects/')
def projects():
    return 'The project page'

@app.route('/about')
def about():
    return 'The about page'
```

## URL のビルド
run.py
```
from flask import Flask, url_for
# インスタンスの作成
app = Flask(__name__)
@app.route('/')
def index(): pass

@app.route('/login')
def login(): pass

@app.route('/user/<username>')
def profile(username): pass

with app.test_request_context():
    print(url_for('index'))
    print(url_for('login'))
    print(url_for('login', next='/'))
    print(url_for('profile', username='John Doe'))
```
実行結果
```
$ python3 run.py
/
/login
/login?next=%2F
/user/John%20Doe
```

## HTTP method
POST, GET
```
@route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        do_the_login():
    else:
        show_the_login_form()
```

## レンダリングテンプレート
Python で HTML を生成するために、Flask ではJinja2 テンプレートエンジンの設定がされている。  
ファイル構成  
```
/app.py
/templates
  /hello.html
```
app.py
```
from flask import Flask, render_template
app = Flask(__name__)

@app.route('/hello')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)

app.run()
```
hello.html
```
<!doctype html>
<title>Hello from Flask</title>
{% if name %}
  <h1>Hello {{ name }}!</h1>
{% else %}
  <h1>Hello World!</h1>
{% endif %}
```
