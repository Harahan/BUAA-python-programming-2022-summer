d = input().split()
d.sort()
essay = input().split()


def search(s: str) -> int:
	left, right, ans = 0, len(d) - 1, 0
	while left <= right:
		mid = (left + right) // 2
		if d[mid] <= s:
			left, ans = mid + 1, mid
		else:
			right = mid - 1
	return ans


for i in range(len(essay)):
	k = search(essay[i])
	if d[k] == essay[i]:
		continue
	else:
		essay[i] = d[k]
for t in essay:
	print(t, end=" ")


