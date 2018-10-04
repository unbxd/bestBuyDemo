import csv
import re
import urllib
import urllib2
import time
''''''

def cleanShitUp ():
	f=open('gogoFeed.json','w')
	f.write('{\"feed\":{\"catalog\":{\"add\":{\"items\":[')
	f.close()

def facetMaker(test_str):
	regex = r"<li\b[^>]*>(.*?)</li>"
	matches = re.finditer(regex, test_str[31], re.MULTILINE)
	output=""
	if test_str[3]=='Color':
		output+=('\"color\":\"'+test_str[4]+'\",')
	for match in matches:
		'''print (match).group(1) '''
		facet=match.group(1).split(':')
		if len(facet)==2:
			if facet[0]=='Color':
				output+=('\"color\":\"'+facet[1]+'\",')
			elif facet[0]=='Voltage':
				output+=('\"voltage\":\"'+facet[1]+'\",')
			elif facet[0]=='Capacity':
				output+=('\"capacity\":\"'+facet[1]+'\",')
			elif facet[0]=='Composition':
				output+=('\"composition\":\"'+facet[1]+'\",')
			elif facet[0]=='Dimensions':
				dimensions=facet[1].split('x')
				try:
					output+=('\"length\":\"'+dimensions[0].replace('\"',"in.").replace('L','').replace('\t','')+'\",')
					output+=('\"width\":\"'+dimensions[1].replace('\"',"in.").replace('W','').replace('\t','')+'\",')
					output+=('\"height\":\"'+dimensions[2].replace('\"',"in.").replace('H','').replace('\t','')+'\",')
				except:
					print('***shit***')

	return output

def getImage(url):
	'''url = 'https://norelco.factoryoutletstore.com/details/114524/norelco-jc302.html'''
	user_agent = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64)'
	values = {'name': 'Shawarma',
	          'location': 'Northampton',
	          'language': 'Python' }
	headers = {'User-Agent': user_agent}
	data = urllib.urlencode(values)
	req = urllib2.Request(url)
	try:
		response = urllib2.urlopen(req)
		the_page = response.read()
		q=re.compile('www.*images.*\.(jpg|JPG)')
		if q.search(the_page):
			imgUrl="https://"+q.search(the_page).group()
			return imgUrl
		else:
			time.sleep(1)
			print ('error in url:',url)
			imgUrl= '******Shit*****'
			'''imgUrl="https://"+q.search(the_page).group()'''
			
			return imgUrl
	except:
		return "URL ERROR"

		
with open('unboxd_sample.tsv') as tsvfile:
  counter=0
  cleanShitUp()
  reader = csv.reader(tsvfile, delimiter='\t')
  for row in reader:
  	
    p=re.compile('<span class=\"prod_name\"[^<>]*>(.*?)<\/span>')
    if p.search(row[5]):
    	feedJson=""
    	f=open('gogoFeed.json','a')
    	feedJson+="{\"uniqueId\":\""+row[0]+"\","
    	'''Title derived from feild: main_id'''
    	titleFind = p.search(row[5]).group(1);
    	titleFind = titleFind.replace ('\"',"in")
    	titleFind = titleFind.replace ('\'',"ft")
    	titleFind = titleFind.replace ('\t','')
    	feedJson+="\"title\":\""+titleFind+"\","
    	'''Catgeory Path derived from field: lineage'''
    	catPath = row[56]
    	feedJson+="\"categoryPath\":\""+catPath+"\","
    	'''URL derived from field: brand+ conatiner_id +ssdKeywords'''
    	url="https://www.factoryoutletstore.com/details/"+row[24]+"/"+row[23]+".html"
    	feedJson+="\"productUrl\":\""+url+"\","
    	'''image URL derived by function which calls url above, fetches pages and parses out default image '''
    	print ('line complete:',counter,url)
    	feedJson+="\"imageUrl\":\""+getImage(url)+"\","
    	''' Adding Facets'''
    	feedJson+=facetMaker(row)
    	''' Adding Brand '''
    	feedJson+="\"brand\":\""+row[53]+"\","
    	feedJson+="\"brand_name\":\""+row [15].replace ('\"',"in").replace ('\'',"ft").replace ('\t','')+"\","
    	'''Add Price and close the set '''
    	feedJson+="\"price\":"+row[39]+"},"
    	f.write (feedJson)
    	f.close()
    	counter+=1

f=open('gogoFeed.json','r')
feedJson=f.read()[0:-1]+"]}}}}"
f.close()
f=open('gogoFeed.json','w')
f.write (feedJson)
f.close()