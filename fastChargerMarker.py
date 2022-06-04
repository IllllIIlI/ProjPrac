import pandas as pd
import returnAddress
import folium as g
from folium.plugins import MarkerCluster

def fastChargerMarker(g_map):
    excel_source = pd.read_excel('result2.xlsx', usecols=[2])
    lat = []
    lng = []
    k = excel_source.shape[0]
    for cnt in range(k):
        chg_lat, chg_lng = returnAddress.getloc(str(excel_source.loc[cnt]))
        lat.append(chg_lat)
        lng.append(chg_lng)
