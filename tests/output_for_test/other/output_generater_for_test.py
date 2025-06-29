import os
import json
import csv

INPUT_DIR = os.path.join(os.path.dirname(__file__), '../../input_for_test')
CSV_PATH = os.path.join(os.path.dirname(__file__), 'invoice_output_pattern.csv')
OUTPUT_DIR = os.path.join(os.path.dirname(__file__), '../')

# CSVを辞書化（大文字小文字無視のためlowerで統一）
def playid_to_fullname(short):
    mapping = {
        'hamlet': 'Hamlet',
        'as-like': 'As You Like It',
        'othello': 'Othello',
    }
    return mapping.get(short.lower(), short)

def load_pattern(csv_path):
    pattern = {}
    with open(csv_path, encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            key = (row['playID'].strip(), int(row['audience']))
            pattern[key] = {'price': int(row['price']), 'point': int(row['point']), 'playID': row['playID']}
    return pattern

pattern_dict = load_pattern(CSV_PATH)

# sample_invoice.txtのフォーマット例
# 顧客名: TestCase No.35
# Hamlet: 41,000 (31人)
# As You Like It: 35,400 (18人)
# Othello: 40,000 (29人)
# 合計金額: 116,400
# 獲得ポイント: 4

def format_invoice(customer, performances):
    lines = ["請求書", f"{customer}"]
    total_price = 0
    total_point = 0
    for perf in performances:
        play_id_short = perf['playID'].strip()
        play_id_full = playid_to_fullname(play_id_short)
        audience = int(perf['audience'])
        key = (play_id_full, audience)
        if key not in pattern_dict:
            raise ValueError(f'パターンが見つかりません: {perf}')
        play_name = pattern_dict[key]['playID']
        price = pattern_dict[key]['price']
        point = pattern_dict[key]['point']
        lines.append(f'・{play_name}（観客数：{audience}人、金額：${price}）')
        total_price += price
        total_point += point
    lines.append(f'合計金額：${total_price}')
    lines.append(f'獲得ポイント：{total_point}pt')
    return '\n'.join(lines)

# input_for_test内のjsonファイルを処理
def main():
    for fname in os.listdir(INPUT_DIR):
        if not fname.endswith('.json'):
            continue
        with open(os.path.join(INPUT_DIR, fname), encoding='utf-8') as f:
            data = json.load(f)
        # dataがリスト形式の場合は最初の要素を使う
        if isinstance(data, list):
            data = data[0]
        customer = data['customer']
        performances = data['performances']
        invoice_text = format_invoice(customer, performances)
        outname = os.path.splitext(fname)[0] + '.txt'
        outpath = os.path.join(OUTPUT_DIR, outname)
        with open(outpath, 'w', encoding='utf-8') as outf:
            outf.write(invoice_text)

if __name__ == '__main__':
    main()
