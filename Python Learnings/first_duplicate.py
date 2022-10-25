def duplicate():    
    s="abcba"
    hmap={}
    for i in s:
        if i in hmap:
            hmap[i]+=1
        else:
            hmap[i]=1
        if hmap[i]>1:
            return i
    
if __name__=="__main__":
    print(duplicate())
