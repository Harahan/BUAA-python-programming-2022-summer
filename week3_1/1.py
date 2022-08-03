ptr = input()
st = input()
ans, i = '', 0
while i < len(st):
	if i + len(ptr) <= len(st) and st[i: i + len(ptr)].upper() == ptr.upper():
		if i != 0 and ans[-1] != ' ':
			ans += ' '
		ans += st[i: i + len(ptr)]
		if i != len(st) - 1:
			ans += ' '
		i += len(ptr)
	else:
		ans += st[i]
		i += 1
print(ans)
