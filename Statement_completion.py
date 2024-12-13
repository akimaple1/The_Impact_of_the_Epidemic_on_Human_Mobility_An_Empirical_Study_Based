import pandas as pd
sss=['al','az','ca','co','ct','de','fl','ga','hi','ia','il','in','ks','ky','la','ma','md','me','mi','mn','mo','mt','nc','nd','ne','nh','nj','nm','nv','ny','oh','ok','or','pa','sc','sd','tn','ut','va','vt','wa']
link=[]
for ii in sss:
    for iii in range(19,22):
        for iiii in range(1,4):
            try:
                input_file = "E:\\实验室\\第一篇区域等级划分访问\\正式\\experiment\\2_excel\\{}_{}_2SA0{}.csv".format(ii,str(iii),str(iiii))
                df_exponents = pd.read_csv(input_file)

                    # 创建一个 DataFrame 来存储新的组合
                new_combinations = []

                    # 遍历每一行，添加新的组合 (g2, g1)
                for _, row in df_exponents.iterrows():
                    if row['group2'] != row['group1']:
                        new_combinations.append({
                            'group1': row['group2'],
                            'group2': row['group1'],
                            'gamma': row['gamma'],
                            'r_squared': row['r_squared'],
                            'avg_distance': row['avg_distance'],
                            'sigma': row['sigma']
                        })

                    # 将新的组合添加到原始 DataFrame
                df_new_combinations = pd.DataFrame(new_combinations)
                df_combined = pd.concat([df_exponents, df_new_combinations], ignore_index=True)



                    # 保存新的 CSV 文件
                output_file = "E:\\实验室\\第一篇区域等级划分访问\\正式\\experiment\\2_excel\\{}_{}_2SA0{}.csv".format(ii,str(iii),str(iiii))
                df_combined.to_csv(output_file, index=False)

                    # 打印保存路径和结果
                print(f"新的组合已保存到: {output_file}")
                print(df_combined.head())
            except Exception:
                error=[ii,iii,iiii]
                link.append(error)

print(link)