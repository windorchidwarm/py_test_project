#!/usr/bin/env python
# -- coding: utf-8 --#
# @Time : 2019/12/20 15:23 
# @Author : Aries 
# @Site :  
# @File : ip_and_move.py
# @Software: PyCharm

# A10;S20;W10;D30;X;A1A;B10A11;;A10;

import sys

def move(data):
    '''
    坐标移动
    :param line:
    :return:
    '''
    x,y = 0,0
    for line in data:
        str_add = line[1:]

        if str_add is None or str_add == '' or not str_add.isdigit():
            continue

        simbol = line[0:1]
        if simbol == 'A':
            x = x - int(str_add)
        elif simbol == 'D':
            x = x + int(str_add)
        elif simbol == 'W':
            y = y + int(str_add)
        elif simbol == 'S':
            y = y - int(str_add)
    return x,y


def ip_to_num(ip_str):
    '''
    ip 字符串转换为 数字
    :param ip_str:
    :return:
    '''
    ips = ip_str.strip().split('.')
    num_str = ''
    for ip in ips:
        num_str += '{:08b}'.format(int(ip))
        # ip_in = str(bin(int(ip))).replace('0b', '')
        # ip_in = ('0' * (8 - len(ip_in))) + ip_in
        # num_str += ip_in
    return int(num_str, 2)


def num_to_ip(num):
    '''
    数字转换为Ip字符串
    :param num:
    :return:
    '''
    # bi_ip = str(bin(num)).replace('0b', '')
    # bi_ip = ('0' * (32 - len(bi_ip))) + bi_ip
    bi_ip = '{:032b}'.format(num)
    ip_str = ''
    for i in range(4):
        ip_str += str(int(bi_ip[0 + 8 * i :8 + 8 * i], 2)) + '.'
    ip_str = ip_str[0: -1]
    return  ip_str


