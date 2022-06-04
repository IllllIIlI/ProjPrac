import googlemaps

def getloc(addr):
    gmaps = googlemaps.Client(key='구글키를 입력해주세요')
    geocode_result = gmaps.geocode(addr)
