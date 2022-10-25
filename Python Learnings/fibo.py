#using recorsion
def fibo(n):
    if n==1 or n==0:
        return n
    
    return fibo(n-1)+ fibo(n-2)
def fib(n):
    a = 0
    b=1
    sum  = 0
    for i in range(n):
        sum = a+b
        a = b
        b = sum
    return sum

print(fib(1))
print(fibo(6))
