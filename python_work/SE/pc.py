import requests
response = requests.get('https://www.baidu.com/img/bd_logo1.png')
with open('logo.png','wb') as logo:
    logo.write(response.content)

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3514.0 Safari/537.36'}
url = 'https://www.douban.com'
response = requests.get(url,headers=headers)

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3514.0 Safari/537.36'}
url = 'https://www.douban.com'
response = requests.get(url,headers=headers)



