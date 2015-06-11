# サンプルプログラム
## drag & drop したファイルの PATH を取得する
1. フォームアプリケーション Form1 を作成。
2. Form1 のプロパティの AllowDrop を true に設定し、drag&dropを許可する。
3. Form1 の DragEnter と DragDrop のイベントに下記の二つの関数を割り当てる。

```
// ファイル以外のデータは受け取らない
private void Form1_DragEnter(object sender, DragEventArgs e)
{
  // ドラッグされたのがファイルであるか確認
  if (e.Data.GetDataPresent(DataFormats.FileDrop))
    // ドラッグされたデータを受け取る
    e.Effect = DragDropEffects.All;
  else
    // ドラッグされたデータを受け取らない
    e.Effect = DragDropEffects.None;
}

// drag & drop 時の処理
private void Form1_DragDrop(object sender, DragEventArgs e)
{
  string[] dlagFilePathArray = (string[])e.Data.GetData(DataFormats.FileDrop, false);

  // 複数のファイルがドラックされた場合、パスが配列として取得されるが、
  // 今回は TextBox が先頭のファイルのみを扱う。
  string filePath = dlagFilePathArray[0];
  string desktopPath = System.Environment.GetFolderPath(Environment.SpecialFolder.DesktopDirectory);
  // ファイルのパスを表示する
  MessageBox.Show(filePath,desktopPath);
}
```

## ドラッグでウィンドウを移動させる
1. フォームアプリケーション Form1 を作成。
2. Form1 の MouseMove のイベントに Form1_MouseMove の関数を割り当てる。
```
private void Form1_MouseMove(object sender, MouseEventArgs e)
{
  if ((e.Button & MouseButtons.Left) == MouseButtons.Left)
  {
    this.Left += e.X;
    this.Top += e.Y;
  }
}
```
## CSV データを扱う

## Excel データを扱う
1. フォームアプリケーション Form1 を作成
2. ソリューションエクスプローラーの参照設定を右クリックで参照の追加を選択
3. Microsoft Excel 12.0 Object Library を追加
4.
```
string filename = "test.xlsx";  //　エクセルファイル名

// エクセルの初期設定
Microsoft.Office.Interop.Excel.Application excel = new Microsoft.Office.Interop.Excel.Application();
excel.Visible = false;  //エクセルを非表示
Microsoft.Office.Interop.Excel.Workbook workbook = excel.Workbooks.Open(filename);  // ファイルを開く
Microsoft.Office.Interop.Excel.Worksheet sheet = workbook.Sheets[1];  // worksheet の選択
sheet.Select();

// sheet の cell[1,1] の値を読み取る
Microsoft.Office.Interop.Excel.Range range = sheet.Cells[1, 1];

// 読み取った cell[1,1] の値を cell[1,2]に書き込む
sheet.Cells[1, 2] = range.Value;

// save
workbook.Save();

// 閉じる
workbook.Close();
excel.Quit();
```
