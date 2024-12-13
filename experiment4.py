import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap
from mpl_toolkits.mplot3d import Axes3D
import seaborn as sns
import os

# 'az','co','ct','ny'
#su = ['al', 'az', 'ca', 'co', 'ct', 'de', 'fl', 'ga', 'hi', 'ia', 'il', 'in', 'ks', 'ky', 'la', 'ma', 'md', 'me', 'mi', 'mn', 'mo', 'mt', 'nc', 'nd', 'ne', 'nh', 'nj', 'nm', 'nv', 'ny', 'oh', 'ok', 'or', 'pa', 'sc', 'sd', 'tn', 'ut', 'va', 'vt', 'wa']
# su = ["ga"]
su=['ia']

for ii in su:
    for iii in range(19, 22):
        for iiii in range(1, 4):
            try:
                # 读取上传的 CSV 文件
                file_path = "E:\\实验室\\第一篇区域等级划分访问\\正式\\experiment\\2_excel\\{}_{}_2SA0{}.csv".format(ii, str(iii),str(iiii))
                df = pd.read_csv(file_path)

                # 创建文件夹以保存图片
                gamma_folder = f"E:\\实验室\\第一篇区域等级划分访问\\正式\\experiment\\3wei\\gamma\\{ii}"
                avg_folder = f"E:\\实验室\\第一篇区域等级划分访问\\正式\\experiment\\3wei\\avg\\{ii}"
                sigma_folder = f"E:\\实验室\\第一篇区域等级划分访问\\正式\\experiment\\3wei\\sigma\\{ii}"
                os.makedirs(gamma_folder, exist_ok=True)
                os.makedirs(avg_folder, exist_ok=True)
                os.makedirs(sigma_folder, exist_ok=True)

                # 定义一个绘制3D图的函数
                def plot_3d_surface(pivot_table, title, save_path):
                    x = np.arange(pivot_table.shape[1])
                    y = np.arange(pivot_table.shape[0])
                    x, y = np.meshgrid(x, y)
                    z = pivot_table.values

                    # 创建3D图形
                    fig = plt.figure(figsize=(10, 8))
                    ax = fig.add_subplot(111, projection='3d')

                    # 使用自定义的颜色映射
                    colors = sns.color_palette("Spectral")
                    colors.reverse()
                    cmap = LinearSegmentedColormap.from_list("mycmap", colors)

                    # 绘制3D表面图
                    surf = ax.plot_surface(x, y, z, cmap=cmap)
                    fig.colorbar(surf)

                    # 设置轴标签和标题
                    ax.set_xlabel('Group1')
                    ax.set_ylabel('Group2')
                    ax.set_zlabel('Normalized Value')
                    ax.set_title(title)

                    # 保存并显示图像
                    plt.savefig(save_path)
                    plt.show()

                # 处理gamma
                pivot_table = df.pivot(index='group2', columns='group1', values='gamma')
                min_val, max_val = pivot_table.min().min(), pivot_table.max().max()
                pivot_table_normalized = pivot_table.applymap(lambda x: (x - min_val) / (max_val - min_val))
                title = '{} 20{} gamma'.format(ii, iii)
                save_path = "E:\\实验室\\第一篇区域等级划分访问\\正式\\experiment\\3wei\\gamma\\{}\\2SA0{}_{}_{}.png".format(ii,str(iiii), ii,str(iii))
                plot_3d_surface(pivot_table_normalized, title, save_path)

                # 处理avg_distance
                pivot_table = df.pivot(index='group2', columns='group1', values='avg_distance')
                min_val, max_val = pivot_table.min().min(), pivot_table.max().max()
                pivot_table_normalized = pivot_table.applymap(lambda x: (x - min_val) / (max_val - min_val))
                title = '{} 20{} avg_distance'.format(ii, iii)
                save_path = "E:\\实验室\\第一篇区域等级划分访问\\正式\\experiment\\3wei\\avg\\{}\\2SA0{}_{}_{}.png".format(ii,str(iiii), ii,str(iii))
                plot_3d_surface(pivot_table_normalized, title, save_path)

                # 处理sigma
                pivot_table = df.pivot(index='group2', columns='group1', values='sigma')
                min_val, max_val = pivot_table.min().min(), pivot_table.max().max()
                pivot_table_normalized = pivot_table.applymap(lambda x: (x - min_val) / (max_val - min_val))
                title = '{} 20{} sigma'.format(ii, iii)
                save_path = "E:\\实验室\\第一篇区域等级划分访问\\正式\\experiment\\3wei\\sigma\\{}\\2SA0{}_{}_{}.png".format(ii,str(iiii), ii,str(iii))
                plot_3d_surface(pivot_table_normalized, title, save_path)

            except Exception as e:
                print(f"Error processing {ii} 20{iii}: {e}")
