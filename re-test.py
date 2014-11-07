import re

m = re.match(r"(\w+) (\w+)", "Issac Newton, physicist")
print m
print m.group(0)
print m.group(1)
print m.group(2)
print m.group(1, 2)
