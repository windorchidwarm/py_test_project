#!/usr/bin/env python
# -- coding: utf-8 --#
# @Time : 2019/12/25 18:20 
# @Author : Aries 
# @Site :  
# @File : min_edit_route.py 
# @Software: PyCharm



def min_edit_rout(data, end_data):
    '''
    从data到end_data的最短编辑距离
    :param data:
    :param end_data:
    :return:
    '''
    if data == '' or end_data == '':
        return max(len(end_data), len(data))
    d_len = len(data)
    n_len = len(end_data)
    m = [[0 for i in range(d_len + 1)] for j in range(n_len + 1)]

    for i in range(d_len + 1):
        m[0][i] = i

    for i in range(n_len + 1):
        m[i][0] = i

    for i in range(1, d_len + 1):
        for j in range(1, n_len + 1):
            m_min = m[j - 1][i - 1] if data[i - 1] == end_data[j - 1] else m[j - 1][i - 1] + 1
            m[j][i] = min(m_min, m[j - 1][i] + 1, m[j][i - 1] + 1)
        print(m)
    return m[n_len][d_len]

if __name__ == '__main__':
    data = 'ixfkieaaocalmxhfifyadnouljtezrnpnfoenespcaenyvzcjtppsaxegmeytqrkvdwugvouskcnnqnmhepquncvyvgkansquaotkgvlvplktrabaikeuubfupunpztpvvzdqaqgfmtzxlcxsipltzwjegpqjzclclvjsmqbmiyzvcujpvhupyhvhhjq'
    end_data = 'ganxioafstgdpceecubqrngumbpjvwxdpzmragsunvfnmejbcvsoydtbbewybygpsmmyjuvezn'
    print(min_edit_rout(data, end_data))