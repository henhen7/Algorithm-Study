#2798
n,m=map(int,input().split())
l=list(map(int,input().split()))
s=0
for i in range(0,n-2):
    for j in range(i+1,n-1):
        for k in range(j+1,n):
            r=l[i]+l[j]+l[k]
            if m>=r and r>s:
                s=r
print(s)