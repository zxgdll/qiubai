#!/usr/bin/env python
#coding=utf-8
import urllib
import urllib2
import cookielib
import re
cookie=cookielib.MozillaCookieJar()
page=1
# pattern=r'''<div class="article block untagged mb15".*?<h2>(.*?)</h2>.*?</a>.*?<div.*?<div.*?<span>(.*?)</span>.*?<div class="thumb">.*?src="(.*?)".*?<div class="stats.*?
# class="number">(.*?)</i>'''
# pattern = re.compile(r'.*?title=.*?(.*?).*?(.*?).*?(.*?).*?.*?class="number">(.*?).*?class="number">(.*?)',re.S)
url='http://www.qiushibaike.com/hot/'+str(page)
user_agent='Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/52.0.2743.116 Chrome/52.0.2743.116 Safari/537.36'
headers={'User-Agent':user_agent}
name=[]
content=[]
num=[]
img_c=[]
img=[]
try:
	request=urllib2.Request(url,headers=headers)
	response=urllib2.urlopen(request)
	page=response.read().decode('utf-8')
	with open('s.html','w') as f1:
		f1.write(page.encode('utf-8'))
	print(page)
	print('#'*80)
	items=re.findall(r'<div class="author clearfix">.*?<img.*?alt="(.*?)"/>.*?<div class="content">.*?<span>(.*?)</span>.*?</div>(.*?)<div class="stats".*?class="number">(.*?)</i>',page,re.S)
	# items=re.findall(r'(?P.*?).*?(?P.*?).*?\s*(?P.*?)\s*\'(?P.*?) (?P.*?).*?(?P.*?)',page,re.S)
	print(len(items))
	for item in items:
		haveimg=re.search("img",item[2])
		if  haveimg:
			print(haveimg.group())
		name.append(item[0])
		content.append(item[1])
		num.append(item[3])

except urllib2.URLError as e:
	if hasattr(e,"code"):
		print(e.code)
	if hasattr(e,"reason"):
		print(e.reason)
for i in range(len(name)):
	print(name[i])
	print(content[i])
	print(num[i])
	print('#'*50)