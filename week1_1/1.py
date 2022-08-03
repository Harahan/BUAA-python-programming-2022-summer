n = int(input())
c = '\\' if n % 2 == 1 else '\"'
for i in range(n):
	for j in range(n - i - 1):
		print(" ", end="")
	for k in range(i + 1):
		print(c, end="")
	print()
