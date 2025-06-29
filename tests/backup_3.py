import json
import os
import glob
from src.main import main

def load_json_for_test(testcase_file):
    """指定されたテストケースファイルを読み込む"""
    with open(f"tests/input_for_test/{testcase_file}", "r", encoding="utf-8") as f:
        invoices = json.load(f)
    with open("input/plays.json", "r", encoding="utf-8") as f:
        plays = json.load(f)
    return invoices, plays

def get_lines_text_invoice():
    """出力テキストファイルを行ごとに読み込み"""
    with open("output/invoice.txt", "r", encoding="utf-8") as f:
        result = f.readlines()
    return result

def get_all_text_invoice():
    """出力テキストファイルの内容を文字列として読み込み"""
    with open("output/invoice.txt", "r", encoding="utf-8") as f:
        result = f.read()
    return result

# TestCase No.1
def test_testcase_1(mocker):
    mocker.patch("src.main.load_json", lambda: load_json_for_test("testcase_1.json"))
    main()
    invoice = get_all_text_invoice()
    with open("tests/output_for_test/testcase_1.txt", "r", encoding="utf-8") as f:
        expected = f.read()
    assert invoice == expected

# TestCase No.2
def test_testcase_2(mocker):
    mocker.patch("src.main.load_json", lambda: load_json_for_test("testcase_2.json"))
    main()
    invoice = get_all_text_invoice()
    with open("tests/output_for_test/testcase_2.txt", "r", encoding="utf-8") as f:
        expected = f.read()
    assert invoice == expected

# TestCase No.3
def test_testcase_3(mocker):
    mocker.patch("src.main.load_json", lambda: load_json_for_test("testcase_3.json"))
    main()
    invoice = get_all_text_invoice()
    with open("tests/output_for_test/testcase_3.txt", "r", encoding="utf-8") as f:
        expected = f.read()
    assert invoice == expected

# TestCase No.4
def test_testcase_4(mocker):
    mocker.patch("src.main.load_json", lambda: load_json_for_test("testcase_4.json"))
    main()
    invoice = get_all_text_invoice()
    with open("tests/output_for_test/testcase_4.txt", "r", encoding="utf-8") as f:
        expected = f.read()
    assert invoice == expected

# TestCase No.5
def test_testcase_5(mocker):
    mocker.patch("src.main.load_json", lambda: load_json_for_test("testcase_5.json"))
    main()
    invoice = get_all_text_invoice()
    with open("tests/output_for_test/testcase_5.txt", "r", encoding="utf-8") as f:
        expected = f.read()
    assert invoice == expected

# TestCase No.6
def test_testcase_6(mocker):
    mocker.patch("src.main.load_json", lambda: load_json_for_test("testcase_6.json"))
    main()
    invoice = get_all_text_invoice()
    with open("tests/output_for_test/testcase_6.txt", "r", encoding="utf-8") as f:
        expected = f.read()
    assert invoice == expected

# TestCase No.7
def test_testcase_7(mocker):
    mocker.patch("src.main.load_json", lambda: load_json_for_test("testcase_7.json"))
    main()
    invoice = get_all_text_invoice()
    with open("tests/output_for_test/testcase_7.txt", "r", encoding="utf-8") as f:
        expected = f.read()
    assert invoice == expected

# TestCase No.8
def test_testcase_8(mocker):
    mocker.patch("src.main.load_json", lambda: load_json_for_test("testcase_8.json"))
    main()
    invoice = get_all_text_invoice()
    with open("tests/output_for_test/testcase_8.txt", "r", encoding="utf-8") as f:
        expected = f.read()
    assert invoice == expected

# TestCase No.9
def test_testcase_9(mocker):
    mocker.patch("src.main.load_json", lambda: load_json_for_test("testcase_9.json"))
    main()
    invoice = get_all_text_invoice()
    with open("tests/output_for_test/testcase_9.txt", "r", encoding="utf-8") as f:
        expected = f.read()
    assert invoice == expected

# TestCase No.10
def test_testcase_10(mocker):
    mocker.patch("src.main.load_json", lambda: load_json_for_test("testcase_10.json"))
    main()
    invoice = get_all_text_invoice()
    with open("tests/output_for_test/testcase_10.txt", "r", encoding="utf-8") as f:
        expected = f.read()
    assert invoice == expected

# TestCase No.11
def test_testcase_11(mocker):
    mocker.patch("src.main.load_json", lambda: load_json_for_test("testcase_11.json"))
    main()
    invoice = get_all_text_invoice()
    with open("tests/output_for_test/testcase_11.txt", "r", encoding="utf-8") as f:
        expected = f.read()
    assert invoice == expected

