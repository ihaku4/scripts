
import urllib
baseUrl = "http://fun.coolshell.cn/n/"
path = "2014"

while (True):
	path = urllib.urlopen(baseUrl + path).read().decode("utf-8")
	print path