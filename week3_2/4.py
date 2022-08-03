d = {"grape": 1, "cherry": 2, "orange": 3, "lemon": 4, "kiwifruit": 5, "tomato": 6, "peach": 7, "pineapple": 8,
	 "coconut": 9, "watermelon": 10, "WATERMELON": 11}
a, flag, ans = [], True, 0


n, m = list(map(int, input().split()))
for i in range(m):
	p = d[input()]
	if ans < 11 and flag:
		x = len(a) - 1
		if x >= 0 and p == a[x]:
			while x >= 0 and p == a[x]:
				a[x] += 1
				if x != len(a) - 1:
					del a[len(a) - 1]
				ans = max(ans, a[x])
				p, x = a[x], x - 1
		else:
			if len(a) < n:
				a.append(p)
				ans = max(ans, p)
			else:
				flag = False
		
if ans == 11 and flag:
	print("You win!")
else:
	print("You lose!")
b = list(d.keys())
for i in a:
	print(b[i - 1], end=" ")

