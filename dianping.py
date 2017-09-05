import urllib
from urllib.request import urlopen

import requests
from bs4 import BeautifulSoup


def get_info(dp_url):

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
        'Accept': 'text/html;q=0.9,*/*;q=0.8',
        'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
        'Accept-Encoding': 'gzip',
        'Connection': 'close',
        'Referer': 'http://www.baidu.com/link?url=_andhfsjjjKRgEWkj7i9cFmYYGsisrnm2A-TN3XZDQXxvGsM9k9ZZSnikW2Yds4s&amp;wd=&amp;eqid=c3435a7d00006bd600000003582bfd1f'
    }

    #dp_url = 'https://hz.lianjia.com/ershoufang/'
    dp_r = requests.get(url=dp_url, headers=headers)
    dp_html = dp_r.content
    dp = BeautifulSoup(dp_html, 'html.parser')
    dp_class = dp.find_all('div', attrs={'class': 'tit'})
    dp_a = dp_class('a')
    print(dp_a)
    #dp_href = dp_a.get('href')
    #dp_title = dp_a.get('title')
    #print(dp_href)
    #print(dp_title)
    #dp_num = dp_num_ct.span.string.strip()
    #dp_hs.write(dp_num + ' ')
    #dp_hs.close()

    #print(dp_num)

url_head = 'https://www.dianping.com/search/keyword/3/0_'
url_code = urllib.parse.quote('孩儿巷220号')
dp_url = url_head + url_code
#html = urllib.request.urlopen(dp_url)
#print(html)
print(dp_url)
get_info(dp_url)

