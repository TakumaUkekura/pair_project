import json
import os
from src.main import main

def excute_main(mocker):
   mocker.patch("src.main.load_json", load_json_for_test)
   main()

# jsonファイルの読み込み
def load_json_for_test():
   with open("tests/mock.json", "r", encoding="utf-8") as f:
        invoices = json.load(f)
   with open("input/plays.json", "r", encoding="utf-8") as f:
        plays = json.load(f)
   return invoices, plays

# 出力テキストファイルを行ごとに読み込み
def get_lines_text_invoice():
   with open("output/invoice.txt", "r", encoding="utf-8") as f:
      result = f.readlines()
   return result

# 出力テキストファイルの内容を文字列として読み込み
def get_all_text_invoice():
   with open("output/invoice.txt", "r", encoding="utf-8") as f:
      result = f.read()
   return result

# 「請求書」というタイトルがあるか
def test_invoice_has_title(mocker):
   excute_main(mocker)
   invoice = get_lines_text_invoice()
   assert invoice[0].strip() == "請求書"

# 会社名があるか
def test_invoice_has_customer_name(mocker):
   excute_main(mocker)
   invoice = get_lines_text_invoice()
   assert invoice[1].strip() == "BigCo"

# Hamlet
def test_hamlet(mocker):
   excute_main(mocker)
   invoice = get_all_text_invoice()
   assert '・Hamlet（観客数：55人、金額：$65000）' in invoice

# As You Like It
def test_as_like(mocker):
   excute_main(mocker)
   invoice = get_all_text_invoice()
   assert '・As You Like It（観客数：35人、金額：$58000）' in invoice

# Othello
def test_othello(mocker):
   excute_main(mocker)
   invoice = get_all_text_invoice()
   assert '・Othello（観客数：40人、金額：$50000）' in invoice

# 合計金額
def test_total_price(mocker):
   excute_main(mocker)
   invoice = get_lines_text_invoice()
   total_price_line = invoice[-2].strip()
   total_price = int(total_price_line.split("合計金額：$")[1])
   assert total_price == 173000

# 獲得ポイント
def test_total_price(mocker):
   excute_main(mocker)
   invoice = get_lines_text_invoice()
   total_price_line = invoice[-1].strip()
   total_price = int(total_price_line.split("獲得ポイント：")[1].split("pt")[0])
   assert total_price == 47