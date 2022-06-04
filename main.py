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
