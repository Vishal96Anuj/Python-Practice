#!/usr/bin/python3

# python program for download you tube videos

import sys
from pytube import YouTube

URL=sys.argv[1]

def display_streams(URL):
	print("Given You Tube Video's URL is : ",URL)
	yt=YouTube(URL)
	print("Title is : ",yt.title)
	print("Author is : ",yt.author)
	sec=int(yt.length/60)
	print("Video length is : {} Minutes".format(sec))
	print("Rating is : ",round(yt.rating,1))
	print("Views are : ",yt.views)
	#yt.streams.get_highest_resolution().download()
	#print("Download Completed & saved at location : ",pwd+"/"+yt.title)

display_streams(URL)

