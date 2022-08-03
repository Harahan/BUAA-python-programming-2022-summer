k, c = list(map(int, input().split()))
f, ans = [[0] * 101 for i in range(101)], 1 if k == 1 else 0
for i in range(c + 1):
	f[i][1] = 1
for i in range(2, 101):
	for j in range(2, i + 1):
		for r in range(1, min(i, c + 1)):
			f[i][j] += f[i - r][j - 1]
		if j >= k and i == 100:
			ans += f[i][j]
print(ans)


