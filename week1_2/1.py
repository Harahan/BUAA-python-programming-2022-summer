mat = []
for i in range(3):
	t = list(map(int, input().split()))
	mat.append(t)


def cal(mi: int, mj: int):
	return mat[1][mi] * mat[2][mj] - mat[1][mj] * mat[2][mi]


print(mat[0][0] * cal(1, 2) - mat[0][1] * cal(0, 2) + mat[0][2] * cal(0, 1))
