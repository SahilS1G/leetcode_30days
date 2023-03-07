def duplicate():
        nums = [0,0,1,1,1,2,2,3,3,4]
        
        count = 0
        i = 0
        while (i < len(nums)):
            if i!=len(nums)-1 and nums[i] == nums[i+1]:
                count += 1
                nums.pop(i)
                # i += 1
                continue
            
            i += 1
        
        print(len(nums))
        
# duplicate()
                
            
def dup():
      nums = [0,0,1,1,1,2,2,3,3,4]
      a = set(map(int, nums))
      print(len(a))

dup()
