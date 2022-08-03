m, mat = list(map(int, input().split())), []
for _ in range(m[0]):
	mat.append(list(map(int, input().split())))
f = [[1 for i in range(m[1])] for j in range(m[0])]


def dfs(x: int, y: int):
	if f[x][y] != 1:
		return f[x][y]
	if x - 1 >= 0 and mat[x - 1][y] < mat[x][y]:
		f[x][y] = max(f[x][y], dfs(x - 1, y) + 1)
	if y - 1 >= 0 and mat[x][y - 1] < mat[x][y]:
		f[x][y] = max(f[x][y], dfs(x, y - 1) + 1)
	if x + 1 < m[0] and mat[x + 1][y] < mat[x][y]:
		f[x][y] = max(f[x][y], dfs(x + 1, y) + 1)
	if y + 1 < m[1] and mat[x][y + 1] < mat[x][y]:
		f[x][y] = max(f[x][y], dfs(x, y + 1) + 1)
	return f[x][y]


tot = 1
for i in range(m[0]):
	for j in range(m[1]):
		tot = max(dfs(i, j), tot)
print(tot)
