import urllib
import re

htmltext = urllib.urlopen("http://guji.artx.cn/Article/787.html").read()
# print htmltext
# m = re.search("\<.+?\>(.+?)\</.+?\>", htmltext)
m = re.findall("\<.+?\>(.+?)\</.+?\>", htmltext)
print m