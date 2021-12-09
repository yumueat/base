a=input().split()
b=int(input())
n=0
for i in a:
    if int(i)<=b+30:
        n+=1
print(n)