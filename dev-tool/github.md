# Githubの使い方
 シンプルに最低限の内容を使い方メモ
 細かいことは理解していないだろう

## Github とは
 ソフトウェア開発の為の共有 web サービスで Git (バージョン管理システム)のハブ

## Github を使う
### 基本は push と pull
  - push : ローカル → Github
  - pull : Github → ローカル

### ローカルのリポジトリから Github に push
  ```
  $ git push https://github.com/[user]/[repository].git
  ```

### Github からローカルのリポジトリに pull
  ローカルで一度pushし、Github上で編集などをした場合にローカルに変更を反映される
  ```
  $ git pull https://github.com/[user]/[repository].git
  ```

## Github を使うときに一連の流れ
  一人で開発するときでもよく使いそうな流れをメモ

### Githubで新しくリポジトリを作成してローカルからpushする
  user はユーザー名、repository はレポジトリ名が入る
  ```
  $ git init
  $ git add .
  $ git commit -m "hoge"
  $ git remote add origin https://github.com/[user]/[repository].git
  $ git push -u origin master
  ```

### Github のソースを利用し、ローカルで編集した後にpushする
  このパターンがもっとも利用すると思う。
  ```
  $ git clone https://github.com/[user]/repository].git
  $ git add .
  $ git commit -m "hoge"
  $ git push origin master
  ```

## Github でよく見かけるファイル

### README.md
  - プロジェクトやツールの使い方の説明や宣伝の為のファイル
  - markdown で作成

## トラブルシューティング

### ローカルを変更した際に Github から pull するとエラーが出る
  Github 上で編集を行って、ローカルのリポジトリに pull したいが、
  ローカルを変更していると pull した際にエラーが出るという話。
  以下は README.md でエラーが出ている。
  ```
  $ git pull origin master
  error: Your local changes to the following files would be overwritten by merge:
  	README.md
  Please, commit your changes or stash them before you can merge.
  Aborting
  ```

  賢いやり方はあまり理解していないが、簡単なのは必要ではない方のバージョンを落とすのがいいだろう。
  両方必要な場合は blanch を作るといいのだと思う。
  ```
  $ git reset --hard [id/(HEAD)]
  ```

### Github で .gitignore が反映されない
キャッシュが残っていると反映されない場合がある。
```
$ git rm -r --cached .
```
