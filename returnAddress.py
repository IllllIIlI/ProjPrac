import googlemaps


def GetLoc(addr):
    gmaps = googlemaps.Client(key='')
    geocode_result = gmaps.geocode(addr)
