import sys
input = sys.stdin.readline
N,M = list(map(int,input().split()))
a=[]
b=[]
for n in range(N):
  a.append(list(map(int,input().split())))
for n in range(N):
  b.append(list(map(int,input().split())))
for n in range(N):
  for m in range(M):
    print(a[n][m]+b[n][m],end=' ')
    if m==M-1:
      print('')