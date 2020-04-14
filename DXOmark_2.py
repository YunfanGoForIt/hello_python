# coding=utf-8
import requests
from bs4 import BeautifulSoup
url='https://www.dxomark.com/cn/category/smartphone-reviews'
headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36'}
response=requests.get(url,headers=headers)
html=response.text
soup=BeautifulSoup(html,'html.parser')
soup_rankingList=soup.find('div',class_='rankingList')
soup_listElement=soup_rankingList.find_all('div',class_='listElement')
name=[]
for item in soup_listElement:
    soup_name=item.find('a').get_text()
    name.append(soup_name)
mark=[]
for item in soup_listElement:
    soup_mark=item.find('div',class_='deviceScore').get_text()
    mark.append(soup_mark)

number=1
with open('DXOmark.txt','w') as f:
    for item in name:
        f.write('%d、'%number+item+'           相机评分是%s'%mark[number]+'\n')
        number+=1

