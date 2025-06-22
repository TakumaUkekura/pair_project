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
    with open(os.path.join(project_root, 'input', 'plays.json'), 'r') as f:
        return json.load(f)

def get_title():
    return "請求書"

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

def get_base_price(play_type):
    base_price = 0
    if play_type == "comedy":
        base_price = COMEDY_PRICE
    if play_type == "tragedy":
        base_price = TRAGEDY_PRICE
    return base_price

def calc_price(play_type, audience):
    price = get_base_price(play_type)
    if play_type == "tragedy":
        if (audience > 30):
            price += (1000 * (audience - 30))
    if play_type == "comedy":
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

def create_invoice_content(invoice):
    trade_contents = ""

    invoice_title = get_title()
    company_name = get_company_name(invoice)
    total_price = 0
    total_point = 0

    trade_contents += invoice_title + "\n"
    trade_contents += "会社名：" + company_name + "\n"

    for performance in invoice[0]["performances"]:
        play_name, play_type = get_play_info(performance["playID"])
        if (play_name == "" or play_type == ""):
            print("play is invalid")
            continue
        
        audience = performance["audience"]
        price = calc_price(play_type, audience)
        point = calc_point(play_type, audience)

        trade_contents += "・" + play_name
        trade_contents += "（観客数：" + str(audience) + "人、"
        trade_contents += "金額：" + str(price) + "円）\n"

        total_price += price
        total_point += point

    trade_contents += "合計金額：" + str(total_price) + "円\n"
    trade_contents += "獲得ポイント：" + str(total_point) + "pt"

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
    invoice = load_invoces_json()
    invoice_content = create_invoice_content(invoice)
    output(invoice_content)
    
main()
