import json
import os
from src.main import main

def excute_main():
   os.environ["USE_MOCK"] = "1"
   main()

# jsonファイルの読み込み
def load_json():
   with open("input/invoices.json", "r", encoding="utf-8") as f:
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
def test_invoice_has_title():
   excute_main()
   invoice = get_lines_text_invoice()
   assert invoice[0].strip() == "請求書"

# 会社名があるか
def test_invoice_has_customer_name():
   excute_main()
   invoice = get_lines_text_invoice()
   assert invoice[1].strip() == "BigCo"

# invoice.jsonにある劇名が全て請求書に含まれているか
def test_invoice_has_all_performance_name():
   invoices, plays = load_json()
   performance_name = [plays[performance["playID"]]["name"] for performance in invoices[0]["performances"]]
   excute_main()
   invoice = get_all_text_invoice()
   for i in range(len(performance_name)):
       assert performance_name[i] in invoice

# 各演目の観客数
def test_hamlet_audience():
   excute_main()
   invoice = get_lines_text_invoice()
   target_line = [line for line in invoice if "Hamlet" in line]
   audience_count = int(target_line[0].split("観客数：")[1].split("人")[0])
   assert audience_count == 55

def test_as_like_audience():
   excute_main()
   invoice = get_lines_text_invoice()
   target_line = [line for line in invoice if "As You Like It" in line]
   audience_count = int(target_line[0].split("観客数：")[1].split("人")[0])
   assert audience_count == 35

def test_othello_audience():
   excute_main()
   invoice = get_lines_text_invoice()
   target_line = [line for line in invoice if "Othello" in line]
   audience_count = int(target_line[0].split("観客数：")[1].split("人")[0])
   assert audience_count == 40

# 各演目の金額
def test_hamlet_price():
   excute_main()
   invoice = get_lines_text_invoice()
   target_line = [line for line in invoice if "Hamlet" in line]
   price = int(target_line[0].split("金額：$")[1].split("）")[0])
   assert price == 65000

def test_as_like_price():
   excute_main()
   invoice = get_lines_text_invoice()
   target_line = [line for line in invoice if "As You Like It" in line]
   price = int(target_line[0].split("金額：$")[1].split("）")[0])
   assert price == 58000

def test_othello_price():
   excute_main()
   invoice = get_lines_text_invoice()
   target_line = [line for line in invoice if "Othello" in line]
   price = int(target_line[0].split("金額：$")[1].split("）")[0])
   assert price == 50000

# 合計金額
def test_total_price():
   excute_main()
   invoice = get_lines_text_invoice()
   total_price_line = invoice[-2].strip()
   total_price = int(total_price_line.split("合計金額：$")[1])
   assert total_price == 173000

# 獲得ポイント
def test_total_price():
   excute_main()
   invoice = get_lines_text_invoice()
   total_price_line = invoice[-1].strip()
   total_price = int(total_price_line.split("獲得ポイント：")[1].split("pt")[0])
   assert total_price == 47