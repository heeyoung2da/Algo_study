x, y = map(int, input().split())

s = 0
e = 1000000000
z = int(y*100 / x)
if z>= 99:
    ans = -1

else:
    ans = int(1e9)
    while s<=e:
        mid = (s+e)//2

        #로직처리
        nz = int((y+mid)*100 /(x+mid))

        if z < nz:
            e = mid - 1
        else:
            s = mid + 1

if ans == -1:
    print(ans)
else:
    print(s)
