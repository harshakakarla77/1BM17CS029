def Fib(n):
    a,b = 0,1
    for i in range(n):
        a,b = b, a+b
    return a


n=int(input("Enter n:"))    
for i in range(n):
    print(Fib(i))
