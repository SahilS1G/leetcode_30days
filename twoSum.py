def tsum():
        # nums = [2,7,11,15]
        nums = [3,2,4]
        target = 6
        nums2 = nums.copy()
        nums2.sort()
        arr = []
        arr2 = []
        l = 0
        r = len(nums) -1 
        while(l<r):
            sum = nums2[l] + nums2[r]
            if sum > target:
                r -= 1
            elif sum < target:
                l += 1
            else:
                arr.append(nums2[l])
                arr.append(nums2[r])
                break
        for i,a in enumerate(nums):
            if a in arr:
                arr2.append(i)
            
        print(arr2)
    
tsum()