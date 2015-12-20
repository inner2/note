# swift 現在の日時を文字列で取得する
swift sample
```
let now = NSDate()
let formatter = NSDateFormatter()
formatter.dateFormat = "yyyy/MM/dd HH:mm:ss"
let date = formatter.stringFromDate(now)
```
