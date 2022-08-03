import re

s = input().replace("english", "English").split()
for i in range(len(s)):
	if ".." in s[i] and "..." not in s[i]:
		s[i] = s[i].replace("..", ".")
for i in range(len(s)):
	if re.search(r"\bu\b", s[i]) is not None:
		s[i] = s[i].replace("u", "you")
for i in range(len(s)):
	if s[i].islower() and (i - 1 < 0 or s[i - 1][len(s[i - 1]) - 1] in ".!?"):
		s[i] = s[i].title()
for p in s:
	print(p, end=" ")
	