import json
import os

# スクリプトファイルのディレクトリを取得
script_dir = os.path.dirname(os.path.abspath(__file__))
# プロジェクトのルートディレクトリを取得（srcの親ディレクトリ）
project_root = os.path.dirname(script_dir)

# inputディレクトリからJSONファイルを読み込み
with open(os.path.join(project_root, 'input', 'invoices.json'), 'r') as f:
    invoice = json.load(f)

with open(os.path.join(project_root, 'input', 'plays.json'), 'r') as f:
    plays = json.load(f)

# ルートディレクトリのoutputディレクトリが存在しない場合は作成
output_dir = os.path.join(project_root, 'output')
os.makedirs(output_dir, exist_ok=True)

# テキストファイルとして出力
with open(os.path.join(output_dir, 'invoice_data.txt'), 'w', encoding='utf-8') as f:
    f.write("=== Invoice Data ===\n")
    f.write(json.dumps(invoice, indent=2, ensure_ascii=False))
    f.write("\n\n")

with open(os.path.join(output_dir, 'plays_data.txt'), 'w', encoding='utf-8') as f:
    f.write("=== Plays Data ===\n")
    f.write(json.dumps(plays, indent=2, ensure_ascii=False))
    f.write("\n")

# 統合されたデータも出力
with open(os.path.join(output_dir, 'combined_data.txt'), 'w', encoding='utf-8') as f:
    f.write("=== Combined Data ===\n")
    f.write("Invoice:\n")
    f.write(json.dumps(invoice, indent=2, ensure_ascii=False))
    f.write("\n\nPlays:\n")
    f.write(json.dumps(plays, indent=2, ensure_ascii=False))
    f.write("\n")

print("データがoutputディレクトリにテキストファイルとして出力されました:")
print("- output/invoice_data.txt")
print("- output/plays_data.txt") 
print("- output/combined_data.txt")