'''def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        c = 
        a=b
        b=c
        print(a,b,c)
        return fibonacci(a,b,n-1)'''



def fibonacci(n):
    if n ==0:
        return 0
    if n==1:
        return 1
    return fibonacci(n-1)+fibonacci(n-2)

print(fibonacci(7))
