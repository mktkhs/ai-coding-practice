def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def main():
    print("簡単な電卓（足し算・引き算）")
    print("計算方法を選んでください: 1) 足し算  2) 引き算")

    choice = input("番号を入力してください (1 または 2): ") #inputを求め、同時にその内容をchioceに代入

    if choice not in ("1", "2"):
        print("無効な選択です。1 または 2 を入力してください。")
        return

    try:
        num1 = float(input("1つ目の数値を入力してください: "))
        num2 = float(input("2つ目の数値を入力してください: "))
    except ValueError:
        print("無効な数値です。")
        return

    if choice == "1":
        print(f"結果: {num1} + {num2} = {add(num1, num2)}")
    else:
        print(f"結果: {num1} - {num2} = {subtract(num1, num2)}")


if __name__ == "__main__":
    main()
