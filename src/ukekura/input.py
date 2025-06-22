import json
import os

# スクリプトファイルのディレクトリを取得
script_dir = os.path.dirname(os.path.abspath(__file__))
# プロジェクトのルートディレクトリを取得（srcの親ディレクトリ）
project_root = os.path.dirname(script_dir)
# ルートディレクトリのoutputディレクトリが存在しない場合は作成
output_dir = os.path.join(project_root, 'output')

def load_json_for(file_name: str):
    with open(os.path.join(project_root, '../input', file_name), 'r') as f:
        result = json.load(f)
    return result

def format(invoices):
    result = invoices[0]
    return result

def input():
    invoice = format(load_json_for('invoices.json'))
    plays = load_json_for('plays.json')
    return invoice, plays