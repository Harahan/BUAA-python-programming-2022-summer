import datetime

arr = [7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2]
ans = [1, 0, "X", 9, 8, 7, 6, 5, 4, 3, 2, 1]


def cal(s):
	tag, _ = 0, 0
	for c in s:
		tag += int(c) * arr[_]
		_ += 1
	tag %= 11
	return ans[tag]


n = int(input())
tmp = list(map(int, input().split()))
initial = datetime.date(tmp[0] - 18, tmp[1], tmp[2])
x, y = 0, 0
for i in range(n):
	t = input()
	if str(cal(t[:-1])) != t[-1]:
		y += 1
	if datetime.date(int(t[6: 10]), int(t[10: 12]), int(t[12: 14])) <= initial:
		x += 1
print(x, y)
