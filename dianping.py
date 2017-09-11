import urllib
import requests
import time
from bs4 import BeautifulSoup
import xlwt


def bs4_url(url):

    #headers = {
    #    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
    #    'Accept': 'text/html;q=0.9,*/*;q=0.8',
    #    'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
    #    'Accept-Encoding': 'gzip',
    #    'Connection': 'close',
    #    'Referer': 'http://www.baidu.com/link?url=_andhfsjjjKRgEWkj7i9cFmYYGsisrnm2A-TN3XZDQXxvGsM9k9ZZSnikW2Yds4s&amp;wd=&amp;eqid=c3435a7d00006bd600000003582bfd1f'
    #}

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.101 Safari/537.36',
        'Accept': 'text/html, application/xhtml+xml, application/xml; q=0.9, image/webp, image/apng, */*; q=0.8',
        #'Accept': 'application/json, text/javascript',
        'Accept-Encoding': 'gzip, deflate',
        'Connection': 'keep-alive',
        'Refer': 'http://www.dianping.com/'
    }
    req = requests.get(url=url, headers=headers)
    html = req.content
    url_cnt = BeautifulSoup(html, 'html.parser')
    return url_cnt



def dp_pro(dp_url):
    txt1_wr = open('./tmp1.txt', 'w')
    txt2_wr = open('./tmp2.txt', 'w')
    dp = bs4_url(dp_url)
    dp_tit = dp.find_all('div', attrs={'class': 'tit'})
    for tit_item in dp_tit:
        tit_a = tit_item.find_all('a', attrs={'data-hippo-type' : 'shop'})
        for tit_a_item in tit_a:
            href  = tit_a_item.get('href')
            title = tit_a_item.get('title')
            #ele1 = title + '#' + href + '\n'
            #txt1_wr.write(ele1)
            #print(href)
            #time.sleep(1)


            href_info = bs4_url(href.encode('gbk'))

            href_tel = href_info.find_all('span', attrs={'itemprop': 'tel'})
            print(href_tel)
            print(href_info.find_all('title'))
            #href_val = href_info.find_all('div', attrs={'class': 'info-value'})
            #if len(href_tel):
            #    tel = href_tel[0].get_text()
            #    print(href_tel[0].get_text())
            #elif len(href_val):
            #    tel = href_val[0].get_text()
            #    print(href_val[0].get_text())
            #else:
            #    tel = 'None'
            #    print('Null')

            #ele1 = title+'#'+tel+'#'+href+'\n'
            #txt1_wr.write(ele1)


    dp_tag = dp.find_all('div', attrs={'class': 'tag-addr'})
    for tag_item in dp_tag:
        tag_a = tag_item.find_all('span', attrs={'class':'addr'})
        #print(tag_a)
        addr = tag_a[0].get_text()
        ele2 = addr + '\n'
        txt2_wr.write(ele2)

    txt1_wr.close()
    txt2_wr.close()

def generate_exl():

    f_exl = xlwt.Workbook()
    sheet1 = f_exl.add_sheet(u'sheet1', cell_overwrite_ok=True)
    txt1_rd = open('./tmp1.txt', 'r')
    txt2_rd = open('./tmp2.txt', 'r')

    line1 = txt1_rd.readlines()
    line2 = txt2_rd.readlines()
    for i in range(len(line1)):
        row1 = line1[i].split('#')[0]
        row2 = line1[i].split('#')[1]
        row3 = line2[i]
        sheet1.write(i,0,row1)
        sheet1.write(i,1,row2)
        sheet1.write(i,2,row3)
        exl_ele = [row1, row2, row3]
        #print(exl_ele)
    f_exl.save('test.xls')

def get_href(href):
    href_info = bs4_url(href)
    href_span = href_info.find_all('span', attrs={'itemprop': 'tel'})
    print(href_span)





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
#generate_exl()