# TestCase No.12
def test_testcase_12(mocker):
    mocker.patch("src.main.load_json", lambda: load_json_for_test("testcase_12.json"))
    main()
    invoice = get_all_text_invoice()
    with open("tests/output_for_test/testcase_12.txt", "r", encoding="utf-8") as f:
        expected = f.read()
    assert invoice == expected

# TestCase No.13
def test_testcase_13(mocker):
    mocker.patch("src.main.load_json", lambda: load_json_for_test("testcase_13.json"))
    main()
    invoice = get_all_text_invoice()
    with open("tests/output_for_test/testcase_13.txt", "r", encoding="utf-8") as f:
        expected = f.read()
    assert invoice == expected

# TestCase No.14
def test_testcase_14(mocker):
    mocker.patch("src.main.load_json", lambda: load_json_for_test("testcase_14.json"))
    main()
    invoice = get_all_text_invoice()
    with open("tests/output_for_test/testcase_14.txt", "r", encoding="utf-8") as f:
        expected = f.read()
    assert invoice == expected

# TestCase No.15
def test_testcase_15(mocker):
    mocker.patch("src.main.load_json", lambda: load_json_for_test("testcase_15.json"))
    main()
    invoice = get_all_text_invoice()
    with open("tests/output_for_test/testcase_15.txt", "r", encoding="utf-8") as f:
        expected = f.read()
    assert invoice == expected

# TestCase No.16
def test_testcase_16(mocker):
    mocker.patch("src.main.load_json", lambda: load_json_for_test("testcase_16.json"))
    main()
    invoice = get_all_text_invoice()
    with open("tests/output_for_test/testcase_16.txt", "r", encoding="utf-8") as f:
        expected = f.read()
    assert invoice == expected

# TestCase No.17
def test_testcase_17(mocker):
    mocker.patch("src.main.load_json", lambda: load_json_for_test("testcase_17.json"))
    main()
    invoice = get_all_text_invoice()
    with open("tests/output_for_test/testcase_17.txt", "r", encoding="utf-8") as f:
        expected = f.read()
    assert invoice == expected

# TestCase No.18
def test_testcase_18(mocker):
    mocker.patch("src.main.load_json", lambda: load_json_for_test("testcase_18.json"))
    main()
    invoice = get_all_text_invoice()
    with open("tests/output_for_test/testcase_18.txt", "r", encoding="utf-8") as f:
        expected = f.read()
    assert invoice == expected

# TestCase No.19
def test_testcase_19(mocker):
    mocker.patch("src.main.load_json", lambda: load_json_for_test("testcase_19.json"))
    main()
    invoice = get_all_text_invoice()
    with open("tests/output_for_test/testcase_19.txt", "r", encoding="utf-8") as f:
        expected = f.read()
    assert invoice == expected

# TestCase No.20
def test_testcase_20(mocker):
    mocker.patch("src.main.load_json", lambda: load_json_for_test("testcase_20.json"))
    main()
    invoice = get_all_text_invoice()
    with open("tests/output_for_test/testcase_20.txt", "r", encoding="utf-8") as f:
        expected = f.read()
    assert invoice == expected

# TestCase No.21
def test_testcase_21(mocker):
    mocker.patch("src.main.load_json", lambda: load_json_for_test("testcase_21.json"))
    main()
    invoice = get_all_text_invoice()
    with open("tests/output_for_test/testcase_21.txt", "r", encoding="utf-8") as f:
        expected = f.read()
    assert invoice == expected

# TestCase No.22
def test_testcase_22(mocker):
    mocker.patch("src.main.load_json", lambda: load_json_for_test("testcase_22.json"))
    main()
    invoice = get_all_text_invoice()
    with open("tests/output_for_test/testcase_22.txt", "r", encoding="utf-8") as f:
        expected = f.read()
    assert invoice == expected

# TestCase No.23
def test_testcase_23(mocker):
    mocker.patch("src.main.load_json", lambda: load_json_for_test("testcase_23.json"))
    main()
    invoice = get_all_text_invoice()
    with open("tests/output_for_test/testcase_23.txt", "r", encoding="utf-8") as f:
        expected = f.read()
    assert invoice == expected

# TestCase No.24
def test_testcase_24(mocker):
    mocker.patch("src.main.load_json", lambda: load_json_for_test("testcase_24.json"))
    main()
    invoice = get_all_text_invoice()
    with open("tests/output_for_test/testcase_24.txt", "r", encoding="utf-8") as f:
        expected = f.read()
    assert invoice == expected

# TestCase No.25
def test_testcase_25(mocker):
    mocker.patch("src.main.load_json", lambda: load_json_for_test("testcase_25.json"))
    main()
    invoice = get_all_text_invoice()
    with open("tests/output_for_test/testcase_25.txt", "r", encoding="utf-8") as f:
        expected = f.read()
    assert invoice == expected

