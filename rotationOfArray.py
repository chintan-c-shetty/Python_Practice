def rotArray(a:list,k):
    n=len(a)
    res=[0]*n
    j=0
    for i in range(n):
         j=(i+k)%n
         res[j]=a[i]
    return res
s=int(input("enter the input size"))
a=[]
for i in range(s):
    ele=int(input())
    a.append(ele)
k=int(input("enter the shift num"))
result=rotArray(a,k)
print(result)
     

