import json
from plotly.graph_objs import Scattergeo, Layout
from plotly import offline
 
#探索數據結構
filename = "eq_data_20210818.json"
with open(filename, encoding='utf-8') as f:
	all_eq_data = json.load(f)

all_eq_dicts = all_eq_data['features']
#擷取震級及位置資料
mags, lons, lats, hover_texts = [], [], [], []
for eq_dict in all_eq_dicts:
	mag = eq_dict['properties']['mag']   #震級
	lon = eq_dict['geometry']['coordinates'][0]   #經度
	lat = eq_dict['geometry']['coordinates'][1]   #緯度
	title = eq_dict['properties']['title']
	mags.append(mag)
	lons.append(lon)
	lats.append(lat)
	hover_texts.append(title)

#繪製地震圖
data = [{
	'type': 'scattergeo',
	'lon': lons,
	'lat': lats,
	'text': hover_texts,
	'marker': {'size': [5*mag for mag in mags],
	'color': mags,   #告知色盤使用的位置
	'colorscale': 'Viridis',   #Virdis色盤是深藍到亮黃
	'reversescale': True,   #黃色代表最低值,深藍代表最高值
	'colorbar': {'title': 'Magnitude'},   #顏色對照嚴重程度
	},
}]
my_layout = Layout(title='2021s年8月全球地震圖')

fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='global_earthquakes.html')