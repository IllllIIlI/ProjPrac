import chargerGuide
import chargingMethod
import pandas as pd

cur_lat = 0.0
cur_lng = 0.0
dst_lat = 0.0
dst_lng = 0.0

chargingMethod.guide()

excel_source = pd.read_excel(
    'ProjPrac/전기차-충전소-설치현황_20220316.xlsx', usecols=[1, 2, 3, 4, 5])
print()
