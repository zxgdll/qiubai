#!/usr/bin/env python
#coding=utf-8
import urllib
import urllib2
import thread
import time
import re
#糗事百科spider
class qiubai:   
	#初始化方法和变量
	def __init__(self):
		self.pageindex=1;
		self.user_agent='Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/52.0.2743.116 Chrome/52.0.2743.116 Safari/537.36'
		self.header={'User-Agent':self.user_agent}
		#存放段子
		self.stories=[]
		self.enable=False
#获取codepage
	def getPage(self,pageindex):
		try:
			url='http://www.qiushibaike.com/hot/page/'+str(pageindex)
			request=urllib2.Request(url,headers=self.header)
			response=urllib2.urlopen(request)
			page=response.read().decode('utf-8')
			with open('test.html','w') as f:
				f.write(page.encode('utf-8'))
			return page
		except urllib2.URLError as e:
			if hasattr(e,"reason"):
				print(u'connect failed',e.reason)
			return None
#获取page中的item
	def getItem(self,pageindex):
		page=self.getPage(pageindex)
		if not page:
			print("fail load page!")
			return None
		pattern=re.compile(r'<div class="author clearfix">.*?<img.*?alt="(.*?)"/>.*?<div class="content">.*?<span>(.*?)</span>.*?</div>(.*?)<div class="stats".*?class="number">(.*?)</i>',re.S)
		items=re.findall(pattern,page)
		pagecomment=[]
		for item in items:
			haveImg=re.search("img",item[2])
			# if not haveImg:
			# 	repalceBR=re.compile('<br/>')
			# 	text=re.sub(repalceBR,"\n",item[1])
			# 	pagecomment.append([item[0].strip(),text.strip(),item[3].strip()])
			repalceBR=re.compile('<br/>')
			text=re.sub(repalceBR,"\n",item[1])
			pagecomment.append([item[0].strip(),text.strip(),item[3].strip()])
		return pagecomment
	def loadpage(self):
		# print('loadpage')
		if self.enable:
			if len(self.stories)<2:
				#获取新一页
				pagecomment=self.getItem(self.pageindex)
				#将该页的段子存放到全局list
				if pagecomment:
					self.stories.append(pagecomment)
					self.pageindex+=1
	def getOnecomment(self,pagecomment,pageindex):
		for comment in pagecomment:
			input=raw_input()
			self.loadpage()
			if input=="Q":
				self.enable=False
				return
			print(u'第%d页\t发布人：%s\t赞数：%s\n%s'%(pageindex,comment[0],comment[2],comment[1]))
	def start(self):
		print(u'读取段子中，按回车查看新段子，Q退出\n')
		self.enable=True
		self.loadpage()
		# print('start')
		nowpage=0
		while self.enable:
			if len(self.stories)>0:
				pagecomment=self.stories[0]
				nowpage+=1
				del self.stories[0]
				self.getOnecomment(pagecomment,nowpage)
spider=qiubai()
spider.start()				

