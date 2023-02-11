import plotly.graph_objects as go
from floodsystem import stationdata

stations = stationdata.build_station_list()

fig = go.Figure(data=go.Scattergeo(
    lat=list(map(lambda s: s.coord[0], stations)),
    lon=list(map(lambda s: s.coord[1], stations)),
    text=list(map(lambda s: s.name, stations)),
    mode="markers",
    marker_color="light blue",
))

fig.update_geos(
    lonaxis_range=[-11, 2],
    lataxis_range=[49, 60],
)

fig.update_layout(title="Monitoring stations in the UK", geo_scope="europe")
fig.show()
