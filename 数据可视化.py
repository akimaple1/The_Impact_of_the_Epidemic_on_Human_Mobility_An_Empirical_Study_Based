import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.colors import LinearSegmentedColormap
from matplotlib import rcParams
import matplotlib.font_manager as fm
from mpl_toolkits.axes_grid1.anchored_artists import AnchoredSizeBar
import geopy.distance  # 用于计算经纬度距离

# 解决中文显示问题，选择一个系统中存在的中文字体
# 替换为你系统中的中文字体，例如 'SimHei' 或 'MS Gothic' 等
rcParams['font.sans-serif'] = ['SimHei']  # 设置字体为黑体，确保支持中文
rcParams['axes.unicode_minus'] = False    # 解决负号显示问题

# 读取表格数据，假设数据保存在 'data.csv' 中，包含 'longitude', 'latitude' 和 'total_flow' 三列
data = pd.read_csv('az_danyuan_19.csv')

# 提取经纬度和 total_flow 数据
longitude = data['centroid_x'].values
latitude = data['centroid_y'].values
total_flow = data['total_flow'].values

# 计算经纬度范围，确定图像覆盖的区域
min_lon, max_lon = longitude.min(), longitude.max()
min_lat, max_lat = latitude.min(), latitude.max()

# 使用 geopy 计算两个经纬度点之间的距离，单位为 km
point_1 = (min_lat, min_lon)
point_2 = (min_lat, max_lon)
distance_km = geopy.distance.distance(point_1, point_2).km

# 确定适合的比例尺长度，取总距离的 1/10
scalebar_length_km = distance_km / 10


# 定义自定义的颜色映射，并减弱亮度
colors = ['#4B0082', '#000080', '#008000', '#FFFF00', '#FFA500', '#FF4500']  # 深蓝, 蓝, 绿, 黄, 橙, 红
cmap = LinearSegmentedColormap.from_list("custom_cmap", colors)

# 对 total_flow 进行标准化
total_flow_normalized = np.log1p(total_flow)

# 创建图形，设置大小
fig, ax = plt.subplots(figsize=(12, 12))
# fig.patch.set_facecolor('black')  # 整个图的背景颜色
# ax.set_facecolor('black')

# 移除边框
for spine in ax.spines.values():
    spine.set_visible(False)

# 移除刻度线和刻度标签
ax.set_xticks([])
ax.set_yticks([])

# 使用 Plasma 配色方案
scatter = ax.scatter(longitude, latitude,
                     c=total_flow_normalized,   # 使用标准化后的 total_flow 作为颜色深浅
                     cmap=cmap,             # 使用类似图片的 "Plasma" 配色
                     s=5,                      # 调整点的大小
                     marker='s',                # 使用正方形作为点的形状
                     alpha=0.8)                 # 调整透明度

# 添加颜色条和标签
#cbar = plt.colorbar(scatter, label='总流量（对数尺度）', shrink=0.8, aspect=30)
#cbar.ax.set_yticklabels([int(np.exp(y) - 1) for y in cbar.get_ticks()])  # 转换为原始 total_flow 值

# 添加网格以便更好地对比点的位置
#ax.grid(True, linestyle='--', alpha=0.3)

# 增加标题和坐标轴标签的字体大小
# ax.set_xlabel('经度', fontsize=14)
# ax.set_ylabel('纬度', fontsize=14)
# ax.set_title('基于总流量（对数尺度）的热力图（Plasma配色）', fontsize=16)

# 调整颜色条字体大小
#cbar.ax.tick_params(labelsize=12)

# 增加坐标轴的刻度字体大小
# plt.xticks(fontsize=12)
# plt.yticks(fontsize=12)

# 添加比例尺，设置在左下角
scalebar = AnchoredSizeBar(ax.transData,
                           scalebar_length_km / distance_km,  # 动态计算比例尺长度
                           f'{int(scalebar_length_km)} km',    # 动态计算比例尺标签
                           'lower left',                      # 设置比例尺的位置
                           pad=0.5,
                           color='black',
                           frameon=False,
                           size_vertical=0.001)  # 调整比例尺的宽度

ax.add_artist(scalebar)

# 显示图像
plt.tight_layout()
plt.show()