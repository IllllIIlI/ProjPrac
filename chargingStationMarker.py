import pandas as pd
import returnAddress
import folium as g
from folium.plugins import MarkerCluster

def chargingStationMarker(g_map):
    excel_source = pd.read_excel('result2.xlsx', usecols=[2])
    lat = []
    lng = []
    
    k = excel_source.shape[0]
    
    for cnt in range(k):
        chg_lat, chg_lng = returnAddress.getloc(str(excel_source.loc[cnt]))
        lat.append(chg_lat)
        lng.append(chg_lng)
    locations = list(zip(lat, lng))
    icons = [g.Icon(icon='glyphicon glyphicon-flash',
                    popup='Charging Station',
                    prefix="glyphicon",
                    color='gray',
                    icon_color='#FFFF00') for _ in range(len(locations))]

    cluster = MarkerCluster(locations = locations, icons = icons)
    cluster.add_to(g_map)