# TestCase No.26
def test_testcase_26(mocker):
    mocker.patch("src.main.load_json", lambda: load_json_for_test("testcase_26.json"))
    main()
    invoice = get_all_text_invoice()
    with open("tests/output_for_test/testcase_26.txt", "r", encoding="utf-8") as f:
        expected = f.read()
    assert invoice == expected

# TestCase No.27
def test_testcase_27(mocker):
    mocker.patch("src.main.load_json", lambda: load_json_for_test("testcase_27.json"))
    main()
    invoice = get_all_text_invoice()
    with open("tests/output_for_test/testcase_27.txt", "r", encoding="utf-8") as f:
        expected = f.read()
    assert invoice == expected

# TestCase No.28
def test_testcase_28(mocker):
    mocker.patch("src.main.load_json", lambda: load_json_for_test("testcase_28.json"))
    main()
    invoice = get_all_text_invoice()
    with open("tests/output_for_test/testcase_28.txt", "r", encoding="utf-8") as f:
        expected = f.read()
    assert invoice == expected

# TestCase No.29
def test_testcase_29(mocker):
    mocker.patch("src.main.load_json", lambda: load_json_for_test("testcase_29.json"))
    main()
    invoice = get_all_text_invoice()
    with open("tests/output_for_test/testcase_29.txt", "r", encoding="utf-8") as f:
        expected = f.read()
    assert invoice == expected

# TestCase No.30
def test_testcase_30(mocker):
    mocker.patch("src.main.load_json", lambda: load_json_for_test("testcase_30.json"))
    main()
    invoice = get_all_text_invoice()
    with open("tests/output_for_test/testcase_30.txt", "r", encoding="utf-8") as f:
        expected = f.read()
    assert invoice == expected

# TestCase No.31
def test_testcase_31(mocker):
    mocker.patch("src.main.load_json", lambda: load_json_for_test("testcase_31.json"))
    main()
    invoice = get_all_text_invoice()
    with open("tests/output_for_test/testcase_31.txt", "r", encoding="utf-8") as f:
        expected = f.read()
    assert invoice == expected

# TestCase No.32
def test_testcase_32(mocker):
    mocker.patch("src.main.load_json", lambda: load_json_for_test("testcase_32.json"))
    main()
    invoice = get_all_text_invoice()
    with open("tests/output_for_test/testcase_32.txt", "r", encoding="utf-8") as f:
        expected = f.read()
    assert invoice == expected

# TestCase No.33
def test_testcase_33(mocker):
    mocker.patch("src.main.load_json", lambda: load_json_for_test("testcase_33.json"))
    main()
    invoice = get_all_text_invoice()
    with open("tests/output_for_test/testcase_33.txt", "r", encoding="utf-8") as f:
        expected = f.read()
    assert invoice == expected

# TestCase No.34
def test_testcase_34(mocker):
    mocker.patch("src.main.load_json", lambda: load_json_for_test("testcase_34.json"))
    main()
    invoice = get_all_text_invoice()
    with open("tests/output_for_test/testcase_34.txt", "r", encoding="utf-8") as f:
        expected = f.read()
    assert invoice == expected

# TestCase No.35
def test_testcase_35(mocker):
    mocker.patch("src.main.load_json", lambda: load_json_for_test("testcase_35.json"))
    main()
    invoice = get_all_text_invoice()
    with open("tests/output_for_test/testcase_35.txt", "r", encoding="utf-8") as f:
        expected = f.read()
    assert invoice == expected

# TestCase No.36
def test_testcase_36(mocker):
    mocker.patch("src.main.load_json", lambda: load_json_for_test("testcase_36.json"))
    main()
    invoice = get_all_text_invoice()
    with open("tests/output_for_test/testcase_36.txt", "r", encoding="utf-8") as f:
        expected = f.read()
    assert invoice == expected

# TestCase No.37
def test_testcase_37(mocker):
    mocker.patch("src.main.load_json", lambda: load_json_for_test("testcase_37.json"))
    main()
    invoice = get_all_text_invoice()
    with open("tests/output_for_test/testcase_37.txt", "r", encoding="utf-8") as f:
        expected = f.read()
    assert invoice == expected

# TestCase No.38
def test_testcase_38(mocker):
    mocker.patch("src.main.load_json", lambda: load_json_for_test("testcase_38.json"))
    main()
    invoice = get_all_text_invoice()
    with open("tests/output_for_test/testcase_38.txt", "r", encoding="utf-8") as f:
        expected = f.read()
    assert invoice == expected

# TestCase No.39
def test_testcase_39(mocker):
    mocker.patch("src.main.load_json", lambda: load_json_for_test("testcase_39.json"))
    main()
    invoice = get_all_text_invoice()
    with open("tests/output_for_test/testcase_39.txt", "r", encoding="utf-8") as f:
        expected = f.read()
    assert invoice == expected
