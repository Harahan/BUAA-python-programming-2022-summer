n, m = map(int, input().split())
k = int(input())

if n * 60 + m + k > 23 * 60 + 30:
	print("23:30")
else:
	print("%02d:" % ((n * 60 + m + k) // 60) + "%02d" % ((n * 60 + m + k) % 60))
