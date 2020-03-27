#!/usr/bin/env python
# -- coding: utf-8 --#
# @Time : 2020/3/26 13:37 
# @Author : Aries 
# @Site :  
# @File : seaborn_test.py 
# @Software: PyCharm


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
import os
import seaborn

COMPONENT_PATH = os.path.join(os.path.dirname(os.path.realpath(__file__))
                              .replace(os.path.join('hugh', os.path.join("onon","guiyang")),''),"files")



def test_seaborn():
    df = pd.read_csv(r'C:\Users\BBD\Desktop\test\tmp\recruit_index_by_province_result.csv', encoding="utf-8", header=0)

    print(df)
    # df = df.sort_values('year_2019_after_df_count', ascending=False)
    print(df)
    print(df.columns)

    # my_font = fm.FontProperties(fname=r'C:\Windows\Fonts\STXINGKA.TTF')
    # my_font = fm.FontProperties(fname=r'E:\BaiduNetdiskDownload\汉仪大隶书繁.ttf')
    my_font = fm.FontProperties(fname=os.path.join(COMPONENT_PATH,"msyhbd.ttc"))
    seaborn.set_style("darkgrid")
    plt.title("中文")
    # seaborn.set(font=my_font.get_name())
    p = seaborn.boxplot(x='company_province', y='year_2019_after_df_count', data=df, hue='year_2019_after_df_count')
    result = p.get_figure()
    plt.xticks(fontproperties=my_font)
    print(result)
    plt.show()


def test_seaborn2():
    # my_font = fm.FontProperties(fname=os.path.join(COMPONENT_FILE_PATH,"msyhbd.ttc"))
    my_font = fm.FontProperties(fname=r'E:\BaiduNetdiskDownload\汉仪大隶书繁.ttf')
    # df = pd.read_csv("C:/Users/Administrator/Desktop/test_data_classification.csv")
    df = pd.read_csv(r'C:\Users\BBD\Desktop\test\tmp\recruit_index_by_province_result.csv', encoding="utf-8", header=0)

    x = "company_province"
    y = "year_2019_after_df_count"

    # plt.xticks(fontproperties=my_font)
    seaborn.set_style("darkgrid")
    # seaborn.set(font=my_font.get_name())
    p = seaborn.boxplot(x=x, y=y, data=df, hue=y)
    # plt.title("中文")
    print(my_font.get_name())
    p.get_figure()
    plt.xticks(fontproperties=my_font)
    plt.show()

if __name__ == '__main__':
    print('xxx')
    # test_seaborn()
    test_seaborn2()