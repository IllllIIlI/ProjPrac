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
