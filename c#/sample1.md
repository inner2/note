# C# でよく使うもののまとめ
## 簡単なメッセージを表示する
MessageBox.Showメソッド使う。  
簡単メッセージを表示するのにとても便利なのでよく使う。  
MessageBox.Show メソッドに int 型や double 型は使えない。  
```
MessageBox.Show(string);
// title を入れる
MessageBox.Show(string, title);
```

## フォームの操作
- タスクバーに表示しない
- 最小化
- 閉じる

```
// このフォームをタスクバーに表示しない
this.ShowInTaskbar = false;
// フォームを最小化する
this.WindowState = FormWindowState.Minimized;
// フォームを閉じる
this.Close();
```

## 新しいフォームを開く
新しくフォームアプリケーションを追加し、新しいウィンドウで開く。
```
Form2 cform2 = new Form2();
cform2.Show();
```

## ウィンドウを常に手前に表示する
```
if (this.TopMost == false)
{
  // ウィンドウを常に手前にする
  this.TopMost = true;
}
else
{
  // ウィンドウを常に手前にしない
  this.TopMost = false;
}
```

## カレントディレクトリを習得する
プログラムを実行しているディレクトリを取得し、フォルダを開く。
```
// カレントディレクトリを取得する
string stCurrentDir = System.IO.Directory.GetCurrentDirectory();
// プログラムの実行(フォルダを開く)
System.Diagnostics.Process.Start(stCurrentDir);
```

## Window の透過度を設定する
```
// 80%
this.Opacity = 0.8;
```
