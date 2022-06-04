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
