import json
import os

def load_json():
    """JSONファイルを読み込む関数"""
    script_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.dirname(script_dir)
    
    with open(os.path.join(project_root, 'input', 'invoices.json'), 'r') as f:
        invoice = json.load(f)
    
    with open(os.path.join(project_root, 'input', 'plays.json'), 'r') as f:
        plays = json.load(f)
    
    return invoice, plays

def main():
    """メイン処理関数"""
    invoice, plays = load_json()
    
    seikyuusyo = "請求書" + "\n"
    seikyuusyo += invoice[0]["customer"] + "\n"
    goukei = 0
    point = 0

    for performance in invoice[0]["performances"]:
        if plays[performance["playID"]]["type"] == "tragedy":
            Ryoukin = 40000 # 基本料金40000$
            if (performance["audience"] > 30):# 観客数が30人を超過する場合
                Ryoukin += (1000 * (performance["audience"] - 30)) # 超過一人当たり1000$
        if plays[performance["playID"]]["type"] == "comedy":
            point += 1 * performance["audience"]//5
            Ryoukin = 30000 # 基本料金30000$
            if (performance["audience"] > 20): # 観客数が20人を超える場合、
                Ryoukin += 10000 # 10000$を追加した上で、
                Ryoukin += (500 * (performance["audience"] - 20)) # さらに超過一人当たり500$

        goukei += Ryoukin
        
        if performance["audience"] > 30:
            point += 1 * (performance["audience"] - 30)
        
        seikyuusyo += "・" + plays[performance["playID"]]["name"] + "（観客数：" + str(performance["audience"]) + "人、" + "金額：$" + str(Ryoukin) + "）\n"

    seikyuusyo += "合計金額：$" + str(goukei) + "\n"
    seikyuusyo += "獲得ポイント：" + str(point) + "pt"

    print("\n==================== 出力内容 ====================\n")
    print(seikyuusyo)

    print("\n========== 請求書がテキストファイルとして出力されました。==========\n")
    script_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.dirname(script_dir)
    output_dir = os.path.join(project_root, 'output')
    os.makedirs(output_dir, exist_ok=True)
    
    # テキストファイルに出力
    with open(os.path.join(output_dir, 'invoice.txt'), 'w', encoding='utf-8') as f:
        f.write(seikyuusyo)

if __name__ == "__main__":
    main()