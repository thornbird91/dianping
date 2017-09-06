import re
import urllib
from urllib.request import urlopen

import requests
from bs4 import BeautifulSoup


def get_info(dp_url, addr_utf):

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
    dp_tit = dp.find_all('div', attrs={'class': 'tit'})
    for tit_item in dp_tit:
        tit_a = tit_item.find_all('a', attrs={'data-hippo-type' : 'shop'})
        for tit_a_item in tit_a:
            #print(tit_a_item.get('href'))
            print(tit_a_item.get('title'))

    dp_tag = dp.find_all('div', attrs={'class': 'tag-addr'})
    for tag_item in dp_tag:
        tag_a = tag_item.find_all('span', attrs={'class':'addr'})
        #print(tag_a)
        addr = tag_a[0].get_text()
        addr_sp = addr.split('-')[0]
        print(addr_sp)
        addr_ser = addr_sp.encode('utf8')
        if re.search(addr_utf, addr_ser):
            print('pass')
        else:
            print('fail')
            print(addr_ser)






    #dp_num = dp_num_ct.span.string.strip()
    #dp_hs.write(dp_num + ' ')
    #dp_hs.close()

    #print(dp_num)

url_head = 'https://www.dianping.com/search/keyword/3/0_'
url_code = urllib.parse.quote('孩儿巷220号')
dp_url = url_head + url_code
#html = urllib.request.urlopen(dp_url)
#print(html)
#print(dp_url)
addr_chn = u'孩儿巷220号'
addr_utf = addr_chn.encode('gbk')
print(filter(str.isdigit, addr_utf))
#get_info(dp_url, addr_utf)

