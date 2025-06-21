import json
import os

# inputディレクトリからJSONファイルを読み込み
with open('input/invoices.json', 'r') as f:
    invoice = json.load(f)

with open('input/plays.json', 'r') as f:
    plays = json.load(f)

# outputディレクトリが存在しない場合は作成
os.makedirs('output', exist_ok=True)

# テキストファイルとして出力
with open('output/invoice_data.txt', 'w', encoding='utf-8') as f:
    f.write("=== Invoice Data ===\n")
    f.write(json.dumps(invoice, indent=2, ensure_ascii=False))
    f.write("\n\n")

with open('output/plays_data.txt', 'w', encoding='utf-8') as f:
    f.write("=== Plays Data ===\n")
    f.write(json.dumps(plays, indent=2, ensure_ascii=False))
    f.write("\n")

# 統合されたデータも出力
with open('output/combined_data.txt', 'w', encoding='utf-8') as f:
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