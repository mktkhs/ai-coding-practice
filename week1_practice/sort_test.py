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
    items = input("並び替えたい要素をカンマ区切りで入力してください: ").split(',')
    result = sort_by_frequency(items)
    print("元のリスト:", items)
    print("頻度順:", result)
