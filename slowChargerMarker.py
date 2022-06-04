import pandas as pd
import returnAddress
import folium as g
from folium.plugins import MarkerCluster


def slowChargerMarker(map):
    excel_source = pd.read_excel('ProjPrac/result_charger.xlsx', usecols=[2])
    lat = []
    lng = []
