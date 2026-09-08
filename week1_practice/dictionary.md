# 学習メモ

新しく知った関数や記述をまとめるメモファイルです。

## print()

コンソール（画面）に文字や値を出力する関数。

```python
print("Hello, World!")
```

## input()

ユーザーからキーボード入力を受け取る関数。戻り値は常に文字列型。

```python
name = input("名前を入力してください: ")
```

## try / except

エラー（例外）が発生しそうな処理を`try`ブロックに書き、エラーが起きたときの処理を`except`に書く仕組み。プログラムが異常終了せずに済む。

```python
try:
    num = float(input("数値: "))
except ValueError:
    print("無効な数値です。")
```
上記の例では、numの変換にあたってValueErrorが起きたときの処理を書いている。


## f文字列（f-string）

文字列の前に`f`をつけると、`{}`の中に変数や式を埋め込める。

```python
result = 5
print(f"結果: {result}")
```

## if __name__ == "__main__":

ファイルが直接実行されたときだけ処理を実行するための書き方。他のファイルから`import`されたときは実行されない。

```python
if __name__ == "__main__":
    main()
```

## not in

値が、指定した複数の値のどれにも一致しないかを判定する。`in`（含まれるか）の否定形。

```python
choice = "3"
if choice not in ("1", "2"):
    print("無効な選択です。")
```

## return

関数の実行をそこで終了し、呼び出し元に値を返す（値がない場合は`None`が返る）。関数の途中で処理を打ち切りたいときにも使う。

```python
def check(choice):
    if choice not in ("1", "2"):
        print("無効な選択です。")
        return  # ここで関数の処理を終了する

    print("有効な選択です。")
```
上記の場合、returnの次点で処理が終了し、check関数を呼び出した場所までNoneが戻る。
returnに何か戻り値を与えていたら、その戻り値が戻る。