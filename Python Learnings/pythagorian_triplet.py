def checkTriplet(a, n):
    a.sort()
    flag = False
    for i in range(0,len(a)-2):
        for j in range(i+1,len(a)-1):
            if (a[i]*a[i]+a[j]*a[j])**0.5 in a:
                flag=True
                break
        if flag==True:
            break
    return flag


if __name__=="__main__":
    a=[3, 2, 4, 6, 5]
    n=len(a)
    print(checkTriplet(a, n))