if __name__ == '__main__':
    # s = input().split(';')
    # x, y = move(s)
    # print(x, ",", y)

    # tmp = '254'
    # print(str(bin(int(tmp))).replace('0b', ''))

    # ee = '255.0.102.0'.split('.')
    # tt = ''
    # for i in range(4):
    #     tt += str(bin(int(ee[i]))).replace('0b', '')
    # print(tt)
    # print('01' in tt)

    # a, b, c, d, e, error, per = 0, 0, 0, 0, 0, 0,0
    # while True:
    #     try:
    #         addr = sys.stdin.readline().strip()
    #         if not '~' in addr:
    #             error += 1
    #             continue
    #         ip = addr.split('~')[0].split('.')
    #         code = addr.split('~')[1].split('.')
    #         if len(ip) != 4 or len(code) != 4:
    #             error += 1
    #             continue
    #         res = True
    #         code_str = ''
    #         for i in range(4):
    #             if ip[i] is None or ip[i] == '' or code[i] is None or code[i] == '' or int(ip[i]) < 0 or int(code[i]) < 0 or int(ip[i]) > 255 or int(code[i]) > 255:
    #                 res = False
    #             else:
    #                 code_str += str(bin(int(code[i]))).replace('0b', '')
    #         if not res:
    #             error += 1
    #             continue
    #         if '01' in code_str or 0 == int(ip[0]):
    #             error += 1
    #             continue
    #
    #         if int(ip[0]) <= 126:
    #             a += 1
    #         elif int(ip[0]) <= 191:
    #             b += 1
    #         elif int(ip[0]) <= 223:
    #             c += 1
    #         elif int(ip[0]) <= 239:
    #             d += 1
    #         elif int(ip[0]) <= 255:
    #             e += 1
    #
    #         if int(ip[0]) == 10 or (int(ip[0]) == 172 and int(ip[1]) >= 16 and int(ip[1]) <= 31) or (int(ip[0]) == 192 and int(ip[1]) == 168):
    #             per += 1
    #         print(str(a) + ' ' + str(b) + ' ' + str(c) + ' ' + str(d) + ' ' + str(e) + ' ' + str(error) + ' ' + str(per) + ' ')
    #     except:
    #         break
    # print(str(a) + ' ' + str(b) + ' ' + str(c) + ' ' + str(d) + ' ' + str(e) + ' ' + str(error) + ' ' + str(per) + ' ')

    # a, b, c, d, e, er, per = 0, 0, 0, 0, 0, 0, 0
    # apt = []
    # try:
    #     while True:
    #         line = sys.stdin.readline().strip()
    #         if line == '':
    #             break
    #         apt.append(line)
    # except:
    #     pass
    #
    # for addr in apt:
    #     if addr == '':
    #         break
    #     if not '~' in addr:
    #         er += 1
    #         continue
    #     ip = addr.split('~')[0].split('.')
    #     code = addr.split('~')[1].split('.')
    #     if code == '255.255.255.255':
    #         er += 1
    #         continue
    #
    #     if len(ip) != 4 or len(code) != 4:
    #         er += 1
    #         continue
    #     res = True
    #     code_str = ''
    #     for i in range(4):
    #         if ip[i] is None or ip[i] == '' or code[i] is None or code[i] == '' or int(ip[i]) < 0 or int(
    #                 code[i]) < 0 or int(ip[i]) > 255 or int(code[i]) > 255:
    #             res = False
    #         else:
    #             code_str += str(bin(int(code[i]))).replace('0b', '')
    #     if not res:
    #         er += 1
    #         continue
    #     if '01' in code_str:
    #         er += 1
    #         continue
    #
    #     if int(ip[0]) in range(1, 127):
    #         a += 1
    #     elif int(ip[0]) in range(128, 192):
    #         b += 1
    #     elif int(ip[0]) in range(192, 224):
    #         c += 1
    #     elif int(ip[0]) in range(224, 240):
    #         d += 1
    #     elif int(ip[0]) in range(240, 255):
    #         e += 1
    #
    #     if (int(ip[0]) == 10) or (int(ip[0]) == 172 and int(ip[1]) in range(16, 32)) or (
    #             int(ip[0]) == 192 and int(ip[1]) == 168):
    #         per += 1
    #
    # print(str(a) + ' ' + str(b) + ' ' + str(c) + ' ' + str(d) + ' ' + str(e) + ' ' + str(er) + ' ' + str(per) + ' ')


    A = 0
    B = 0
    C = 0
    D = 0
    E = 0
    count = 0
    siyo = 0


    apt = []
    try:
        while True:
            line = sys.stdin.readline().strip()
            if line == '':
                break
            apt.append(line)
    except:
        pass
    for v in apt:
        Ide = v.index('~')
        IP = v[:Ide]
        IPY = v[Ide + 1:]
        ym = list(filter(None, IPY.split('.')))
        print(ym)
        if len(ym) == 4 and ym != ['255', '255', '255', '255'] and ym != ['0', '0', '0', '0']:
            t = 1
            for y in ym:
                if int(y) >= 0 and int(y) < 256:
                    print('{:08b}'.format(int(y)))
                    for x in ('{:08b}'.format(int(y))):
                        print(x)
                        if t - int(x) >= 0:
                            t = int(x)
                            yero = True
                        else:
                            count = count + 1
                            yero = False
                            break
                    if yero == False:
                        break
            if yero == False:
                pass
            else:
                ip = list(filter(None, congzu(IP, '.')))
                if ip[0] != '0':
                    if len(ip) == 4:
                        for i in ip:
                            try:
                                int(i)
                                if int(i) >= 0 and int(i) < 256:
                                    iero = True
                                else:
                                    iero = False
                                    count = count + 1
                                    break
                            except:
                                iero = False
                                count = count + 1
                                break
                        if iero == False:
                            break
                        else:
                            if int(ip[0]) in range(1, 127):
                                A = A + 1
                                if int(ip[0]) == 10:
                                    siyo = siyo + 1
                            elif int(ip[0]) in range(128, 192):
                                B = B + 1
                                if int(ip[0]) == 172 and int(ip[1]) in range(16, 32):
                                    siyo = siyo + 1
                            elif int(ip[0]) in range(192, 224):
                                C = C + 1
                                if int(ip[0]) == 192 and int(ip[1]) == 168:
                                    siyo = siyo + 1
                            elif int(ip[0]) in range(224, 240):
                                D = D + 1
                            elif int(ip[0]) in range(240, 255):
                                E = E + 1
                            else:
                                pass
                    else:
                        count = count + 1
                else:
                    pass
        else:
            count = count + 1
    print(str(A) + ' ' + str(B) + ' ' + str(C) + ' ' + str(D) + ' ' + str(E) + ' ' + str(count) + ' ' + str(siyo))

    # line = input().strip()
    # ip_num = int(input().strip())
    # print(ip_to_num(line))
    # print(num_to_ip(ip_num))