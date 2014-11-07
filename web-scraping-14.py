import urllib
from bs4 import BeautifulSoup
import urlparse
import mechanize

url = "http://abc.com"

br = mechanize.Browser()
br.open(url)
for link in br.links():
	print link
	print link.base_url
	print link.url
	newurl = urlparse.urljoin(link.base_url, link.url)
	print newurl
	print urlparse.urlparse(newurl).hostname
	b1 = urlparse.urlparse(newurl).hostname
	b2 = urlparse.urlparse(newurl).path
	print "http://" + b1 + b2

htmlfile = urllib.urlopen(url).read()
soup = BeautifulSoup(htmlfile)
for tag in soup.findAll('a', href=True):
	print tag['href']