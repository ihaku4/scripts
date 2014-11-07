from threading import Thread
import urllib
import re
import MySQLdb


conn = MySQLdb.connect(host="localhost", user="root", passwd="", db="stock_data")
# query = "create table if not exists test_table(test_column int, is_deleted int)"
query = "insert into test_table(test_column) values(2345)"
# x = conn.cursor()
# x.execute(query)
conn.cursor().execute(query)
conn.commit()
# row = x.fetchall()
# print row