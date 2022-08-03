n = int(input())
new = [0] + list(map(int, input().split()))
w = [0] + list(map(int, input().split()))
fix = [0] + list(map(int, input().split()))
f = [[2147483647 for __ in range(n + 1)] for _ in range(n + 1)]
# f[y][used]
f[0][0] = 0

for i in range(1, n + 1):
	for j in range(1, i + 1):
		if j != 1:
			f[i][j] = f[i - 1][j - 1] + fix[j]
		f[i][1] = min(f[i - 1][j - 1] + new[i] - w[j - 1] + fix[1], f[i][1])
ans = 2147483647
for i in range(1, len(f[n])):
	ans = min(ans, f[n][i] - w[i])
print(ans)
