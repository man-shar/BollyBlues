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


auth=HTTPProxyAuth("manas.sharma","jammingtheg")
#numfile=open("num.csv","ab+")
#for year in range(1941,1941):
#    numfile.write("{0}".format(year))

#numfile.write("\n")

for year in range(1966,1967):
    print year
    url="http://en.wikipedia.org/wiki/List_of_Bollywood_films_of_{0}".format(year)
    r=requests.get(url,auth=auth)
    #time.sleep(1)
    r.raise_for_status()
    filename="{0}.csv".format(year)
    datafile=open(filename,'ab+')
    soup=BeautifulSoup(r.text,"html.parser")
    #print soup
    tables=soup.findAll("table",class_="wikitable")
    current_table=tables[0]
    current_table_list=current_table.findAll("tr")
    #pdb.set_trace()
    header_fields=current_table_list[0].findAll("th")

    for j in range(0,len(header_fields)):
        str='"{0}",'.format(header_fields[j].text.encode("utf-8"))
        datafile.write(str)

    datafile.write("\n")
    count=0

    for i in range(0,len(tables)):
        current_table=tables[i]
        current_table_list=current_table.findAll("tr")

        for j in range(1,len(current_table_list)):
            current_line_fields=current_table_list[j].findAll("td")

            #if len(current_line_fields)==len(header_fields):

            for k in range(0,len(current_line_fields)):
                str='"{0}",'.format(current_line_fields[k].text.encode('utf-8'))
                datafile.write(str)
            datafile.write("\n")
            count+=1

    print count
    #numfile.write("{0},".format(count))
    #pdb.set_trace()
    datafile.close()

#numfile.close()
