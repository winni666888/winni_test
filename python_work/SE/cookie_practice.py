from selenium import webdriver
import time

print("start")
driver = webdriver.Firefox()
driver.get_cookies()
driver.get('https://www.51zxw.net/')
driver.get_cookies()
driver.delete_all_cookies()
driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div[2]/a').click()
driver.find_element_by_xpath('//*[@id="loginStr"]').send_keys('mwn666888@163.com')
driver.find_element_by_xpath('//*[@id="pwd"]').send_keys('mwnlyxsl199406')
driver.find_element_by_xpath('//*[@id="remberLogin"]').click()
driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div/form/div/div[5]/button').click()
time.sleep(3)
print(1)
print(driver.get_cookies())

print(1.5)
# 获取51自学网的cookie,,,,注意是单数cookie
print(driver.get_cookie(name='ASP.NET_SessionId'))

# 删除kookie
driver.delete_cookie(name='newsMember')
print(1.75)
print(driver.get_cookie(name='newsMember'))
# 刷新浏览器
driver.refresh()
print(2)
print(driver.get_cookies())

cookie={'name': 'ASP.NET_SessionId',
         'value': 'tey30au1d4uuhwx3lhos1a3x', 'path': '/',
         'domain': 'www.51zxw.net',
         'secure': False,
         'httpOnly': True}
driver.add_cookie(cookie)
time.sleep(3)
driver.refresh()

