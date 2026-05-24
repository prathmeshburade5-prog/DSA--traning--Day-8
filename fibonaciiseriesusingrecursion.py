def fibo(n):
    if n==1:
        return 1
    

    elif n==0:
        return 0
    else:
        return fibo(n-1)+fibo(n-2)
n=10
for i in range(n):    
    print (fibo(n),end=" ")