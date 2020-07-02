#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : kmeans_test.py
# Author: hugh
# Date  : 2020/7/2

from sklearn.cluster import KMeans
from sklearn import preprocessing
import pandas as pd
import numpy as np

import PIL.Image as image
import matplotlib.image as mpimg
import os
from skimage import color

base_path = os.path.dirname(os.path.realpath(__file__))\
    .replace(os.path.join('hugh', os.path.join('base_some', 'base_data_ana')), '')
print(base_path)

file_dir = os.path.join(os.path.join(base_path, 'files'), 'kmeans')

def load_data(filePath):
    f = open(filePath, 'rb')
    data = []
    # 得到图像的像素值
    img = image.open(f)
    # 得到图像尺寸
    width, height = img.size
    print(img)

    for x in range(width):
        for y in range(height):
            # 注意png jpg等像素的不同 这里是rgb
            c1, c2, c3 = img.getpixel((x,y))
            data.append([(c1 + 1) / 256.0, (c2 + 1) / 256.0, (c3 + 1) / 256.0])

    f.close()
    return np.mat(data), width, height



def test_kmeans1():
    '''

    :return:
    '''
    # 加载图像，得到规范化的结果imgData，以及图像尺寸
    img, width, height = load_data(os.path.join(file_dir, 'weixin.jpg'))
    # 用K-Means对图像进行16聚类
    kmeans =KMeans(n_clusters=16)
    label = kmeans.fit_predict(img)
    # 将图像聚类结果，转化成图像尺寸的矩阵
    label = label.reshape([width, height])
    # 创建个新图像img，用来保存图像聚类压缩后的结果
    # img=image.new('RGB', (width, height))
    # for x in range(width):
    #     for y in range(height):
    #         c1 = kmeans.cluster_centers_[label[x, y], 0]
    #         c2 = kmeans.cluster_centers_[label[x, y], 1]
    #         c3 = kmeans.cluster_centers_[label[x, y], 2]
    #         img.putpixel((x, y), (int(c1*256)-1, int(c2*256)-1, int(c3*256)-1))
    # img.save(os.path.join(file_dir, 'weixin_new.jpg'))

    # 将聚类标识矩阵转化为不同颜色的矩阵
    label_color = (color.label2rgb(label) * 255).astype(np.uint8)
    label_color = label_color.transpose(1, 0, 2)
    images = image.fromarray(label_color)
    images.save(os.path.join(file_dir, 'weixin_new.jpg'))

def test_kmeans():
    '''
    KMeans(algorithm='auto', copy_x=True, init='k-means++', max_iter=300,
    n_clusters=8, n_init=10, n_jobs=None, precompute_distances='auto',
    random_state=None, tol=0.0001, verbose=0)
    n_clusters: 即 K 值，一般需要多试一些 K 值来保证更好的聚类效果。
    n_init：初始化中心点的运算次数，默认是 10。程序是否能快速收敛和中心点的选择关系非常大，
    所以在中心点选择上多花一些时间，来争取整体时间上的快速收敛还是非常值得的。
    由于每一次中心点都是随机生成的，这样得到的结果就有好有坏，非常不确定，
    所以要运行 n_init 次, 取其中最好的作为初始的中心点。如果 K 值比较大的时候，你可以适当增大 n_init 这个值；
    init： 即初始值选择的方式，默认是采用优化过的 k-means++ 方式，你也可以自己指定中心点，
    或者采用 random 完全随机的方式。自己设置中心点一般是对于个性化的数据进行设置，很少采用。
    random 的方式则是完全随机的方式，一般推荐采用优化过的 k-means++ 方式；
    algorithm：k-means 的实现算法，有“auto” “full”“elkan”三种。一般来说建议直接用默认的"auto"。
    简单说下这三个取值的区别，如果你选择"full"采用的是传统的 K-Means 算法，
    “auto”会根据数据的特点自动选择是选择“full”还是“elkan”。我们一般选择默认的取值，即“auto” 。

    :return:
    '''
    data = pd.read_csv('')
    train_x = data[['', '', '']]
    df = pd.DataFrame(train_x)
    kmens = KMeans(n_clusters=3)
    min_max_scaler = preprocessing.MinMaxScaler()
    train_x =  min_max_scaler.fit_transform(train_x)
    kmens.fit(train_x)
    predict = kmens.predict(train_x)
    # predict = kmens.fit_predict(train_x)
    result = pd.concat((data, pd.DataFrame(predict)), axis=1)
    result.rename({0:u'聚类'})


if __name__ == '__main__':
    '''
    K-means 聚类问题
    选取 K 个点作为初始的类中心点，这些点一般都是从数据集中随机抽取的；
    将每个点分配到最近的类中心点，这样就形成了 K 个类，然后重新计算每个类的中心点；
    重复第二步，直到类不发生变化，或者你也可以设置最大迭代次数，这样即使类中心点发生变化，
    但是只要达到最大迭代次数就会结束。
    
    
    '''
    # test_kmeans()
    test_kmeans1()