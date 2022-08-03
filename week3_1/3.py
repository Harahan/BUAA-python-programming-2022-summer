n = int(input())
x = list(map(int, input().split()))
y = list(map(int, input().split()))
t, ans = 0, 0
for i in range(len(x)):
	t += x[i]
	ans += t * y[i]
print(ans)
