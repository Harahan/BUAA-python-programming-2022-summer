s = input()
sl = []
for c in s:
	sl.append(c)
p = input()
pl = []
for c in p:
	pl.append(c)
sk = []
ans = 0
while sl and pl:
	for i in range(2):
		tl = sl if i == 0 else pl
		a = tl.pop(0)
		if a in sk:
			sk, bl = sk[:sk.index(a)], sk[sk.index(a):]
			tl += bl
			tl.append(a)
		else:
			sk.append(a)
		if not tl:
			ans = 1 if tl == sl else 2
			break

if ans == 2:
	print("Hahaha~")
else:
	print("Oh, no!")
	sl = pl
for s in sl:
	print(s, end="")
	
	
		




