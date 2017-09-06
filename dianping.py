import re
import urllib
from urllib.request import urlopen

import requests
from bs4 import BeautifulSoup
from pyexcel_xls import get_data
from pyexcel_xls import save_data
from collections import OrderedDict


def bs4_url(url):

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
        'Accept': 'text/html;q=0.9,*/*;q=0.8',
        'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
        'Accept-Encoding': 'gzip',
        'Connection': 'close',
        'Referer': 'http://www.baidu.com/link?url=_andhfsjjjKRgEWkj7i9cFmYYGsisrnm2A-TN3XZDQXxvGsM9k9ZZSnikW2Yds4s&amp;wd=&amp;eqid=c3435a7d00006bd600000003582bfd1f'
    }

    req = requests.get(url=url, headers=headers)
    html = req.content
    url_cnt = BeautifulSoup(html, 'html.parser')
    return url_cnt

def dp_pro(dp_url):
    tit = {}
    dp = bs4_url(dp_url)
    dp_tit = dp.find_all('div', attrs={'class': 'tit'})
    for tit_item in dp_tit:
        tit_a = tit_item.find_all('a', attrs={'data-hippo-type' : 'shop'})
        for tit_a_item in tit_a:
            #print(tit_a_item.get('href'))
            #print(tit_a_item.get('title'))
            href  = tit_a_item.get('href')
            title = tit_a_item.get('title')
            tit[title] = href
    print(tit)


    dp_tag = dp.find_all('div', attrs={'class': 'tag-addr'})
    for tag_item in dp_tag:
        tag_a = tag_item.find_all('span', attrs={'class':'addr'})
        #print(tag_a)
        addr = tag_a[0].get_text()
        print(addr)

def rd_exl():
    xls_data = get_data(r'./test.xlsx')
    for sheet_n in xls_data.keys():
        print(sheet_n, ':', xls_data[sheet_n])

#rd_exl()

def wr_exl(title, addr, href):
    data = OrderedDict()
    sheet_1 = []
    row_1_data = [u'店名', u'地址', u'链接']
    row_2_data = [4,5,6]
    sheet_1.append(row_1_data)
    sheet_1.append(row_2_data)
    data.update({u'sheet1':sheet_1})
    save_data('./wr_test.xls', data)


#wr_exl()





url_head = 'https://www.dianping.com/search/keyword/3/0_'
url_code = urllib.parse.quote('孩儿巷220号')
dp_url = url_head + url_code
#html = urllib.request.urlopen(dp_url)
#print(html)
#print(dp_url)
#addr_chn = u'孩儿巷220号'
#addr_utf = addr_chn.encode('gbk')
#get_info(dp_url)
dp_pro(dp_url)

