import googlemaps

def getloc(addr):
    gmaps = googlemaps.Client(key='Please Enter Your Googlemaps Key.')
    geocode_result = gmaps.geocode(addr)
