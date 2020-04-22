import requests
from bs4 import BeautifulSoup

a=25
url='https://movie.douban.com/top250'
headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36'}
response=requests.get(url,headers=headers)
html=response.text
soup=BeautifulSoup(html,'html.parser')
soup_ol=soup.find('ol',class_='grid_view')
soup_li=soup_ol.find_all('li')
name=[]  #电影名
number=1 #电影排名
for item in soup_li:  #爬取第一个页面（1-25）
    soup_movie_hd=item.find('div',class_='hd')
    soup_movie_name=soup_movie_hd.find('span',class_='title').get_text()
    name.append(soup_movie_name)
for item_1 in range(1,10,1): #爬取后99个页面
    url = 'https://movie.douban.com/top250'+'?start=%d&filter='%a
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36'}
    response = requests.get(url, headers=headers)
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')
    soup_ol = soup.find('ol', class_='grid_view')
    soup_li = soup_ol.find_all('li')
    for item in soup_li:
        soup_movie_hd = item.find('div', class_='hd')
        soup_movie_name = soup_movie_hd.find('span', class_='title').get_text()
        name.append(soup_movie_name)
    a += 25
with open('豆瓣TOP250名单.txt', 'w') as f:  #输出到一个txt文档
        f.write('豆瓣TOP250名单\n')
        for item in name:
            name_final = '%d、%s\n' % (number,item)
            f.write( name_final)
            number+=1


