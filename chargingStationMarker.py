import pandas as pd
import returnAddress
import folium as g
from folium.plugins import MarkerCluster

def chargingStationMarker(g_map):
    excel_source = pd.read_excel('C:/Users/cksdn/PycharmProjects/OSS_Project_04/result2.xlsx', usecols=[2]) #new 2
    lat = []
    lng = []
   
