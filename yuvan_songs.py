#! /usr/bin/env python
import urllib2
import os
import sys
from sgmllib import SGMLParser
import time
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
dir_name=link.split('/')[-1].split('.')[0]
dir_content=list(os.listdir(os.getcwd()))
if not dir_name in dir_content:
	ret_code=os.mkdir(dir_name)
os.chdir(dir_name)
dir_content=list(os.listdir(os.getcwd()))
y=[x for x in url.urls if x.endswith(".mp3")]
for all in y:
	name=all.rsplit('/')[-1]
	if not  dir_content.__contains__(name):
		print "-"*50+"\n"+name+" is downloading in "+dir_name
		read_start_time=time.time()
		file=urllib2.urlopen(all).readlines()
		read_end_time=time.time()
		writing=open(name,"w")
		writing.writelines(file)
		close_time=time.time()
		writing.close()
		dir_content.append(all)
		print "\n "+name+" took "+str((read_end_time -read_start_time)/60.0)+" minutes to read "+str((close_time - read_end_time)/60.0) +" minutes and to write to directory => "+dir_name
