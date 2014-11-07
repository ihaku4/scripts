import urllib
from bs4 import BeautifulSoup
import urlparse

# htmltext = urllib.urlopen("http://nytimes.com")
# htmltext = urllib.urlopen("http://sina.com")
htmltext = urllib.urlopen("http://bbs.hupu.com/f1")
# htmltext = urllib.urlopen("http://baidu.com").read()
# print htmltext
soup = BeautifulSoup(htmltext)

# for tag in soup.findAll('a', href=True):
for tag in soup.findAll('td'):
	print tag
	# print tag.keys()
	# if 'class' in tag.keys() and tag["class"] == "p_title":
	# 	print tag
	# 	raw = tag['href']
	# 	b1 = urlparse.urlparse(tag['href']).hostname
	# 	b2 = urlparse.urlparse(tag['href']).path
	# 	newurls = ""
	# 	print raw
	# 	print b1
	# 	print b2
	# 	print ""

for tag in soup.findAll('a', href=True):
	raw = tag['href']
	b1 = urlparse.urlparse(tag['href']).hostname
	b2 = urlparse.urlparse(tag['href']).path
	print str(b1)+str(b2)
