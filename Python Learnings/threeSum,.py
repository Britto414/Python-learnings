nums = [-1,0,1,0]
def threeSum(nums: list[int]) -> list[list[int]]:
    res = []
    nums.sort()
    for i in range(len(nums)):
        if i>0 and nums[i-1]==nums[i]:
            continue
        if nums[i] > 0:
            break
        l,r = i+1 ,len(nums)-1
        while l<r:
            threesum = nums[i] + nums[l] + nums[r]
            if threesum > 0:
                r -= 1
            elif threesum < 0:
                l += 1
            else:
                res.append([nums[i], nums[l],nums[r]])
                
                while l<=r-1 and nums[l] == nums[l+1] :
                    l+=1
                l+=1
    return res
print(threeSum(nums))
