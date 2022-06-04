import chargingMethod
import pandas as pd
import findCurLoc
import chargerGuide

chargingMethod.guide()
excel_source = pd.read_excel('C:/Users/cksdn/PycharmProjects/OSS_Project_04/전기차-충전소-설치현황_20220316.xlsx', usecols=[1, 2, 3, 4, 5])
print("Please enter the area where you want to find the location of the charging station. ex)청주")
str_want_go = input()
int_line = excel_source['주소'].str.contains(str_want_go)
want_go_excel = excel_source[int_line]
want_go_excel.to_excel('C:/Users/cksdn/PycharmProjects/OSS_Project_04/result.xlsx', sheet_name= 'Result')

cur_lat, cur_lng = findCurLoc.find()

excel_source = pd.read_excel('C:/Users/cksdn/PycharmProjects/OSS_Project_04/result.xlsx', usecols=[1, 2, 3, 4, 5])
print("Please enter the type of car you want.\n"
      "SM3 Z.E, 레이EV, 소울EV, 닛산리프, 아이오닉EV, BMW i3, 스파크EV, 볼트EV
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
want_go_excel.to_excel('C:/Users/cksdn/PycharmProjects/OSS_Project_04/result1.xlsx', sheet_name= 'Result')
      
excel_source = pd.read_excel('C:/Users/cksdn/PycharmProjects/OSS_Project_04/result1.xlsx', usecols=[1, 2, 3, 4, 5])

chargerGuide.guide()
