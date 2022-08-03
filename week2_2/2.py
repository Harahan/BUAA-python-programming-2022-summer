d0, d1 = dict(), dict()
n = int(input())
for i in range(n):
	tmp = input().split()
	for name in tmp[1:]:
		d1[name] = tmp[0]
	d0[tmp[0]] = [0, 0, 0, 0]
m = int(input())
for i in range(m):
	tmp = input().split()
	c = d1.get(tmp[0])
	d0.get(c)[int(tmp[1])] += 1
	d0.get(c)[0] += 1
d2 = sorted(d0.items(), key=lambda x: (-x[1][1], x[0]))
for i in d2:
	print(i[0], i[1][1], i[1][2], i[1][3])
print("-----")
d3 = sorted(d0.items(), key=lambda x: (-x[1][0], x[0]))
for i in d3:
	print(i[0], i[1][1], i[1][2], i[1][3])

