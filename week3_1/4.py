a = ['H', 'HE', 'LI', 'BE', 'B', 'C', 'N', 'O', 'F', 'NE', 'NA', 'MG', 'AL', 'SI', 'P', 'S', 'CL', 'AR']


def dfs(si):
	if si == len(s):
		return True
	else:
		if s[si].upper() in a and dfs(si + 1):
			return True
		if s[si: si + 2].upper() in a and dfs(si + 2):
			return True
	return False


n = int(input())
for i in range(n):
	s = input()
	if dfs(0):
		print('Yes')
	else:
		print('No')
	