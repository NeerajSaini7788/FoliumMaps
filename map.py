import folium
import pandas as pd

#Reading the data file
data = pd.read_csv("Volcanoes_USA.txt")

#converting pd column into a list
lat = list(data["LAT"])
lon = list(data["LON"])
name = list(data["NAME"])


map = folium.Map(location=(45.540470, -73.668482) , zoom_start = 5, width = "75%" , height = "75%" , min_zoom = 2 )
map.add_child(folium.TileLayer('Stamen Terrain'))
map.add_child(folium.TileLayer('Stamen Toner'))
map.add_child(folium.TileLayer('Stamen Water Color'))
map.add_child(folium.TileLayer('cartodbpositron'))



#mapping the Markers
Markers_fg = folium.FeatureGroup(name = "My Map")
for lat, lon,name in zip(lat,lon,name):
    Markers_fg.add_child(folium.Marker(location = (lat,lon) , popup = name , icon = folium.Icon(color="green")))


#Adding the feature group to the map
map.add_child(Markers_fg)


map.add_child(folium.LayerControl())
map.save("Map.html")
