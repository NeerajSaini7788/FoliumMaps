import folium
import pandas as pd

#Reading the data file
data = pd.read_csv("Volcanoes_USA.txt")

#converting pd column into a list
lat = list(data["LAT"])
lon = list(data["LON"])
name = list(data["NAME"])
elevation = list(data["ELEV"])

#intitalizing Map
map = folium.Map(location=(48.7767982, -121.8109970) , zoom_start = 5, width = "75%" , height = "75%" , min_zoom = 2 )
map.add_child(folium.TileLayer('Stamen Terrain'))
map.add_child(folium.TileLayer('Stamen Toner'))
map.add_child(folium.TileLayer('Stamen Water Color'))
map.add_child(folium.TileLayer('cartodbpositron'))


#Color generator based on elevation
def color_generator(elevation):
    if elevation<1000:
        return 'green'
    elif 1000<=elevation < 3000:
        return 'orange'
    else:
        return 'red'


#mapping the Markers
Markers_fg = folium.FeatureGroup(name = "Volcanoes")
for lat, lon,name,elevation in zip(lat,lon,name,elevation):
    #Markers_fg.add_child(folium.Marker(location = (lat,lon) , popup = name+"\n"+str(+elevation) , icon = folium.Icon(color= color_generator(elevation))))
    Markers_fg.add_child(folium.CircleMarker(location = (lat,lon) , radius = 7, popup = name+"\n"+str(+elevation) , fill_color = color_generator(elevation) ,fill_opacity = 0.7))



boundry_fg = folium.FeatureGroup(name = "Boundary")
boundry_fg.add_child(folium.GeoJson(data = open('world.json' , 'r' , encoding = 'utf-8-sig').read() , style_function =lambda x :{ 'fillColor' : 'green' if x['properties']['POP2005'] < 10000000
else 'orange' if 10000000 <= x ['properties']['POP2005']<20000000 else 'red'}))







#Adding the feature group to the map
map.add_child(boundry_fg)
map.add_child(Markers_fg)
map.add_child(folium.LayerControl())
map.save("Map.html")
