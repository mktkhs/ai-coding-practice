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

## for index

for文の中で、繰り返しの回数や位置を表す変数を使う書き方。
`enumerate()`と組み合わせることが多い。

```python
for index in range(3):
    print(index)
```

出力:
```python
0
1
2
```

`index` は「何番目か」を表す変数で、リストの中の位置を扱うときに便利。

## enumerate()

リストや文字列などを順番に取り出しながら、インデックス番号も一緒に取得できる関数。

```python
fruits = ["apple", "banana", "grape"]
for index, fruit in enumerate(fruits):
    print(index, fruit)
```

出力:
```python
0 apple
1 banana
2 grape
```

`enumerate()` は、繰り返し処理の中で「何番目か」を知りたいときに便利。

## get(a, b)

辞書からキーを使って値を取り出すメソッド。
キーが存在しない場合は `b` を返す。

```python
counts = {"apple": 3, "banana": 2}
print(counts.get("apple", 0))
print(counts.get("orange", 0))
```

出力:
```python
3
0
```

`"orange"` のように存在しないキーにアクセスしたいとき、エラーではなく `0` を返してくれるので安全。

## setdefault()

辞書にキーがまだ存在しない場合だけ、そのキーを追加し、値を設定するメソッド。

```python
order = {}
order.setdefault("apple", 0)
order.setdefault("banana", 1)
print(order)
```

出力:
```python
{'apple': 0, 'banana': 1}
```

もし同じキーがすでに存在していれば、元の値をそのまま保つ。

## dict.fromkeys(a, b)

リストやタプルの要素を辞書のキーにして、すべての値を `b` にして辞書を作るメソッド。

```python
items = ["apple", "banana", "orange"]
result = dict.fromkeys(items, 0)
print(result)
```

出力:
```python
{'apple': 0, 'banana': 0, 'orange': 0}
```

この書き方は、重複を取り除くときにも使える。

```python
items = ["apple", "banana", "apple", "orange"]
unique = list(dict.fromkeys(items))
print(unique)
```

出力:
```python
['apple', 'banana', 'orange']
```

## sorted(a, key=lambda b: x[b])

`sorted()` はリストを並び替える関数で、`key` を使うと並び替えの基準を決められる。

```python
scores = {"apple": 3, "banana": 2, "orange": 5}
result = sorted(scores, key=lambda x: scores[x])
print(result)
```

出力:
```python
['banana', 'apple', 'orange']
```

これは `scores` のキーを値の小さい順に並べ替えている。

`key=lambda item: (-counts[item], order[item])` のように書くと、
- 出現回数の多い順
- その中で元の順に並ぶ

という並び替えができる。

`lambda` は簡単な関数を一時的に作るための書き方で、`key` のルールを短く書ける。

## まとめ

今回の学習では、以下の要素を使って「重複を除いて頻度順に並べる」処理を作成した。

- `for index`
- `enumerate()`
- `get(a, b)`
- `setdefault()`
- `dict.fromkeys(a, b)`
- `sorted(a, key=lambda b: x[b])`

これらは、辞書とループを使ったデータ処理で非常に役立つ記法である。

## 例題1: `enumerate()` を使って位置を確認する

```python
fruits = ["apple", "banana", "orange"]
for index, fruit in enumerate(fruits):
    print(f"{index}番目: {fruit}")
```

出力:
```python
0番目: apple
1番目: banana
2番目: orange
```

## 例題2: `get()` を使って存在しないキーを安全に扱う

```python
counts = {"apple": 3, "banana": 2}
print(counts.get("apple", 0))
print(counts.get("grape", 0))
```

出力:
```python
3
0
```

## 例題3: `setdefault()` で辞書に初期値を入れる

```python
order = {}
order.setdefault("apple", 0)
order.setdefault("banana", 1)
order.setdefault("apple", 99)
print(order)
```

出力:
```python
{'apple': 0, 'banana': 1}
```

`apple` はすでに存在しているので、`99` は上書きされない。

## 例題4: `dict.fromkeys()` で重複を除く

```python
items = ["A", "B", "A", "C", "B"]
unique_items = list(dict.fromkeys(items))
print(unique_items)
```

出力:
```python
['A', 'B', 'C']
```

## 例題5: `sorted()` と `lambda` で頻度順に並べる

```python
counts = {"apple": 3, "banana": 2, "orange": 3, "grape": 1}
result = sorted(counts, key=lambda x: (-counts[x], x))
print(result)
```

出力:
```python
['apple', 'orange', 'banana', 'grape']
```

`-counts[x]` により、出現回数が多い順に並び、同じ回数なら文字で並ぶ。

## 例題6: まとめて使う

```python
items = ["apple", "banana", "apple", "orange", "banana", "apple", "grape"]
counts = {}
for item in items:
    counts[item] = counts.get(item, 0) + 1

unique_items = list(dict.fromkeys(items))
result = sorted(unique_items, key=lambda x: (-counts[x], items.index(x)))
print(result)
```

出力:
```python
['apple', 'banana', 'orange', 'grape']
```

この例では、辞書の作成・重複除去・並び替えを一連の流れで扱っている。