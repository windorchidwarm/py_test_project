#!/usr/bin/env python
# -- coding: utf-8 --#
# @Time : 2019/12/24 15:15 
# @Author : Aries 
# @Site :  
# @File : num_to_en.py 
# @Software: PyCharm



word_and = 'and'
num_en = ['zero','one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']
num_ten_en = ['twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety', 'hundred', 'thousand', 'million', 'billion']


def num_to_en(num):
    '''
    输入数字 转换为对应英文
    :param num:
    :return:
    '''
    if num == 0:
        return []
    elif num < 20:
        return [num_en[num]]
    elif num < 100:
        return [num_ten_en[num // 10 - 2]] +  num_to_en(num % 10)
    elif num < 1000:
        return [num_en[num // 100 ]] + ['hundred'] + ['and'] + num_to_en(num % 100)
    else:
        for w,p in enumerate(('thousand', 'million', 'billion'), 1):
            if (num < 1000 ** (w + 1)):
                return num_to_en(num // (1000**w) )+[p] + num_to_en( num % (1000 **w ))


if __name__ == '__main__':
    print('----------')
    print(' '.join(num_to_en(123456780)))