import urllib2
import urllib
import nltk
from bs4 import BeautifulSoup

def getR(q):
	q=urllib.urlencode({'q':q})
	reqst=urllib2.Request('https://www.google.com/search?client=ubuntu&channel=fs&'+q+'&ie=utf-8&oe=utf-8')
	reqst.add_header('User-agent','Mozilla/5.0 (X11; U; Linux i686; de-AT; rv:1.6) Gecko/20040115') # the key
	saved=urllib2.urlopen(reqst, timeout=100).read()
	soup=BeautifulSoup(saved)
	print 'RESULTS:'
	for i in soup.findAll("h3",attrs={'class':'r'}):
		print nltk.clean_html(str(i))
		link = i.find("a").get("href")[7:]
		print link[:len(link)-84]
	print 'Next Pages:'
	for i in soup.findAll("a",attrs={"class":'fl'}): print i.get("href")


getR("cryptomania") 
