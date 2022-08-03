import re

s = input()
t = input()
co = re.compile(t)
if not co.findall(s):
	print("False")
else:
	print(len(co.findall(s)))
	