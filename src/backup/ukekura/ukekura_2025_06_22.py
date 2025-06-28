from input import input
from output import output


class TradeItem:
    def __init__(self, id, name, play_type, audience):
        self.id = id
        self.name = name
        self.play_type = play_type
        self.audience = audience
        self.price = None
        self.point = None
        self.calculate_price_and_point()

    def calculate_price_and_point(self):
        if self.play_type == "tragedy":
            self.price = calc_tragedy_price(self.audience)
            self.point = calc_tragedy_point(self.audience)
        elif self.play_type == "comedy":
            self.price = calc_comedy_price(self.audience)
            self.point = calc_comedy_point(self.audience)

    @classmethod
    def from_invoice_and_plays(cls, invoice, plays):
        trade_items = []
        for performance in invoice["performances"]:
            play_id = performance["playID"]
            play_info = plays[play_id]
            name = play_info["name"]
            play_type = play_info["type"]
            audience = performance["audience"]
            item = cls(id=play_id, name=name, play_type=play_type, audience=audience)
            trade_items.append(item)
        return trade_items

    def __repr__(self):
        return f"TradeItem(id={self.id}, name={self.name}, play_type={self.play_type}, audience={self.audience}, price={self.price}, point={self.point})"

def get_trade_info_list(invoice, plays):
    performance_name_list = [plays[performance["playID"]]["name"] for performance in invoice["performances"]]
    audience_number_list = [performance["audience"] for performance in invoice["performances"]]
    return performance_name_list, audience_number_list

def get_audience_number_list(invoice):
    audience_number_list = []
    for performance in invoice["performances"]:
        audience_number_list.append(performance["audience"])
    return audience_number_list


def get_price_list(invoice, plays):
    price_and_point_list = [get_price_and_point(plays[performance["playID"]]["type"], performance["audience"]) for performance in invoice["performances"]]
    price_list, point_list = zip(*price_and_point_list)
    return list(price_list), list(point_list)

def get_price_and_point(play_type, audience_number):
    if play_type == "tragedy":
       price = calc_tragedy_price(audience_number)
       point = calc_tragedy_point(audience_number)
    if play_type == "comedy":
        price = calc_comedy_price(audience_number)
        point = calc_comedy_point(audience_number)
    return price, point

def calc_tragedy_price(audience_number):
    price= 40000 # 基本料金40000$
    if (audience_number > 30):# 観客数が30人を超過する場合
        price+= 1000 * (audience_number - 30)
    return price

def calc_comedy_price(audience_number):
    price= 30000
    price += 300 * audience_number
    if (audience_number > 20): # 観客数が20人を超える場合、
        price+= 1000 
        price += (500 * (audience_number - 20))
    return price

def calc_tragedy_point(audience_number):
    result = max(audience_number - 30, 0)
    return result

def calc_comedy_point(audience_number):
    result = max(audience_number - 30, 0)
    result += audience_number // 5
    return result

def create_invoice_content(invoice, plays):

    invoice_content = ""

    invoice_title = "請求書"
    company_name = "会社名：" + invoice["customer"]
    trade_content = ""
    total_price = 0
    total_point = 0

    invoice_content += invoice_title + "\n"
    invoice_content += company_name + "\n"

    performance_name_list, audience_number_list = get_trade_info_list(invoice, plays)
    # audience_number_list = get_audience_number_list(invoice)
    price_list, type_list = get_price_list(invoice, plays)

    for i in range(len(invoice["performances"])):
        trade_content += "・" + performance_name_list[i] + "（観客数："
        trade_content += str(audience_number_list[i]) + "人、金額："
        trade_content += str(price_list[i]) + "）\n"
        total_price += price_list[i]
        total_point += type_list[i]
    

    invoice_content += trade_content

    invoice_content += "合計金額：" + str(total_price) + "円\n"
    invoice_content += "獲得ポイント：" + str(total_point) + "pt"

    return invoice_content

def main():
    invoice, plays = input()
    trade_items = TradeItem.from_invoice_and_plays(invoice, plays)
    print(trade_items)
    invoice_content = create_invoice_content(invoice, plays)
    output(invoice_content)
    
main()

