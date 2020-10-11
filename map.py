import folium
map = folium.Map(location=(45.540470, -73.668482) , zoom_start = 5, width = "75%" , height = "75%" , min_zoom = 2 )
map.add_child(folium.TileLayer('Stamen Terrain'))
map.add_child(folium.TileLayer('Stamen Toner'))
map.add_child(folium.TileLayer('Stamen Water Color'))
map.add_child(folium.TileLayer('cartodbpositron'))





map.add_child(folium.LayerControl())
map.save("Map.html")
