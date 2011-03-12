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
dir_content=[]
dir_content=os.listdir("songs")
y=[x for x in url.urls if x.endswith(".mp3")]
for all in y:
	if all not in dir_content:
		print "-"*50+"\n"+all+"is downloading"
		file=urllib2.urlopen(all).readlines()
		writing=open(all.rsplit('/')[-1],"w")
		writing.writelines(file)
		writing.close()
		dir_content.append(all)
		print "\n "+all+"Downloaded"
#os.system("wget '%s'"%(y[0]))
