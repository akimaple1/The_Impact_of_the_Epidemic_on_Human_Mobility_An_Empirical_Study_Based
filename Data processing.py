import pandas as pd
from tqdm import tqdm
import os


def load_data(xwalk_path, od_path):
    # 加载数据
    xwalk_data = pd.read_csv(xwalk_path)
    od_data = pd.read_csv(od_path)
    return xwalk_data, od_data


def get_coordinates_mapping(xwalk_data):
    # 创建经纬度映射
    return xwalk_data.set_index('tabblk2020')[['blklatdd', 'blklondd']]


def apply_coordinates(geocode_series, mapping):
    # 应用映射以获取经纬度
    latitudes = geocode_series.map(mapping['blklatdd'])
    longitudes = geocode_series.map(mapping['blklondd'])
    return latitudes, longitudes


def main(xwalk_file, od_file, output_file):
    # 加载数据
    xwalk_data, od_data = load_data(xwalk_file, od_file)

    # 获取经纬度映射
    mapping = get_coordinates_mapping(xwalk_data)

    # 应用映射到OD数据
    od_data['w_lat'], od_data['w_lon'] = apply_coordinates(od_data['w_geocode'], mapping)
    od_data['h_lat'], od_data['h_lon'] = apply_coordinates(od_data['h_geocode'], mapping)

    # 保存结果
    output_dir = os.path.dirname(output_file)
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # 保存结果
    od_data.to_csv(output_file, index=False)
    print(f"Data saved to {output_file}")


# 文件路径定义
for x in tqdm(range(0,6)):
    for y in tqdm(range(2018,2022)):
        try:
            xwalk_file_path = 'D:\\数据\\美国人流数据\\dc\\dc_xwalk.csv'
            od_file_path = 'D:\\数据\\美国人流数据\\dc\\dc_od_main_JT0{}_{}.csv'.format(x,y)
            output_file_path = 'D:\\数据\\美国人流数据\\dc\\匹配\\{}\\output_dc_od_main_JT0{}_{}.csv'.format(y,x,y)

            # 调用主函数
            main(xwalk_file_path, od_file_path, output_file_path)
        except:
            continue
