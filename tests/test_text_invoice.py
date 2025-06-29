import json
from src.main import main

"""悲劇の観客数が「悲劇金額変化観客数」を超過した場合、該当演目の金額の算定方法が変わる。"""
"""喜劇の観客数が「喜劇金額変化観客数」を超過した場合、該当演目の金額の算定方法が変わる。"""
"""観客数が「共通ポイント付与観客数」を超過した場合、各演目ごとにポイントが付与される。"""
"""喜劇の場合、観客数が「喜劇ポイント付与観客倍数」ごとにポイントが付与される。"""

def load_json_for_test(testcase_file):
    """指定されたテストケースファイルを読み込む"""
    with open(f"tests/input_for_test/{testcase_file}", "r", encoding="utf-8") as f:
        invoices = json.load(f)
    with open("input/plays.json", "r", encoding="utf-8") as f:
        plays = json.load(f)
    return invoices, plays

def get_output_invoice():
    """出力テキストファイルの内容を文字列として読み込み"""
    with open("output/invoice.txt", "r", encoding="utf-8") as f:
        result = f.read()
    return result

# TestCase No.1
def test_testcase_1(mocker):
    """悲劇の観客数が「悲劇金額変化観客数」未満であるとき、金額は基本料金のみである。"""
    mocker.patch("src.main.load_json", lambda: load_json_for_test("testcase_1.json"))
    main()
    invoice = get_output_invoice()
    with open("tests/output_for_test/testcase_1.txt", "r", encoding="utf-8") as f:
        expected = f.read()
    assert invoice == expected

# TestCase No.2
def test_testcase_2(mocker):
    """悲劇の観客数が「悲劇金額変化観客数」であるとき、金額は基本料金のままである。"""
    mocker.patch("src.main.load_json", lambda: load_json_for_test("testcase_2.json"))
    main()
    invoice = get_output_invoice()
    with open("tests/output_for_test/testcase_2.txt", "r", encoding="utf-8") as f:
        expected = f.read()
    assert invoice == expected

# TestCase No.3
def test_testcase_3(mocker):
    """悲劇の観客数が「悲劇金額変化観客数」を超過しているとき、金額は基本料金より大きい。"""
    mocker.patch("src.main.load_json", lambda: load_json_for_test("testcase_3.json"))
    main()
    invoice = get_output_invoice()
    with open("tests/output_for_test/testcase_3.txt", "r", encoding="utf-8") as f:
        expected = f.read()
    assert invoice == expected

# TestCase No.4
def test_testcase_4(mocker):
    """喜劇の観客数が「喜劇ポイント付与観客倍数」未満であるとき、ポイントは付与されない。"""
    mocker.patch("src.main.load_json", lambda: load_json_for_test("testcase_4.json"))
    main()
    invoice = get_output_invoice()
    with open("tests/output_for_test/testcase_4.txt", "r", encoding="utf-8") as f:
        expected = f.read()
    assert invoice == expected

# TestCase No.5
def test_testcase_5(mocker):
    """喜劇の観客数が「喜劇ポイント付与観客倍数」であるとき、初めてポイントが付与される。"""
    mocker.patch("src.main.load_json", lambda: load_json_for_test("testcase_5.json"))
    main()
    invoice = get_output_invoice()
    with open("tests/output_for_test/testcase_5.txt", "r", encoding="utf-8") as f:
        expected = f.read()
    assert invoice == expected

# TestCase No.6
def test_testcase_6(mocker):
    """喜劇の観客数が「喜劇ポイント付与観客倍数」以上かつ次の「喜劇ポイント付与観客倍数」未満であるとき、初めの獲得ポイントのままである。"""
    mocker.patch("src.main.load_json", lambda: load_json_for_test("testcase_6.json"))
    main()
    invoice = get_output_invoice()
    with open("tests/output_for_test/testcase_6.txt", "r", encoding="utf-8") as f:
        expected = f.read()
    assert invoice == expected

