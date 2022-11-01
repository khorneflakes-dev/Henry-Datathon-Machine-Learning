from geopy.geocoders import Nominatim

demo = 'POINT (-73.106 7.064)'

def geopy_func(value):
    value = value.replace('POINT (','')
    value = value.replace(')','')
    return value

def geolocalizar(value):
	new_value = value.replace('POINT (','')
	new_value = new_value.replace(')','')
	
	lat = new_value.split(' ')[1]
	lon = new_value.split(' ')[0]
	geoLoc = Nominatim(user_agent="myGeocoder") 
	locname = geoLoc.reverse((lat, lon))
	return locname.raw['address']['state_district']

print(geolocalizar(demo))