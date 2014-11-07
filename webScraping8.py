import urllib
import re
import json

symbolslist = open("googleprice/symbols.txt").read()
symbolslist = symbolslist.split("\n")

for symbol in symbolslist:
	myfile = open("googleprice/daily_prices/" + symbol + ".txt", "w+")
	myfile.close()

	htmltext = urllib.urlopen("http://www.bloomberg.com/markets/chart/data/1D/").read()
	print htmltext
	data = json.load(htmltext)
	datapoints = data["data_values"]

	myfile = open("googleprice/daily_prices/" + symbol + ".txt", "a")
	for point in datapoints:
		myfile.write(str(symbol + "," + str(point[0]) + "," + str(point[1] + "\n")))
	myfile.close()