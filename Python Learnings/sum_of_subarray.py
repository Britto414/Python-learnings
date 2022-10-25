a=[1,1,1,1,1,2,2]
sum=5
hmap={0:-1}
sum1=0
for i in range(len(a)):
  sum1+=a[i]
  if sum1-sum in hmap:
    print(hmap[sum1-sum]+1,i)
  else:
    hmap[sum1]=i
