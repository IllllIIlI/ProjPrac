import chargerGuide
import chargingMethod
import findCurLoc
import pandas as pd

cur_lat = 0.0
cur_lng = 0.0
dst_lat = 0.0
dst_lng = 0.0

chargingMethod.guide()

excel_source = pd.read_excel(
    'ProjPrac/전기차-충전소-설치현황_20220316.xlsx', usecols=[1, 2, 3, 4, 5])
print("Please enter the area where you want to find the location of the charging station. ex)청주")
str_want_go = input()
int_line = excel_source['주소'].str.contains(str_want_go)
want_go_excel = excel_source[int_line]
want_go_excel.to_excel(
    'ProjPrac/result.xlsx', sheet_name='Result')

cur_lat, cur_lng = findCurLoc.Find()
excel_source = pd.read_excel(
    'ProjPrac/result.xlsx', usecols=[1, 2, 3, 4, 5])
print("Please enter the type of car you want.\n"
      "SM3 Z.E, 레이EV, 소울EV, 닛산리프, 아이오닉EV, BMW i3, 스파크EV, 볼트EV, 테슬라")

car = input()
line = excel_source['지원차종'].str.contains(car)

want_go_excel = excel_source[line]
want_go_excel.to_excel(
    'ProjPrac/result1.xlsx', sheet_name='Result')

excel_source = pd.read_excel(
    'ProjPrac/result1.xlsx', usecols=[1, 2, 3, 4, 5])
chargerGuide.guide()
print("Pick a charger that you want between a fast charger and a slow charger\n"
      "Fast, Slow, No Problem")
charger = input()
if charger == "Fast":
    int_line1 = excel_source['급속충전기(대)'].astype(str).str.contains("1")
    int_line2 = excel_source['급속충전기(대)'].astype(str).str.contains("2")
    int_line3 = excel_source['급속충전기(대)'].astype(str).str.contains("3")
    int_line4 = excel_source['급속충전기(대)'].astype(str).str.contains("4")
    int_line5 = excel_source['급속충전기(대)'].astype(str).str.contains("5")
    int_line6 = excel_source['급속충전기(대)'].astype(str).str.contains("6")
    int_line7 = excel_source['급속충전기(대)'].astype(str).str.contains("7")
    int_line8 = excel_source['급속충전기(대)'].astype(str).str.contains("8")
    int_line9 = excel_source['급속충전기(대)'].astype(str).str.contains("9")
    want_go_excel = excel_source[int_line1]
    want_go_excel.to_excel(
        'ProjPrac/result_charger_1.xlsx', sheet_name='Fast_Charger')
    want_go_excel = excel_source[int_line2]
    want_go_excel.to_excel(
        'ProjPrac/result_charger_2.xlsx', sheet_name='Fast_Charger')
    want_go_excel = excel_source[int_line3]
    want_go_excel.to_excel(
        'ProjPrac/result_charger_3.xlsx', sheet_name='Fast_Charger')
    want_go_excel = excel_source[int_line4]
    want_go_excel.to_excel(
        'ProjPrac/result_charger_4.xlsx', sheet_name='Fast_Charger')
    want_go_excel = excel_source[int_line5]
    want_go_excel.to_excel(
        'ProjPrac/result_charger_5.xlsx', sheet_name='Fast_Charger')
    want_go_excel = excel_source[int_line6]
    want_go_excel.to_excel(
        'ProjPrac/result_charger_6.xlsx', sheet_name='Fast_Charger')
    want_go_excel = excel_source[int_line7]
    want_go_excel.to_excel(
        'ProjPrac/result_charger_7.xlsx', sheet_name='Fast_Charger')
    want_go_excel = excel_source[int_line8]
    want_go_excel.to_excel(
        'ProjPrac/result_charger_8.xlsx', sheet_name='Fast_Charger')
    want_go_excel = excel_source[int_line9]
    want_go_excel.to_excel(
        'ProjPrac/result_charger_9.xlsx', sheet_name='Fast_Charger')
    excel_names = ['ProjPrac/result_charger_1.xlsx', 'ProjPrac/result_charger_2.xlsx', 'ProjPrac/result_charger_3.xlsx', 'ProjPrac/result_charger_4.xlsx',
                   'ProjPrac/result_charger_5.xlsx', 'ProjPrac/result_charger_6.xlsx', 'ProjPrac/result_charger_7.xlsx', 'ProjPrac/result_charger_8.xlsx',
                   'ProjPrac/result_charger_9.xlsx']
    excels = [pd.ExcelFile(name) for name in excel_names]
    frames = [x.parse(x.sheet_names[0], header=None, index_col=None)
              for x in excels]
    frames[1:] = [df[1:] for df in frames[1:]]
    combined = pd.concat(frames)
    combined.to_excel(
        "ProjPrac/result_charger.xlsx", header=False, index=False)

elif charger == "Slow":
    int_line1 = excel_source['완속충전기(대)'].astype(str).str.contains("1")
    int_line2 = excel_source['완속충전기(대)'].astype(str).str.contains("2")
    int_line3 = excel_source['완속충전기(대)'].astype(str).str.contains("3")
    int_line4 = excel_source['완속충전기(대)'].astype(str).str.contains("4")
    int_line5 = excel_source['완속충전기(대)'].astype(str).str.contains("5")
    int_line6 = excel_source['완속충전기(대)'].astype(str).str.contains("6")
    int_line7 = excel_source['완속충전기(대)'].astype(str).str.contains("7")
    int_line8 = excel_source['완속충전기(대)'].astype(str).str.contains("8")
    int_line9 = excel_source['완속충전기(대)'].astype(str).str.contains("9")
    want_go_excel = excel_source[int_line1]
    want_go_excel.to_excel(
        'ProjPrac/result_charger_1.xlsx', sheet_name='Normal_Charger')
    want_go_excel = excel_source[int_line2]
    want_go_excel.to_excel(
        'ProjPrac/result_charger_2.xlsx', sheet_name='Normal_Charger')
    want_go_excel = excel_source[int_line3]
    want_go_excel.to_excel(
        'ProjPrac/result_charger_3.xlsx', sheet_name='Normal_Charger')
    want_go_excel = excel_source[int_line4]
    want_go_excel.to_excel(
        'ProjPrac/result_charger_4.xlsx', sheet_name='Normal_Charger')
    want_go_excel = excel_source[int_line5]
    want_go_excel.to_excel(
        'ProjPrac/result_charger_5.xlsx', sheet_name='Normal_Charger')
    want_go_excel = excel_source[int_line6]
    want_go_excel.to_excel(
        'ProjPrac/result_charger_6.xlsx', sheet_name='Normal_Charger')
    want_go_excel = excel_source[int_line7]
    want_go_excel.to_excel(
        'ProjPrac/result_charger_7.xlsx', sheet_name='Normal_Charger')
    want_go_excel = excel_source[int_line8]
    want_go_excel.to_excel(
        'ProjPrac/result_charger_8.xlsx', sheet_name='Normal_Charger')
    want_go_excel = excel_source[int_line9]
    want_go_excel.to_excel(
        'ProjPrac/result_charger_9.xlsx', sheet_name='Result')
    excel_names = ['ProjPrac/result_charger_1.xlsx', 'ProjPrac/result_charger_2.xlsx', 'ProjPrac/result_charger_3.xlsx', 'ProjPrac/result_charger_4.xlsx',
                   'ProjPrac/result_charger_5.xlsx', 'ProjPrac/result_charger_6.xlsx', 'ProjPrac/result_charger_7.xlsx', 'ProjPrac/result_charger_8.xlsx',
                   'ProjPrac/result_charger_9.xlsx']
