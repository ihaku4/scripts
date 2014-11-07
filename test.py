# a = [11, 23, 45, 11]
# print a.count(11), a.count(22), a.count(23)
# a.append(77)
# a.append(88)
# print a
# a.pop()
# print a
# a.pop()
# print a

# from collections import deque
# a = [11, 23, 45, 11]
# q = deque(a)
# print q
# q.popleft()
# print q

# a = [11, 23, 45, 11]
# s = set(a)
# print s
# print 11 in s
# print 22 in s

import re
text = """fljdsajfldjtest
tesdsjfltext
tewsttextfdlsafjdl
lfjdsafl;ja"""
# result = re.search(r"test", "xxxxtest...")
# result = re.search(r"^.*text.*$", text, re.M)
result = re.findall(r"^.*text.*$", text, re.M)
print result
print dir(result)
# print result.group(0)

# ------------
base = "http://bbs.hupu.com/10205976"
subfix = ".html"
index = 1

import urllib

while (index < 9):
	if (index > 1):
		url = base + "-" + index + subfix 
	else:
		url = base + subfix
	# html = urllib.urlopen(url).read().decode("utf-8")
	html = urllib.urlopen(url).read()
	print html
	# pattern = "^.*.*$".decode("utf-8")
	# result = re.findall(pattern, html, re.M)
	# print result
