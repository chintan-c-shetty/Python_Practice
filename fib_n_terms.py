def fib_n(n:int)->int:
    prev,cur=0,1
    if n==0:
        return prev
    if n==1:
        return cur
    
    fibsum=1
    l=[prev,cur]
    for i in range(n-2):
        next=prev+cur
        l.append(next)
        fibsum+=next
        prev,cur=cur,next
    print(l)
    print(fibsum)
n=int(input("enter the term"))
s=fib_n(n)
print(s)