# TestCase No.7
def test_testcase_7(mocker):
    """喜劇の観客数が「喜劇金額変化観客数」未満であるとき、金額は基本料金と一人当たり$300の合算のみである。"""
    mocker.patch("src.main.load_json", lambda: load_json_for_test("testcase_7.json"))
    main()
    invoice = get_output_invoice()
    with open("tests/output_for_test/testcase_7.txt", "r", encoding="utf-8") as f:
        expected = f.read()
    assert invoice == expected

# TestCase No.8
def test_testcase_8(mocker):
    """喜劇の観客数が「喜劇金額変化観客数」であるとき、金額は基本料金と一人当たり$300の合算のままである。"""
    mocker.patch("src.main.load_json", lambda: load_json_for_test("testcase_8.json"))
    main()
    invoice = get_output_invoice()
    with open("tests/output_for_test/testcase_8.txt", "r", encoding="utf-8") as f:
        expected = f.read()
    assert invoice == expected

# TestCase No.9
def test_testcase_9(mocker):
    """喜劇の観客数が「喜劇金額変化観客数」を超過している場合、金額は基本料金と一人当たり$300の合算より大きくなる。"""
    mocker.patch("src.main.load_json", lambda: load_json_for_test("testcase_9.json"))
    main()
    invoice = get_output_invoice()
    with open("tests/output_for_test/testcase_9.txt", "r", encoding="utf-8") as f:
        expected = f.read()
    assert invoice == expected

# TestCase No.10
def test_testcase_10(mocker):
    """喜劇の観客数が「喜劇ポイント付与観客倍数」以上かつ「ポイント付与観客数」未満である場合、「喜劇ポイント付与観客倍数」分のポイントを獲得する。"""
    mocker.patch("src.main.load_json", lambda: load_json_for_test("testcase_10.json"))
    main()
    invoice = get_output_invoice()
    with open("tests/output_for_test/testcase_10.txt", "r", encoding="utf-8") as f:
        expected = f.read()
    assert invoice == expected

# TestCase No.11
def test_testcase_11(mocker):
    mocker.patch("src.main.load_json", lambda: load_json_for_test("testcase_11.json"))
    main()
    invoice = get_output_invoice()
    with open("tests/output_for_test/testcase_11.txt", "r", encoding="utf-8") as f:
        expected = f.read()
    assert invoice == expected

# TestCase No.12
def test_testcase_12(mocker):
    mocker.patch("src.main.load_json", lambda: load_json_for_test("testcase_12.json"))
    main()
    invoice = get_output_invoice()
    with open("tests/output_for_test/testcase_12.txt", "r", encoding="utf-8") as f:
        expected = f.read()
    assert invoice == expected

# TestCase No.13
def test_testcase_13(mocker):
    mocker.patch("src.main.load_json", lambda: load_json_for_test("testcase_13.json"))
    main()
    invoice = get_output_invoice()
    with open("tests/output_for_test/testcase_13.txt", "r", encoding="utf-8") as f:
        expected = f.read()
    assert invoice == expected

# TestCase No.14
def test_testcase_14(mocker):
    mocker.patch("src.main.load_json", lambda: load_json_for_test("testcase_14.json"))
    main()
    invoice = get_output_invoice()
    with open("tests/output_for_test/testcase_14.txt", "r", encoding="utf-8") as f:
        expected = f.read()
    assert invoice == expected

# TestCase No.15
def test_testcase_15(mocker):
    mocker.patch("src.main.load_json", lambda: load_json_for_test("testcase_15.json"))
    main()
    invoice = get_output_invoice()
    with open("tests/output_for_test/testcase_15.txt", "r", encoding="utf-8") as f:
        expected = f.read()
    assert invoice == expected

# TestCase No.16
def test_testcase_16(mocker):
    mocker.patch("src.main.load_json", lambda: load_json_for_test("testcase_16.json"))
    main()
    invoice = get_output_invoice()
    with open("tests/output_for_test/testcase_16.txt", "r", encoding="utf-8") as f:
        expected = f.read()
    assert invoice == expected

# TestCase No.17
def test_testcase_17(mocker):
    mocker.patch("src.main.load_json", lambda: load_json_for_test("testcase_17.json"))
    main()
    invoice = get_output_invoice()
    with open("tests/output_for_test/testcase_17.txt", "r", encoding="utf-8") as f:
        expected = f.read()
    assert invoice == expected

