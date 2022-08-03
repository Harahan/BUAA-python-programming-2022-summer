n = int(input())
s1 = list(input())
s2 = list(input())
s1.reverse()
s2.reverse()
ans, i, car = '', 0, 0
while i < min(len(s1), len(s2)):
	ans += str((int(s1[i]) + int(s2[i]) + car) % n)
	car = (int(s1[i]) + int(s2[i]) + car) // n
	i += 1
s3 = s1 if i < len(s1) else s2
while i < len(s3):
	ans += str((int(s3[i]) + car) % n)
	car = (int(s3[i]) + car) // n
	i += 1
if car != 0:
	ans += str(car)
ans_list = list(ans)
ans_list.reverse()
for i in ans_list:
	print(i, end="")
	