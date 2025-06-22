import json
import os

# スクリプトファイルのディレクトリを取得
script_dir = os.path.dirname(os.path.abspath(__file__))
# プロジェクトのルートディレクトリを取得（srcの親ディレクトリ）
project_root = os.path.dirname(script_dir)
# ルートディレクトリのoutputディレクトリが存在しない場合は作成
output_dir = os.path.join(project_root, 'output')

def input():
    # inputディレクトリからJSONファイルを読み込み
    with open(os.path.join(project_root, 'input', 'invoices.json'), 'r') as f:
        invoice = json.load(f)

    with open(os.path.join(project_root, 'input', 'plays.json'), 'r') as f:
        plays = json.load(f)
    return invoice, plays


def create_invoice_content(invoice, plays):

    invoice_title = "請求書"
    company_name = "会社名：" + invoice[0]["customer"]
    trade_content = ""

    trade_content += invoice_title + "\n"
    trade_content += company_name + "\n"

    performance_name_list = get_performances_name_list(invoice, plays)
    audience_number_list = get_audience_number_list(invoice)
    price_list = get_price_list(invoice, plays)

    for i in range(len(invoice[0]["performances"])):
        trade_content += "・" + performance_name_list[i] + "（観客数："
        trade_content += str(audience_number_list[i]) + "人、金額："
        trade_content += str(price_list[i]) + "）\n"
    
    invoice_content = trade_content

    return invoice_content


def get_performances_name_list(invoice, plays):
    performance_name_list = []
    for performance in invoice[0]["performances"]:
        performance_name_list.append(plays[performance["playID"]]["name"])
    return performance_name_list

def get_audience_number_list(invoice):
    audience_number_list = []
    for performance in invoice[0]["performances"]:
        audience_number_list.append(performance["audience"])
    return audience_number_list

def get_price_list(invoice, plays):
    price_list = []
    for performance in invoice[0]["performances"]:
        if plays[performance["playID"]]["type"] == "tragedy":
            Ryoukin = 40000 # 基本料金40000$
            if (performance["audience"] > 30):# 観客数が30人を超過する場合
                Ryoukin += (1000 * (performance["audience"] - 30)) # 超過一人当たり1000$
        if plays[performance["playID"]]["type"] == "comedy":
            Ryoukin = 30000 # 基本料金30000$
            if (performance["audience"] > 20): # 観客数が20人を超える場合、
                Ryoukin += 1000 # 10000$を追加した上で、
                Ryoukin += (500 * (performance["audience"] - 20)) # さらに超過一人当たり500$
        price_list.append(Ryoukin)
    return price_list


def output(output):
    print(output)
    # # ルートディレクトリのoutputディレクトリが存在しない場合は作成
    # os.makedirs(output_dir, exist_ok=True)
    # # テキストファイルとして出力
    # with open(os.path.join(output_dir, 'invoice.txt'), 'w', encoding='utf-8') as f:
    #     f.write(output)

    # print("データがoutputディレクトリにテキストファイルとして出力されました:")

def main():
    invoice, plays = input()
    invoice_content = create_invoice_content(invoice, plays)
    output(invoice_content)
    
main()