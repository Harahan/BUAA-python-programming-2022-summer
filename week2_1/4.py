n, d = int(input()), dict()
for i in range(n):
	# input()
	s = input().split()
	if s[0] == "1":
		d[s[1]] = int(s[2])
	elif s[0] == "2":
		if s[1] in d.keys():
			print("%04d" % d[s[1]])
		else:
			print("9999")
	else:
		tot = 0
		for j in d.keys():
			if d[j] <= int(s[2]):
				tot += 1
		print(tot)
		