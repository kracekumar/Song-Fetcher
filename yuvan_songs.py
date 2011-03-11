#! /usr/bin/env python
import urllib2
import os
import urllib
from sgmllib import SGMLParser
link=raw_input("Enter the URI:")
content=urllib2.urlopen(link)
source=content.read()
class URLLister(SGMLParser):
	def reset(self):
		SGMLParser.reset(self)
		self.urls=[]

	def start_a(self,attrs):
		href=[v for k,v in attrs if k=="href"]
		if href:
			self.urls.extend(href)
url=URLLister()
url.feed(source)
content.close()
url.close()
os.chdir("songs")
y=[x for x in url.urls if x.endswith(".mp3")]
for all in y:
	file=urllib2.urlopen(all).readlines()
	writing=open(all.rsplit('/')[-1],"w")
	writing.writelines(file)
	writing.close()
#os.system("wget '%s'"%(y[0]))
