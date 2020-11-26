import pandas as pd
from pandas import DataFrame,Series
import matplotlib.pyplot as plt
from os import walk
i=[]
n=0
n1=1
for a,b,c in walk('F:\\作业\\asn89-19-\\asn89-19'):
    for o in c:
        su=pd.read_table(str(a+'\\'+o),header=None,error_bad_lines=False)
        for q in su[0]:
            p=str(q);
            p=p.split(':',2)
            if len(p)!=1 and len(p[0])<=20:
                i.append(p[0])
            pass
    pass
pass
i=Series(i)
i=i.unique()
for t in i:
    su.loc[n,0]=t
    n=n+1
    pass
n=0
for a,b,c in walk('F:\\作业\\asn89-19-\\asn89-19'):
    for o in c:
        i1=[]
        su1=pd.read_table(str(a+'\\'+o),header=None,error_bad_lines=False)
        for q in su1[0]:
            p=str(q)
            i1.append(p)
            pass
        for o1 in i1:
            p1=str(o1)
            p1=p1.split(':',1)
            for o2 in i:
                if o2==p1[0] :
                    try:
                        su.loc[n,n1]=p1[1]
                    except IndexError:
                        break
                n=n+1
                pass
            n=0
            pass
        n1=n1+1
    pass
pass
su.to_excel("工作簿.xlsx")
