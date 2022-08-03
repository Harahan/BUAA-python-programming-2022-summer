x, y = list(map(int, input().split()))
vr, vc, vl1, vl2, ans = [False for i in range(8)], [False for j in range(8)], [False for k in range(15)], \
						[False for m in range(15)], 0
vr[x - 1] = vc[y - 1] = vl1[y - x + 7] = vl2[x + y - 2] = True


# 0 - 14
# (-y - 7) = -x - t => t = y - x + 7
# -y = x - t => x + y

def dfs(ix: int):
	global ans
	if ix == x - 1:
		dfs(ix + 1)
	if ix > 7:
		ans += 1
		return
	for iy in range(8):
		if vr[ix] == vc[iy] == vl1[iy - ix + 7] == vl2[ix + iy] and vr[ix] is False:
			vr[ix] = vc[iy] = vl1[iy - ix + 7] = vl2[ix + iy] = True
			dfs(ix + 1)
			vr[ix] = vc[iy] = vl1[iy - ix + 7] = vl2[ix + iy] = False
			
			
dfs(0)
print(ans)
