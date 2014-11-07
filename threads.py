from threading import Thread
import urllib
import re
import MySQLdb

login_info = open("threads/login.txt").read()
login_info = login_info.split()

host = login_info[0]
user = login_info[1]
password = ""
# password = login_info[2]

# conn = MySQLdb.connect(host=host, user=user, passwd=password, db="stock_data")
# conn = MySQLdb.connect(host=host, user=user, db="stock_data")
conn = MySQLdb.connect(host="localhost", user="root", passwd="", db="stock_data")

def th(ur):
    regex = "<title>.+?</title>"
    pattern = re.compile(regex)
    htmltext = urllib.urlopen(ur).read()
    # print "------" + ur
    print re.findall(pattern, htmltext)
    # print htmltext[0:100]

urls = "http://cnn.com http://google.com http://yahoo.com http://wikipedia.com".split()

threadlist = []

for u in urls:
    t = Thread(target = th, args = (u, ))
    t.start()
    threadlist.append(t)

for b in threadlist:
    b.join()