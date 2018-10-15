import csv
import re
import urllib
import urllib2
import json
import time
import sys
reload(sys)
sys.setdefaultencoding('utf8')

def cleanShitUp ():
	f=open('bbFeed.json','w')
	f.write('{\"feed\":{\"catalog\":{\"add\":{\"items\":[')
	f.close()


def getImage(bbSku):
	url = ('https://api.bestbuy.com/v1/products/'+bbSku+'.json?apiKey=wpngmxnfm8rt5x7cwb9qn3d3')
	time.sleep(1)
	req = urllib2.Request(url)
	try:
		response = urllib2.urlopen(req)
		the_page = json.loads(response.read())
		return (the_page["image"])
	except:
		print(the_page["image"])
		return "http://didNotWork.com"

		
with open('Local_unbxd_products_info.csv') as csvfile:
	counter=0
	cleanShitUp()
	reader = csv.reader(csvfile)
	for row in reader:
		if (counter == 0):
			counter+=1
		else:
			feedJson=""
			f=open('bbFeed.json','a')
			'''Catgeory Path derived from field: lineage'''
			catPath = row[0].replace(',','>')
			feedJson+="{\"categoryPath\":"+json.dumps(catPath)+","
			'''SKU is unique ID'''
			feedJson+="\"uniqueId\":"+json.dumps(row[1])+","
			'''Title derived from field: title'''
			feedJson+="\"title\":"+json.dumps(row[2])+","
			''' Adding Brand '''
			feedJson+="\"brand\":"+json.dumps(row[3])+","
			'''Features Facet '''
			feedJson+="\"features\":"+json.dumps(row[4])+","
			'''Model Family '''
			feedJson+="\"modelFamily\":"+json.dumps(row[5])+","
			'''Model Number '''
			feedJson+="\"modelNumber\":"+json.dumps(row[6])+","
			'''Add Image '''
			imageUrl="https://img.bbystatic.com/BestBuy_US/images/products/"+row[1][0:4]+"/"+row[1]+"_sa.jpg"
			feedJson+="\"imgUrl\":"+json.dumps(imageUrl)+","
			print imageUrl
			'''Add Price and close the set '''
			if (row[7]):
				feedJson+="\"price\":"+row[7]+"},"
			else:
				feedJson+="\"price\":1.00},"
			f.write (feedJson)
			f.close()
			counter+=1

f=open('bbFeed.json','r')
feedJson=f.read()[0:-1]+"]}}}}"
f.close()
f=open('bbFeed.json','w')
f.write (feedJson)
f.close()