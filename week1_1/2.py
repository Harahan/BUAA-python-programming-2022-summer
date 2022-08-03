import math

a = list(map(float, input().split()))
b = list(map(float, input().split()))
c = list(map(float, input().split()))


def x(ai: list, bi: list) -> float:
	return math.sqrt((ai[0] - bi[0]) ** 2 + (ai[1] - bi[1]) ** 2)


print("%.2f" % (x(a, b) + x(a, c) + x(b, c)))
