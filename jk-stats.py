import requests
from bs4 import BeautifulSoup
res=requests.get("https://www.census2011.co.in/census/state/districtlist/jammu+and+kashmir.html")
bs=BeautifulSoup(res.content,"html.parser")
all=bs.find_all("tbody")
l=["Sno.","District","Population","Increase","Sex Ratio","Literacy","Density"]
lis=["Area","No. of Tehsils","No. of Blocks","No. of Panchayats"]
data=all[0].find_all("tr")
f=[]
for i in range(0,len(data)):
    if i==7 or i==15 or i==23:
        pass
    else:
        t=0
        d={}
        for item in data[i]:
            try:
                if item.text=="List":
                    pass
                else:
                    d[l[t]]=item.text
                    t+=1
            except:
                pass
        f.append(d)
import pandas
df=pandas.DataFrame(f)
print(df)
