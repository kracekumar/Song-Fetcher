#! /usr/bin/env python
import os
def change_name(arg,dirname,fnames):
	x=map(lambda x:os.rename(dirname+"/"+x,dirname+"/"+x.replace("TamilWire.com", "").replace("%20","")),filter(lambda x:x.endswith('.mp3') ,fnames))

os.path.walk(os.getcwd(),change_name,None)

