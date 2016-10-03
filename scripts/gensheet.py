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
import csv

genres={
        "Mythology":[0]*96,
        "Drama":[0]*96,
        "Social":[0]*96,
        "Family":[0]*96,
        "Crime":[0]*96,
        "Crime Thriller":[0]*96,
        "Thriller":[0]*96,
        "Mystery":[0]*96,
        "Devotional":[0]*96,
        "Action":[0]*96,
        "Fantasy":[0]*96,
        "Legend":[0]*96,
        "Biopic":[0]*96,
        "Comedy":[0]*96,
        "Costume":[0]*96,
        "Historical":[0]*96,
        "Romance":[0]*96,
        "Suspense":[0]*96,
        "Adventure":[0]*96,
        

}
ignore_genres=["Legend","Erotica","","Bollywood","Partition","World Cinema","Period","Sentiment","Dark","Film","Epic","Music","Patriotic","Sport","Sports","Remake","Adult","Experimental","Superhero","Road","Cult","Science","Dark","Film","Found","Footage","Political","Politics","Cricket","B-grade","Business","Erotic","Silent","Spy","Revolutionary","Short","Dacoit","Classic","Anthology","Double-role","Tragedy","Realism","realism","War","Dance","Muslim","Triangle","Reincarnation","National","triangle","Supernatural","Folk","Travel","Monster","Festival","Satire","Anthology","Documentary","Melodrama","True-life","Zombie","Espionage","Rom","Masala","Psychological","Spoof"]



for year in range(1920,2016):
    filename="{0}.csv".format(year)
    with open (filename,"rb") as file:
        data=csv.DictReader(file)
        for row in data:
            curr=row["Genre"].split(", ")
            if curr[0]!="":
                for i in range(0,len(curr)):
                    try:
                        genres[curr[i]][year-1920]+=1
                    except KeyError:
                        print year
                        print curr[i]
                        if curr[i] not in ignore_genres:
                            genres[curr[i]]=[0]*96
                            genres[curr[i]][year-1920]+=1
                    #print i

outfile=open("numbers.csv","wa")
outfile.write("Year,")
#print genres
print len(genres)

for key,value in genres.iteritems():
    outfile.write(key+",")
outfile.write("\n")
##
##print genres

for year in range(1920,2016):
    outfile.write(str(year)+",")
    for i,j in genres.iteritems():
        outfile.write(str(j[year-1920])+",")
    outfile.write("\n")