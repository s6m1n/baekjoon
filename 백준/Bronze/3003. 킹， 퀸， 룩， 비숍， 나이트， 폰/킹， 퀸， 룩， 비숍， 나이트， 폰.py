l = list(map(int,input().split()))
a = [1,1,2,2,2,8]
for i in range(6):
  l[i] = a[i]-l[i]
print(*l)