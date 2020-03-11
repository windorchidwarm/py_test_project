#!/usr/bin/env python
# -- coding: utf-8 --#
# @Time : 2020/3/9 16:09 
# @Author : Aries 
# @Site :  
# @File : test_plot.py 
# @Software: PyCharm


import pandas as pd

import matplotlib.pyplot as plt
import matplotlib.font_manager as fm  #字体管理器

def test_plot():
    df = pd.read_csv(r'C:\Users\BBD\Desktop\test\tmp\recruit_index_by_province_result.csv', encoding="utf-8", header=0)

    print(df)
    # df = df.sort_values('year_2019_after_df_count', ascending=False)
    print(df)
    print(df.columns)

    my_font = fm.FontProperties(fname=r'C:\Windows\Fonts\STXINGKA.TTF')

    # ln1, = plt.plot(df['company_province'],df['year_2019_after_df_count'],color='red',linewidth=2.0,linestyle='--')
    # ln2, = plt.plot(df['company_province'],df['year_2020_after_df_count'],color='blue',linewidth=3.0,linestyle='-.')
    # plt.xticks(fontproperties=my_font)
    # plt.xlabel("x轴", fontproperties=my_font) # 步骤三
    # plt.ylabel("y轴", fontproperties=my_font)
    # plt.title("电子产品销售量",fontproperties=my_font) #设置标题及字体
    # plt.show()

    dfgp1 = (df['year_2019_after_df_count']).groupby(df['company_province']).sum()
    print(dfgp1)
    dfgp2 = (df['year_2020_after_df_count']).groupby(df['company_province']).sum()
    print(dfgp2)
    dfgpx = (df['company_province'])
    print(dfgpx)
    # figsize = 30,8
    # figure, ax = plt.subplots(figsize=figsize)
    # plt.plot(dfgpx,dfgp1,dfgp2)
    plt.ylabel('rec_num')  # 显示y轴名称
    plt.xlabel('province')  # 显示x轴名称
    plt.title('2019 vs.2020')  # 显示统计标题
    dfgp1.plot.line(label='after 2019')  # 2019春节后
    dfgp2.plot.line(label='after 2020')  # 2020春节后
    plt.xticks(fontproperties=my_font)

    plt.tick_params(labelsize=13)
    plt.tight_layout()
    plt.show()



def over_lap_test():
    print('xxxx')


if __name__ == '__main__':
    print('xxx')