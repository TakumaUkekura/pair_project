import json
import os
from allpairspy import AllPairs

# 各演目の観客数の候補
parameters = [
    [0, 29, 30, 31],  # Hamlet
    [0, 4, 5, 6, 19, 20, 21, 30, 31, 35],  # As You Like It
    [0, 29, 30, 31]  # Othello
]

# 対応する演目ID
play_ids = ["hamlet", "as-like", "othello"]

# 出力ディレクトリ
output_dir = "tests/input_for_test"
os.makedirs(output_dir, exist_ok=True)

# テストケース番号のカウント（スキップする可能性があるため手動カウント）
testcase_number = 1

# AllPairsで生成されたペアワイズ組み合わせを各JSONファイルとして保存
for pairs in AllPairs(parameters):
    # 観客数が0のものは含めない
    performances = [
        {"playID": play_id, "audience": audience}
        for play_id, audience in zip(play_ids, pairs)
        if audience != 0
    ]

    # すべて0で空になったらスキップ
    if not performances:
        continue

    data = {
        "customer": f"TestCase No.{testcase_number}",
        "performances": performances
    }

    # 外側をリストで囲む
    data_list = [data]

    file_path = os.path.join(output_dir, f"testcase_{testcase_number}.json")
    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(data_list, f, indent=2, ensure_ascii=False)

    testcase_number += 1

print(f"{testcase_number - 1} 件のテストケースを '{output_dir}' に保存しました。")
