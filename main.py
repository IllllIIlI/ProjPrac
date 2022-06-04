import pandas as pd
import folium as g
import chargingMethod
import findCurLoc
import findDestination
import chargerGuide
import findTheDistanceBetweenCoordinates as Dis
import chargingStationMarker
import fastChargerMarker
import slowChargerMarker

cur_lat = 0.0
cur_lng = 0.0
dst_lat = 0.0
dst_lng = 0.0

chargingMethod.guide()

excel_source = pd.read_excel('전기차-충전소-설치현황_20220316.xlsx', usecols=[1, 2, 3, 4, 5])
print("충전소 위치를 찾고 싶은 도시를 입력하세요.")
str_want_go = input()
int_line = excel_source['주소'].str.contains(str_want_go)
want_go_excel = excel_source[int_line]
want_go_excel.to_excel('result.xlsx', sheet_name= 'Result')

excel_source = pd.read_excel('result.xlsx', usecols=[1, 2, 3, 4, 5])
print("원하는 차종을 입력하세요.\n"
      "SM3 Z.E, 레이EV, 소울EV, 닛산리프, 아이오닉EV, BMW i3, 스파크EV, 볼트EV, 테슬라")

car = input()
if car == "SM3 Z.E":
    str_want_go = "SM3 Z.E"
    int_line = excel_source['지원차종'].str.contains(str_want_go)
elif car == "레이EV":
    str_want_go = "레이EV"
    int_line = excel_source['지원차종'].str.contains(str_want_go)
elif car == "소울EV":
    str_want_go = "소울EV"
    int_line = excel_source['지원차종'].str.contains(str_want_go)
elif car == "닛산리프":
    str_want_go = "닛산리프"
    int_line = excel_source['지원차종'].str.contains(str_want_go)
elif car == "아이오닉EV":
    str_want_go = "아이오닉EV"
    int_line = excel_source['지원차종'].str.contains(str_want_go)
elif car == "BMW i3":
    str_want_go = "BMW i3"
    int_line = excel_source['지원차종'].str.contains(str_want_go)
elif car == "스파크EV":
    str_want_go = "스파크EV"
    int_line = excel_source['지원차종'].str.contains(str_want_go)
elif car == "볼트EV":
    str_want_go = "볼트EV"
    int_line = excel_source['지원차종'].str.contains(str_want_go)
elif car == "테슬라":
    str_want_go = "테슬라"
    int_line = excel_source['지원차종'].str.contains(str_want_go)

want_go_excel = excel_source[int_line]
want_go_excel.to_excel('result1.xlsx', sheet_name= 'Result')

excel_source = pd.read_excel('result1.xlsx', usecols=[1, 2, 3, 4, 5])

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
    want_go_excel.to_excel('result2_1.xlsx', sheet_name='Result')
    want_go_excel = excel_source[int_line2]
    want_go_excel.to_excel('result2_2.xlsx', sheet_name='Result')
    want_go_excel = excel_source[int_line3]
    want_go_excel.to_excel('result2_3.xlsx', sheet_name='Result')
    want_go_excel = excel_source[int_line4]
    want_go_excel.to_excel('result2_4.xlsx', sheet_name='Result')
    want_go_excel = excel_source[int_line5]
    want_go_excel.to_excel('result2_5.xlsx', sheet_name='Result')
    want_go_excel = excel_source[int_line6]
    want_go_excel.to_excel('result2_6.xlsx', sheet_name='Result')
    want_go_excel = excel_source[int_line7]
    want_go_excel.to_excel('result2_7.xlsx', sheet_name='Result')
    want_go_excel = excel_source[int_line8]
    want_go_excel.to_excel('result2_8.xlsx', sheet_name='Result')
    want_go_excel = excel_source[int_line9]
    want_go_excel.to_excel('result2_9.xlsx', sheet_name='Result')
    excel_names = ['result2_1.xlsx', 'result2_2.xlsx', 'result2_3.xlsx', 'result2_4.xlsx',
                   'result2_5.xlsx', 'result2_6.xlsx', 'result2_7.xlsx', 'result2_8.xlsx',
                   'result2_9.xlsx']
    excels = [pd.ExcelFile(name) for name in excel_names]
    frames = [x.parse(x.sheet_names[0], header=None, index_col=None) for x in excels]
    frames[1:] = [df[1:] for df in frames[1:]]
    combined = pd.concat(frames)
    combined.to_excel("result2.xlsx", header=False, index=False)

elif charger == "Slow":
    int_line1 = excel_source['완속충전기(대)'].astype(str).str.contains("1")
    int_line2 = excel_source['완속충전기(대)'].astype(str).str.contains("2")
    int_line3 = excel_source['완속충전기(대)'].astype(str).str.contains("3")
    int_line4 = excel_source['완속충전기(대)'].astype(str).str.contains("4")
    int_line5 = excel_source['완속충전기(대)'].astype(str).str.contains("5")
    int_line6 = excel_source['완속충전기(대)'].astype(str).str.contains("6")
    int_line7 = excel_source['완속충전기(대)'].astype(str).str.contains("7")
    int_line8 = excel_source['완속충전기(대)'].astype(str).str.contains("8")
