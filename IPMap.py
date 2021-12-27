import geocoder
import folium

g = geocoder.ip("me")

myAddress = g.latlng

my_map1 = folium.Map(location=myAddress, zoom_start=12)

folium.CircleMarker(location=myAddress, radius=150, popup="Mumbai").add_to(my_map1)

folium.Marker(myAddress, popup="Mumbai").add_to(my_map1)

my_map1.save('my_map.html')

print(myAddress)

