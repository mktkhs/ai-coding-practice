def sort_by_frequency(items):
    """重複を除き、出現頻度が高い順に並び替えたリストを返す。"""
    counts = {} #要素ごとの出現頻度
    order = {} #要素ごとの最初の出現位置

    for index, item in enumerate(items): #単にitemsではダメなのか？
        counts[item] = counts.get(item, 0) + 1
        order.setdefault(item, index)

    unique_items = list(dict.fromkeys(items))
    return sorted(unique_items, key=lambda item: (-counts[item], order[item]))


if __name__ == "__main__":
    sample = ["apple", "banana", "apple", "or,ange", "banana", "apple", "grape", "orange"]
    # 要素内に,が含まれていても正常に動作する
    result = sort_by_frequency(sample)
    print("元のリスト:", sample)
    print("頻度順:", result)
