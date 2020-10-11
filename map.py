import folium
import pandas as pd

#Reading the data file
data = pd.read_csv("Volcanoes_USA.txt")

#converting pd column into a list
lat = list(data["LAT"])
lon = list(data["LON"])
name = list(data["NAME"])
elevation = list(data["ELEV"])


map = folium.Map(location=(48.7767982, -121.8109970) , zoom_start = 5, width = "75%" , height = "75%" , min_zoom = 2 )
map.add_child(folium.TileLayer('Stamen Terrain'))
map.add_child(folium.TileLayer('Stamen Toner'))
map.add_child(folium.TileLayer('Stamen Water Color'))
map.add_child(folium.TileLayer('cartodbpositron'))

def color_generator(elevation):
    if elevation<1000:
        return 'green'
    elif 1000<=elevation < 3000:
        return 'orange'
    else:
        return 'red'





#mapping the Markers
Markers_fg = folium.FeatureGroup(name = "My Map")
for lat, lon,name,elevation in zip(lat,lon,name,elevation):
    Markers_fg.add_child(folium.Marker(location = (lat,lon) , popup = name+"\n"+str(+elevation) , icon = folium.Icon(color= color_generator(elevation))))


#Adding the feature group to the map
map.add_child(Markers_fg)
map.add_child(folium.LayerControl())
map.save("Map.html")
