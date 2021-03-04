# -*- coding:utf-8 -*-
# 酷狗音乐下载器
# 作者：Eric
# pyinstaller -F KG_Downloader_v1_2.py

import requests
import re
import os
import time
import colortext as ct #把colortext.py复制到C:\Python37\Lib\site-packages\mylib目录下

class Downloader():
	def __init__(self):
		# 伪装成浏览器
		self.headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.146 Safari/537.36'}
		# 酷狗查询链接url，使用时需要传入要搜索的歌曲
		self.search_url = 'http://songsearch.kugou.com/song_search_v2?keyword={}&page=1&pagesize=30'
		# 获取指定hash值的歌曲详情页面，使用时要传入该歌曲的hash值，该hash值从搜索的结果中获取
		self.hash_url = 'http://www.kugou.com/yy/index.php?r=play/getdata&hash={}'
	def run(self, keyword):
		# 根据歌名搜索，获取所需的信息
		print('\n嗯嗯，让我帮你找一下......\n')
		res = requests.get(self.search_url.format(keyword), headers=self.headers)
		filehash = re.findall('"FileHash":"(.*?)"', res.text)
		songnames = re.findall('"FileName":"(.*?)"', res.text)
		
		# 选择要下载的歌曲
		selected = self.selectsongs(songnames)
		
		# 开始下载
		print('\n伙计，我要开始下载啦...\n')
		directory = './驴子最爱的歌'
		if not os.path.exists(directory):
				os.mkdir(directory)
		for n in selected:
			content = requests.get(self.hash_url.format(filehash[n]))
			songname = songnames[n]+'.mp3'
			#获取真实的下载地址
			url = re.findall('"play_url":"(.*?)"', content.text)[0]
			download_url = url.replace("\\", "")
			ct.printGreen('开始下载第 %d首歌...%s\n' % (n+1,songname))
			with open('{}/{}'.format(directory,songname), 'wb') as f:
				f.write(requests.get(download_url).content)
		print('\n伙计，你要的歌曲全部都下载好啦=^_^=\n')

	# 选择要下载的歌曲
	def selectsongs(self,songnames):
		ct.printGreen("-----------------------------------------------------\n\n")
		print("伙计，这是我帮你找到的所有歌曲：\n")
		for i in range(len(songnames)):
			ct.printSkyBlue("     %d---%s\n" %(i+1,songnames[i]))
		#获取要下载的歌曲
		ct.printGreen("-----------------------------------------------------\n\n")
		inputs = input("伙计，输入你想要下载的歌曲编号(如果有多个编号，中间用空格隔开)：")
		selected = inputs.split(" ");
		return list(int(x)-1 for x in selected)
		
if __name__ == '__main__':
	ct.printGreen('---------------酷狗音乐下载器  V1.1版----------------\n\n')
	ct.printGreen('--献给我的最铁伙计，愿你生活中每一天都是一首幸福的歌！\n')
	ct.printGreen('						--Eric\n\n')
	while True:
		ct.printGreen("-----------------------------------------------------\n\n")
		keyword = input('伙计，你想下载什么歌啊(输入n退出):')
		if(keyword[0]=='n'):
			ct.printGreen("\n再见，伙计，下次下歌再找我Y(^_^)Y\n")
			ct.printGreen("\n3秒后自动退出！Y(^_^)Y\n")
			time.sleep(3)
			break
		dl = Downloader()
		dl.run(keyword)