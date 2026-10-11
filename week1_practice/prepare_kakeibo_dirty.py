from pathlib import Path
import random

import pandas as pd


BASE_DIR = Path(__file__).resolve().parent
INPUT_PATH = BASE_DIR / "kakeibo2025.csv"
OUTPUT_PATH = BASE_DIR / "kakeibo_dirty.csv"
EXPECTED_COLUMNS = ["日付", "カテゴリ", "金額", "メモ"]
RANDOM_SEED = 20261008


def main():
    if not INPUT_PATH.is_file():
        raise FileNotFoundError(f"入力ファイルがありません: {INPUT_PATH.name}")
    if OUTPUT_PATH.exists():
        raise FileExistsError(
            f"出力ファイルが既にあります。上書きしません: {OUTPUT_PATH.name}"
        )

    data = pd.read_csv(
        INPUT_PATH,
        dtype={"日付": "string", "カテゴリ": "string", "金額": "Int64", "メモ": "string"},
    )
    if list(data.columns) != EXPECTED_COLUMNS:
        raise ValueError(f"CSVの列が想定と異なります: {list(data.columns)}")

    row_count = len(data)
    if row_count != 500:
        raise ValueError(f"元データは500行を想定しています。現在: {row_count}行")

    parsed_dates = pd.to_datetime(data["日付"], format="%Y-%m-%d", errors="raise")
    if not (parsed_dates.dt.year == 2025).all():
        raise ValueError("日付はすべて2025年である必要があります")

    rent_mask = data["カテゴリ"].eq("住宅費")
    course_mask = data["カテゴリ"].eq("教育費") & data["メモ"].eq("通信講座費")

    def check_monthly_schedule(mask, label, expected_day):
        selected_dates = parsed_dates.loc[mask]
        if len(selected_dates) != 12 or set(selected_dates.dt.month) != set(range(1, 13)):
            raise ValueError(f"{label}は1月から12月まで各月1件必要です")
        if not selected_dates.dt.day.eq(expected_day).all():
            raise ValueError(f"{label}の日付は毎月{expected_day}日である必要があります")

    check_monthly_schedule(rent_mask, "家賃", 1)
    check_monthly_schedule(course_mask, "通信講座費", 15)
    data.loc[rent_mask, "金額"] = 95000

    reserved_mask = rent_mask | course_mask
    editable_indices = data.index[~reserved_mask].tolist()
    rng = random.Random(RANDOM_SEED)

    missing_count = round(row_count * 0.03)
    category_variation_count = round(row_count * 0.05)
    slash_date_count = round(row_count * 0.05)
    outlier_count = 3

    missing_indices = set(rng.sample(editable_indices, missing_count))
    remaining_indices = [index for index in editable_indices if index not in missing_indices]
    category_indices = set(rng.sample(remaining_indices, category_variation_count))
    remaining_indices = [index for index in remaining_indices if index not in category_indices]
    outlier_indices = set(rng.sample(remaining_indices, outlier_count))

    date_indices = set(rng.sample(data.index.tolist(), slash_date_count))
    time_seconds = {
        index: rng.randrange(24 * 60 * 60)
        for index in data.index
    }

    # 定期支出は請求時刻をそろえ、その他の記録には時刻のばらつきを加える。
    for index in data.index[rent_mask | course_mask]:
        time_seconds[index] = 9 * 60 * 60
    timestamps = parsed_dates + pd.to_timedelta(
        pd.Series(time_seconds), unit="s"
    )
    date_text = timestamps.dt.strftime("%Y-%m-%d %H:%M:%S")
    slash_date_text = timestamps.dt.strftime("%Y/%m/%d %H:%M:%S")
    data["日付"] = date_text
    for index in date_indices:
        data.at[index, "日付"] = slash_date_text.at[index]

    data.loc[list(missing_indices), "金額"] = pd.NA

    category_variants = {
        "食費": ["食費 ", "食費　"],
        "交通費": ["交通費 ", "交通費　", "交通費(ﾊﾞｽ)"],
        "日用品": ["日用品 ", "日用品　"],
        "娯楽": ["娯楽 ", "娯楽　"],
        "光熱費": ["光熱費 ", "光熱費　"],
        "交際費": ["交際費 ", "交際費　"],
        "医療費": ["医療費 ", "医療費　"],
        "教育費": ["教育費 ", "教育費　"],
        "その他": ["その他 ", "その他　"],
    }
    for index in category_indices:
        original_category = data.at[index, "カテゴリ"]
        data.at[index, "カテゴリ"] = rng.choice(category_variants[original_category])

    for index, amount in zip(sorted(outlier_indices), [9999999, -50000, 0]):
        data.at[index, "金額"] = amount

    # 複製元は欠損・カテゴリ揺れ・異常値の対象外から選ぶ。
    duplicate_candidates = [
        index
        for index in editable_indices
        if index not in missing_indices
        and index not in category_indices
        and index not in outlier_indices
    ]
    duplicate_indices = rng.sample(duplicate_candidates, 3)
    duplicates = data.loc[duplicate_indices].copy()
    data = pd.concat([data, duplicates], ignore_index=True)

    if data["金額"].isna().sum() != missing_count:
        raise AssertionError("金額の欠損件数が想定と異なります")
    if data.duplicated().sum() < 3:
        raise AssertionError("完全な重複行が3件ありません")

    data.to_csv(OUTPUT_PATH, index=False, encoding="utf-8")
    print(f"出力先: {OUTPUT_PATH.name}")
    print(f"データ行数: {len(data)}")
    print(f"金額欠損: {missing_count}件")
    print(f"カテゴリ表記揺れ: {category_variation_count}件")
    print(f"スラッシュ形式の日付: {slash_date_count}件")
    print("完全な重複行: 3件追加")
    print(f"異常値: {outlier_count}件")


if __name__ == "__main__":
    main()