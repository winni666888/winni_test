#爬取西安58同城的测试工程师招聘信息
#   引入库
import requests
from lxml import etree
import csv
import time
import random
# from pip._vendor.msgpack.fallback import newlist_hint
#定义抓取函数
def spider():
    headers ={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3514.0 Safari/537.36'}
    prefix_url = 'https://xa.58.com/ruanjiangong/pn'
    for i in range(1,6):
    #  拼接成完整的url
        url= prefix_url+str (i)
    #  请求页面
        html = requests.get(url,headers = headers)
        time.sleep(2)
        #print(html.text())             没有输出来东西
        #获取selector
        selector = etree.HTML(html.text)
        # 获取工作列表
        job_list = selector.xpath('//*[@id="list_con"]/li')
        #print(job_list)
        for job in job_list:
            name = job.xpath('div[1]/div[1]/a/span[2]/text()')[0]
            price = job.xpath('div[1]/p/text()')[0]
            address = job.xpath('div[2]/div/a/text()')[0]
            print(name,price,address)
            # 保存数据
            item = [name,price,address]
            data_write(item)
         #休息2-3秒
            time.sleep(random.randint(2,3))
#定义保存函数
def data_write(item):
     with open('job.csv','a',encoding='utf-8',newline = '')as file:
         writer = csv.writer(file)
         writer.writerow(item)
if __name__ == '__main__' :
    spider()