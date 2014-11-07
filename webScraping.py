import urllib
import re
import json
import bs4

# s = "https://www.google.com/finance?q=aapl"
# print s

# regex = '<span id="ref_[^.]*_l">(.+?)</span>'
# pattern = re.compile(regex)
# htmltext = urllib.urlopen(s).read()
# # price = pattern.match(htmltext)
# price = re.findall(pattern, htmltext)
# print price

htmlfile = urllib.urlopen("http://v2ex.com/api/members/show.json?id=50071")
data = json.load(htmlfile)
print data