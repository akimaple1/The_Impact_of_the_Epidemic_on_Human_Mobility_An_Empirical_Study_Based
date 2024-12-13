import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os

# 'az','co','ct','ny'
su = ['al', 'az', 'ca', 'co', 'ct', 'de', 'fl', 'ga', 'hi', 'ia', 'il', 'in', 'ks', 'ky', 'la', 'ma', 'md', 'me', 'mi','mn', 'mo', 'mt', 'nc', 'nd', 'ne', 'nh', 'nj', 'nm', 'nv', 'ny', 'oh', 'ok', 'or', 'pa', 'sc', 'sd', 'tn', 'ut','va', 'vt', 'wa']

for ii in su:
    for iii in range(19, 22):
        for iiii in range(1,4):
            try:
                file_path = "E:\\实验室\\第一篇区域等级划分访问\\正式\\experiment\\2_excel\\{}_{}_2SA0{}.csv".format(ii,str(iii),str(iiii))
                data = pd.read_csv(file_path)


                gamma_folder = f"E:\\实验室\\第一篇区域等级划分访问\\正式\\experiment\\2_tu12\\gamma\\{ii}"
                avg_folder = f"E:\\实验室\\第一篇区域等级划分访问\\正式\\experiment\\2_tu12\\avg\\{ii}"
                sigma_folder = f"E:\\实验室\\第一篇区域等级划分访问\\正式\\experiment\\2_tu12\\sigma\\{ii}"
                os.makedirs(gamma_folder, exist_ok=True)
                os.makedirs(avg_folder, exist_ok=True)
                os.makedirs(sigma_folder, exist_ok=True)


                # Create a colormap for the line chart
                viridis = plt.get_cmap('viridis')
                colors = viridis(np.linspace(0, 1, 10))  # Generate colors for the 10 different group2 values

                # 1. Plot for 'gamma'
                fig, ax = plt.subplots(figsize=(10, 6))
                for i, color in zip(range(1, 11), colors):  # Assuming group2 ranges from 1 to 10
                    subset = data[data['group2'] == i]
                    ax.plot(subset['group1'], subset['gamma'], marker='o', color=color, label=f'Group2={i}')

                ax.set_xlabel('Group1')
                ax.set_ylabel('Gamma')
                ax.set_title('{} 20{} SA0{} - Gamma per Group1 and Group2 (Viridis Colormap)'.format(ii, iii, str(iiii)))
                ax.legend(bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=0.)
                plt.savefig("E:\\实验室\\第一篇区域等级划分访问\\正式\\experiment\\2_tu12\\gamma\\{}\\2SA0{}_{}_{}.png".format(ii,str(iiii), ii,str(iii)), bbox_inches='tight')
                plt.show()

                # 2. Plot for 'avg_distance'
                fig, ax = plt.subplots(figsize=(10, 6))
                for i, color in zip(range(1, 11), colors):  # Assuming group2 ranges from 1 to 10
                    subset = data[data['group2'] == i]
                    ax.plot(subset['group1'], subset['avg_distance'], marker='o', color=color, label=f'Group2={i}')

                ax.set_xlabel('Group1')
                ax.set_ylabel('Average Distance')
                ax.set_title('{} 20{} SA0{} - Avg Distance per Group1 and Group2 (Viridis Colormap)'.format(ii, iii, str(iiii)))
                ax.legend(bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=0.)
                plt.savefig("E:\\实验室\\第一篇区域等级划分访问\\正式\\experiment\\2_tu12\\avg\\{}\\2SA0{}_{}_{}.png".format(ii,str(iiii), ii,str(iii)), bbox_inches='tight')
                plt.show()

                # 3. Plot for 'sigma'
                fig, ax = plt.subplots(figsize=(10, 6))
                for i, color in zip(range(1, 11), colors):  # Assuming group2 ranges from 1 to 10
                    subset = data[data['group2'] == i]
                    ax.plot(subset['group1'], subset['sigma'], marker='o', color=color, label=f'Group2={i}')

                ax.set_xlabel('Group1')
                ax.set_ylabel('Sigma')
                ax.set_title('{} 20{} SA0{} - Sigma per Group1 and Group2 (Viridis Colormap)'.format(ii, iii, str(iiii)))
                ax.legend(bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=0.)
                plt.savefig("E:\\实验室\\第一篇区域等级划分访问\\正式\\experiment\\2_tu12\\sigma\\{}\\2SA0{}_{}_{}.png".format(ii,str(iiii), ii,str(iii)), bbox_inches='tight')
                plt.show()

            except Exception as e:
                print(f"Error processing {ii} 20{iii}: {e}")


