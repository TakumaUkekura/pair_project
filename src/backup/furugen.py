import json
import os

# スクリプトファイルのディレクトリを取得
script_dir = os.path.dirname(os.path.abspath(__file__))
# プロジェクトのルートディレクトリを取得（srcの親ディレクトリ）
project_root = os.path.dirname(script_dir)
# ルートディレクトリのoutputディレクトリが存在しない場合は作成
output_dir = os.path.join(project_root, 'output')

COMEDY_PRICE = 30000
TRAGEDY_PRICE = 40000

def load_invoces_json():
    with open(os.path.join(project_root, 'input', 'invoices.json'), 'r') as f:
        return json.load(f)

def load_plays_json():
    with open(os.path.join(project_root, 'input', 'plays.json'), 'r') as f: # TODO: invoeceと同様の記述なのでまとめたい
        return json.load(f)

def get_company_name(invoice):
    company_name = invoice[0]["customer"]
    return company_name

def get_play_info(play_id):
    plays = load_plays_json()
    play_name = ""
    play_type = ""
    if play_id in plays:
        play_name = plays[play_id]["name"]
        play_type = plays[play_id]["type"]
    return play_name, play_type

def calc_price(play_type, audience):
    price = 0
    if play_type == "tragedy": # TODO: 直打ちは避けたい。定数に切り分ける？
        price = TRAGEDY_PRICE
        if (audience > 30):
            price += (1000 * (audience - 30))
    if play_type == "comedy":
        price = COMEDY_PRICE
        if (audience > 20):
            price += 1000
            price += (500 * (audience - 20))
            price += (300 * audience)
    return price

def calc_point(play_type, audience):
    point = 1 * (audience - 30)
    if play_type == "comedy":
      point += 1 * audience//5
    return point

def create_invoice_header(invoice_data):
    invoice_header = ""
    invoice_title = "請求書"
    company_name = get_company_name(invoice_data)
    invoice_header += invoice_title + "\n"
    invoice_header += "会社名：" + company_name + "\n"
    return invoice_header

def create_invoice_row(play_name, audience, price):
    invoice_row = ""
    invoice_row += "・" + play_name
    invoice_row += "（観客数：" + str(audience) + "人、"
    invoice_row += "金額：" + str(price) + "円）\n"
    return invoice_row

def create_invoice_footer(total_price, total_point):
    invoice_footer = ""
    invoice_footer += "合計金額：" + str(total_price) + "円\n"
    invoice_footer += "獲得ポイント：" + str(total_point) + "pt"
    return invoice_footer

def create_invoice_content(invoice_data):
    invoice_body = ""
    total_price = 0
    total_point = 0

    invoice_header = create_invoice_header(invoice_data)

    for performance in invoice_data[0]["performances"]:

        play_name, play_type = get_play_info(performance["playID"]) # TODO: for文の中で毎回playをロードしているのを避けたい
        if (play_name == "" or play_type == ""): # TODO: エラー判定はここで行うべきなのか？他の判定の考慮も
            print("play is invalid")
            continue

        audience = performance["audience"]
        invoice_body += create_invoice_row(play_name, audience, calc_price(play_type, audience))
        total_price += calc_price(play_type, audience)
        total_point += calc_point(play_type, audience)

    invoice_footer = create_invoice_footer(total_price, total_point)

    trade_contents = invoice_header + invoice_body + invoice_footer
    return trade_contents

def output(output):
    print(output)
    # # ルートディレクトリのoutputディレクトリが存在しない場合は作成
    # os.makedirs(output_dir, exist_ok=True)
    # # テキストファイルとして出力
    # with open(os.path.join(output_dir, 'invoice.txt'), 'w', encoding='utf-8') as f:
    #     f.write(output)

    # print("データがoutputディレクトリにテキストファイルとして出力されました:")

def main():
    invoice_data = load_invoces_json()
    invoice_content = create_invoice_content(invoice_data)
    output(invoice_content)
    
main()
