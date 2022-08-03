import math

n, d, s = int(input()), [], 2147483647
x0, y0 = list(map(int, input().split()))
for _ in range(n):
	d.append(list(map(int, input().split())))
vis = [False for _ in range(n)]


def dfs(x, y, t, res):
	global s
	if t == n:
		s = min(s, res + math.sqrt((x - x0)**2 + (y - y0)**2))
		return
	for i in range(n):
		if not vis[i]:
			vis[i] = True
			dfs(d[i][0], d[i][1], t + 1, res + math.sqrt((x - d[i][0])**2 + (y - d[i][1])**2))
			vis[i] = False
		
		
dfs(x0, y0, 0, 0)
print("%.2f" % s)

