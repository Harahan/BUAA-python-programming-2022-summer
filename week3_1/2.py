M, N, T = list(map(int, input().split()))
ok = [_ for _ in range(1, M + 1)]
for i in range(1, M * T + 1):
	p = i % M if i % M != 0 else M
	if (i % N == 0 or str(N) in str(i)) and p in ok:
		ok.remove(p)
if not ok:
	print("NO")
else:
	for i in ok:
		print(i, end=" ")
		
