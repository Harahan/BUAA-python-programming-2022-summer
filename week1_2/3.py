n = int(input())
a, b, c = [], [], []
for _ in range(n * 3):
	# input()
	l = input().split()
	s, t = l[0], l[1]
	if t == "Chinese":
		a.append(float(s))
	elif t == "Math":
		b.append(float(s))
	else:
		c.append(float(s))
print("%.2f" % (sum(a) / len(a)))
print("%.2f" % (sum(b) / len(b)))
print("%.2f" % (sum(c) / len(c)))
