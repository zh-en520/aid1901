#!/usr/bin/env python3
# -*- coding:utf-8 -*-

# Author :魏泽明（达内北京）
＃ dat   :2017
#版权参考

"""2048游戏

本模块已完整实现２０４８游戏的算法及分数的计算算法
游戏的界面采用Ｐｙｔｈｏｎ标准库tkinter来实现
此界面的布局采用tkinter中的grid布局
"""

import random#导入随机模块ｒａｎｄｏｍ，主要用于随机生成新的数字及数字摆放位置
import math #导入数学模块，用来计算分数

＃_map_data 绑定一个4 * 4列表，此列表为２０４８游戏地图，初始值如下：
_map_data =[
    [0,0,0,0],
    [0,0,0,0],
    [0,0,0,0],
    [0,0,0,0]
]
＃－－－－－－－－－－－－以下为２０４８游戏的基本算法－－－－－－－－－－
def reset():
    '''重新设置游戏数据，将地图回复为初始状态，并加入两个数据２作用初始状态’‘’
    _map_data[:]=[]#_map_data.clear()
    _map_data.append([0,0,0,0])
    _map_data.append([0,0,0,0])
    _map_data.append([0,0,0,0])
    _map_data.append([0,0,0,0])
    #在空白地图上填充两个２
    fill2()
    fill2()

def get_space_count():
    """获取没有数字的方格的数量，如果数量为０则说明无法填充新数据，游戏即将结束"""
    count=0
    for r in _map_data:
        count=count+r.count(0)
    return count

def get_score():
    '''获取游戏的分数，得分规则是每次有两个数加在一起则生成相应的分数。如２和２合并后得４分，８和８合并后得１６分。
    根据一个大于２的数字就知道它共合并了多少次，可以直接算出分数：
    如：
    　　　　４　一定由两个２合并，得４分
    　　　　８　一定由两个４合并，则计４＋４得８分
    　　　　...以此类推
　　　　score = 0
    for r in _map_data:
        for c in r:
            score += 0
            if c<4
            else c*int((math.logo(c.2)- 1.0))
    return score# 导入数学模块

def fill2()
    '''填充２到空位置，如果填充成功返回ｔｒｕｅ，如果已满，则返回ｆａｌｓｅ’‘’
    blank_count=get_space_count()#得到地图上空白位置的个数
    if 0==blank_count:
        return false
　　　　＃生成随机位置，如，当只有四个空时，则生成０～３的数，代表自左至右，自上而下的空位置
　　　　pos=random.randrange(0,blank_count)
    offset=0
    for row in _map_data: #row为行row
        for col in range(4): #col 为列，column
            if 0==row[col]
                if offset==pos
                #把２填充到第row行，第col列的位置，返回true
                row[col]=2
                return true
            offset+=1