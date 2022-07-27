#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/7/11 14:55
# @Author  : Smaller

import requests
import re
from bs4 import BeautifulSoup
from itertools import chain
import time
import csv

findbrand = re.compile(r'<h3><a href="/pic/brand-(.*?).html"')
findid = re.compile(r'((?<=__).+)(.+(?=.jpg))')


# 1.创建一个访问网页的函数
def askurl(url):
    headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36 QIHU 360SE"
    }
    html = requests.get(url, headers=headers)
    return html.text

# 2.先获取到车型库
def getcars():
    brands = []  # 存放获得的brand值
    html = askurl(
        'https://car.autohome.com.cn/AsLeftMenu/As_LeftListNew.ashx?typeId=2%20&brandId=0%20&fctId=0%20&seriesId=0')
    soup = BeautifulSoup(html, 'html.parser')
    for item in soup:
        item = str(item)
        brand = re.findall(findbrand, item)
        # print(brand)
        brands.append(brand)
    brandlist = []  # 清洗brand列表
    brandlist = [ele for ele in brands if ele != []]  # 删除空数组
    brandlist = list(chain.from_iterable(brandlist))  # 合并小列表
    # print(brandlist)

    # https: // car.autohome.com.cn / pic / brand - 524.html
    brandlinks = [] #存放链接值
    for i in brandlist:
        u = 'https://car.autohome.com.cn/pic/brand-' + str(i) + '.html'
        brandlinks.append(u)
        # print(brandlinks)

    time.sleep(3)

    for u in brandlinks:  #
        brand_last = []
        # print(u)
        html = askurl(u)
        soup = BeautifulSoup(html, 'html.parser')
        title_div = soup.find('div', class_='cartab-title')
        title = title_div.find('a').text
        brand_last.append(title)
        div = soup.find('div',class_ = 'uibox')
        lis = div.find_all('li')
        for li in lis:
            img = li.find('img')
            img_url = img.get('src')
            img_id = findid.findall(img_url)
            if img_id:
                brand_last.append(img_id[0][0])
        save_csv(brand_last)
        print(brand_last)


def save_csv(brand_last):
        with open('predict.csv', mode='a', newline='',encoding='utf-8-sig') as predict_file:
            csv_writer = csv.writer(predict_file)
            for row in brand_last:
                csv_writer.writerow([row])


# 3.运行代码
def main():
    getcars()

# 4.主程序
if __name__ == '__main__':
    main()
