import pydeck as pdk
import pandas as pd

GPU_GRID_LAYER_DATA = (
    "https://raw.githubusercontent.com/uber-common/"
    "deck.gl-data/master/website/sf-bike-parking.json"
)
df = pd.read_json(GPU_GRID_LAYER_DATA)

# Define a layer to display on a map
layer = pdk.Layer(
    "GPUGridLayer",
    df,
    pickable=True,
    extruded=True,
    cellSize=200,
    elevation_scale=4,
    get_position="COORDINATES",
)

# Set the viewport location
view_state = pdk.ViewState(
    latitude=37.7749295, longitude=-122.4194155, zoom=11, bearing=0, pitch=45
)


# Render
r = pdk.Deck(
    layers=[layer],
    initial_view_state=view_state,
    tooltip={"text": "{position}\nCount: {count}"},
)
r.to_html("gpu_grid_layer.html")
