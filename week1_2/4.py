def f(x: int):
	if x <= 1:
		return 1 if x == 0 else 3
	return (f(x - 2) + f(x - 1)) / (1.01 ** f(x - 1))


print("%.2f" % f(int(input())))
