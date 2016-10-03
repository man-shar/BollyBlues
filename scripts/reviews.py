import requests
import pdb
from bs4 import BeautifulSoup
import requests
from requests.auth import HTTPProxyAuth
import pdb
import os
from HTMLParser import HTMLParser
import json
from StringIO import StringIO
import time
import string
import csv


base_url="https://www.omdbapi.com/?t="
extra_url="&y=&plot=short&r=json&tomatoes=true"
auth=HTTPProxyAuth("manas.sharma","jammingtheg")
output=open("reviews.csv","a")

#for i in range(1920,2016):
#	output.write(str(i)+",")
#output.write("\n")
#
for i in range(1995,2016):
	filename="{0}.csv".format(i)
	output.write(str(i)+",")
	print i
	with open(filename,"r") as file:
		data=csv.DictReader(file)
		for row in data:
			name=row["Title"]
			name=string.replace(name," ","+")
			#print name
			url=base_url+"{0}".format(name)+extra_url
			#print url
			try:
				r=requests.get(url,auth=auth)
				r.raise_for_status()
				response=json.loads(r.text)
				print name
				try:
					#print i
					rating=float(response["imdbRating"])
					#print i
					#print name
					print rating
					output.write(str(rating)+",")
				except:
					output.write(",")
			except:
				continue
	
	output.write("\n")

#name="Dhoom 2"
#name=string.replace(name," ","+")
#url=base_url+"{0}".format(name)+extra_url
#r=requests.get(url,auth=auth)
#r.raise_for_status()
#print name
#print url
#print r.url
#print r.json()
#json=json.loads(r.text)
#print json["imdb"]
