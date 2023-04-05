a,_=map(int,input().split())
b=[*map(int,input().split())]
print(sum(((0 if i else a)+b[i]-b[i-1]-2)//2 for i in range(len(b))))
