# coding=utf-8

import urllib2
import urlparse
import re

htmltext = urllib2.urlopen("http://v2ex.com", timeout = 5).read()

#pattern = u'\\d.*?人在线'
#regex = re.compile(pattern, re.U)
#result = regex.match(htmltext)
#m = re.match(r".*\d.*?人在线.*", htmltext)
#m = re.match(r"^.*lang.*$", htmltext, re.I)
#m = re.search(r"lang", htmltext, re.M)
#m = re.match(r".*yyy.*", "xxx xxx yyy zzz")
#m = re.match(r"(\w+) (\w+)", "Issac Newton, physicist")
#print m

m = re.search(r"(\d+?)\s*人在线.*最高记录.*?(\d+)", htmltext, re.M)

if m:
  print m.group(1)
  print m.group(2)
else:
  print "[ERROR]fetch online data fail."


