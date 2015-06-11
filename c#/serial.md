# Serial 通信
## シリアル通信とは
電気通信において伝送路上を一度に1ビットずつ、逐次的にデータを送ることをいう。 また、コンピュータにおいては、バス上を一度に1ビットずつ、逐次的にデータを送ることをいう。

## 送信
1. Windows form application を作成
2. ツールボックスから SerialPortを使用する。
```
private SerialPort sp = new SerialPort("COM3", 9600);
sp.Open();
sp.Write("a");
```
