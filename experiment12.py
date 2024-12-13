import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.colors import LinearSegmentedColormap
#'az','co','ct','ny'
su=['al','az','ca','co','ct','de','fl','ga','hi','ia','il','in','ks','ky','la','ma','md','me','mi','mn','mo','mt','nc','nd','ne','nh','nj','nm','nv','ny','oh','ok','or','pa','sc','sd','tn','ut','va','vt','wa']
#su=["ga"]
for ii in su:
    for iii in range(19,22):
        try:
            # 读取上传的 CSV 文件
            file_path = "E:\\实验室\\第一篇区域等级划分访问\\正式\\experiment\\1_excel\\{}_{}_2.csv".format(ii,str(iii))
            df = pd.read_csv(file_path)

            # 创建一个透视表，以便绘制热力图
            pivot_table = df.pivot(index='group2', columns='group1', values='gamma')

            min_val = pivot_table.min().min()
            max_val = pivot_table.max().max()
            # 自定义归一化函数，确保负值映射接近0，正值映射接近1
            def normalize(value, min_val, max_val):
                return (value - min_val) / (max_val - min_val)
            # 对数据进行归一化处理，使用我们自定义的归一化函数
            pivot_table_normalized = pivot_table.applymap(lambda x: normalize(x, min_val, max_val))

            # 使用 seaborn 创建颜色列表，然后转换为 LinearSegmentedColormap
            colors = sns.color_palette("Spectral")
            colors.reverse()
            cmap = LinearSegmentedColormap.from_list("mycmap", colors)


            # 重新绘制热力图
            plt.figure(figsize=(10, 8))
            sns.heatmap(pivot_table_normalized, annot=False, cmap=cmap, cbar=True)
            plt.title('{} 20{} gamma'.format(ii,iii))
            plt.xlabel('group1')
            plt.ylabel('group2')

            plt.gca().invert_yaxis()
            plt.savefig('E:\\实验室\\第一篇区域等级划分访问\\正式\\experiment\\1_tu1111\\gamma\\{}_{}_gamma'.format(ii,iii))
            plt.show()


            pivot_table = df.pivot(index='group2', columns='group1', values='avg_distance')

            min_val1 = pivot_table.min().min()
            max_val1 = pivot_table.max().max()
            # 自定义归一化函数，确保负值映射接近0，正值映射接近1
            def normalize1(value, min_val, max_val):
                return (value - min_val) / (max_val - min_val)
            # 对数据进行归一化处理，使用我们自定义的归一化函数
            pivot_table_normalized = pivot_table.applymap(lambda x: normalize1(x, min_val1, max_val1))

            # 使用 seaborn 创建颜色列表，然后转换为 LinearSegmentedColormap
            colors = sns.color_palette("Spectral")
            colors.reverse()
            cmap = LinearSegmentedColormap.from_list("mycmap", colors)


            # 重新绘制热力图
            plt.figure(figsize=(10, 8))
            sns.heatmap(pivot_table_normalized, annot=False, cmap=cmap, cbar=True)
            plt.title('{} 20{} avg_distance'.format(ii,iii))
            plt.xlabel('group1')
            plt.ylabel('group2')

            plt.gca().invert_yaxis()
            plt.savefig('E:\\实验室\\第一篇区域等级划分访问\\正式\\experiment\\1_tu1111\\avg\\{}_{}_avg'.format(ii,iii))
            plt.show()


            pivot_table = df.pivot(index='group2', columns='group1', values='sigma')

            min_val2 = pivot_table.min().min()
            max_val2 = pivot_table.max().max()
            # 自定义归一化函数，确保负值映射接近0，正值映射接近1
            def normalize2(value, min_val, max_val):
                return (value - min_val) / (max_val - min_val)
            # 对数据进行归一化处理，使用我们自定义的归一化函数
            pivot_table_normalized = pivot_table.applymap(lambda x: normalize2(x, min_val2, max_val2))

            # 使用 seaborn 创建颜色列表，然后转换为 LinearSegmentedColormap
            colors = sns.color_palette("Spectral")
            colors.reverse()
            cmap = LinearSegmentedColormap.from_list("mycmap", colors)


            # 重新绘制热力图
            plt.figure(figsize=(10, 8))
            sns.heatmap(pivot_table_normalized, annot=False, cmap=cmap, cbar=True)
            plt.title('{} 20{} sigma'.format(ii,iii))
            plt.xlabel('group1')
            plt.ylabel('group2')

            plt.gca().invert_yaxis()
            plt.savefig('E:\\实验室\\第一篇区域等级划分访问\\正式\\experiment\\1_tu1111\\sigma\\{}_{}_sigma'.format(ii,iii))
            plt.show()
        except Exception:
            oo=1