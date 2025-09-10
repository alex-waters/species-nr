import folium
import json

m = folium.Map(
    location=[53.52671888897747, -2.093758895421331],
    zoom_start=15,
    #tiles="cartodbpositron"
)

with open('../static/nr-polygon.json', 'r') as file:
    nr_poly_json = json.load(file)

for i in nr_poly_json['features'][0]['geometry']['coordinates'][0]:
    i.reverse()

folium.Polygon(
    locations=nr_poly_json['features'][0]['geometry']['coordinates'][0],
    popup="Northern Roots",
    color='#00453B',
    weight=8
).add_to(m)

# Add pond
with open('../static/pond-polygon.json', 'r') as file:
    pond_poly_json = json.load(file)

for i in pond_poly_json['features'][0]['geometry']['coordinates'][0]:
    i.reverse()

pond_label = """
    <h1> Pond 1 </h1><br>
    <h2>This is where our pond species survey was done on:</h2>
    <p>
    <code>
        1st January 2025
    </code>
    </p>
"""

folium.Polygon(
    locations=pond_poly_json['features'][0]['geometry']['coordinates'][0],
    tooltip=pond_label,
    color='#blue',
    weight=4
).add_to(m)

folium.CircleMarker(
    location=[53.52671888897747, -2.093758895421331],
    radius=20,
    color="cornflowerblue",
    stroke=False,
    fill=True,
    fill_opacity=0.8,
    opacity=1,
    tooltip=pond_label,
).add_to(m)

folium.LayerControl().add_to(m)

m.save('../static/vis_map.html')
