import googlemaps


def GetLoc(addr):
    gmaps = googlemaps.Client(key='')
    geocode_result = gmaps.geocode(addr)
    lat = geocode_result[0]['geometry']['location']['lat']
    lng = geocode_result[0]['geometry']['location']['lng']
    return lat, lng
