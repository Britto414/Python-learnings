def convert(n):
    if n==0:
        return 0
    s=n%10
    if s==0:
        s=5
    return convert(n//10)*10+s


print(convert(43609))
