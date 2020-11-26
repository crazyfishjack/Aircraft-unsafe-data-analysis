import pandas as pd
from pandas import DataFrame,Series
import matplotlib.pyplot as plt
from os import walk
from pylab import *
font = {'family': 'Microsoft YaHei',  'weight': 'bold',  'size': '14'}
matplotlib.rc("font", family="Microsoft YaHei", weight="bold", size="7")
su=pd.read_excel("工作簿.xlsx")
i=["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
i1=[0,0,0,0,0,0,0]
for i2 in range(6586):
    try:
        p=str(su.loc[1,i2])
        p=p.split(" ")
        if p[0]=="Monday":
            i1[0]=i1[0]+1
        if p[0]=="Tuesday":
            i1[1]=i1[1]+1
        if p[0]=="Wednesday":
            i1[2]=i1[2]+1
        if p[0]=="Thursday":
            i1[3]=i1[3]+1
        if p[0]=="Friday":
            i1[4]=i1[4]+1
        if p[0]=="Saturday":
            i1[5]=i1[5]+1
        if p[0]=="Sunday":
            i1[6]=i1[6]+1
    except KeyError:
        continue
    pass
plt.title("飞机不安全事件发生统计")
plt.ylabel("次数")
plt.bar(i,i1,color='#87CEEB',edgecolor='#000000',linewidth=1)
plt.show()

