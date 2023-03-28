import folium
import geocoder



g = geocoder.ip("me")

address = g.latlng

map1 = folium.Map(location = address,
                  zoom_start=12)
folium.CircleMarker(location=address,
                    radius=50, popup="mumbai").add_to(map1)
folium.Marker(address,
              popup="mumbai").add_to(map1)

map1.save("map.html ")