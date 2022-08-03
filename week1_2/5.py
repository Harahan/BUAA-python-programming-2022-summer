def div(x: int):
	for k in tp:
		if x % k != 0:
			return False
	return True


def get(x: int, st: list):
	st.reverse()
	ig = int(str(x) + "".join(st))
	if div(ig) and 10 <= ig <= 10 ** 8:
		ans.append(ig)


tp, ans = [], []
n = int(input())
for i in range(n):
	tp.append(int(input()))
for _ in range(1, 10005):
	get(_, list(str(_))[:-1])
	get(_, list(str(_)))
ans = sorted(ans)
if len(ans) == 0:
	print("None")
else:
	for i in ans:
		print(i)
		