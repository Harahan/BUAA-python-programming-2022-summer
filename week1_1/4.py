def gp(x: float):
	return 0 if 0 <= x < 60 else 4 - 3 * (100 - x) ** 2 / 1600


n, k, ans, tp = int(input()), [], 0, 0
for i in range(n):
	k.append(list(map(float, input().split())))
	tp += k[i][1] if k[i][1] >= 1 else 0
for i in range(n):
	if k[i][1] >= 1:
		ans += gp(k[i][0]) * k[i][1]
print("%.2f" % (ans / tp))

