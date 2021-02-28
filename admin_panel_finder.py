#!/usr/bin/env python2
#by: Ahmed Mohamed
#Admin Panel Finder v1.0

from urllib2 import Request, urlopen, URLError, HTTPError

def Space(Y):
	A = 0
	while A<=Y:
		print " ",
		A+=1


def findAdmin():
	o = open("link.txt","r");
	link = raw_input("Enter Site Name \n(ex : example.com or www.example.com ): ")
	print "\n\nAvilable links : \n"
	while True:
		sub_link = o.readline()
		if not sub_link:
			break
		req_link = "http://"+link+"/"+sub_link
		req = Request(req_link)
		try:
			response = urlopen(req)
		except HTTPError as e:
			continue
		except URLError as e:
			continue
		else:
			print "OK => ",req_link

def Credit():
	Space(9); print "#####################################"
	Space(9); print "#   +++ Admin Panel Finder v1.0 +++ #"
	Space(9); print "#     Script by Ahmed Mohamed...    #"
	Space(9); print "#    Bangladesh White Hat Hackers   #"
	Space(9); print "#####################################"

Credit()
findAdmin()
