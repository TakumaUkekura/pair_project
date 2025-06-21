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


invoice_content = "請求書"


# ルートディレクトリのoutputディレクトリが存在しない場合は作成
output_dir = os.path.join(project_root, 'output')
os.makedirs(output_dir, exist_ok=True)

# テキストファイルとして出力
with open(os.path.join(output_dir, 'invoice.txt'), 'w', encoding='utf-8') as f:
    f.write(invoice_content)

print("データがoutputディレクトリにテキストファイルとして出力されました:")