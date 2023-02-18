'''
Given an integer array nums of length n and an integer target, find three integers in nums such that the sum is closest to target.

Return the sum of the three integers.

You may assume that each input would have exactly one solution.

 

Example 1:

Input: nums = [-1,2,1,-4], target = 1
Output: 2
Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
Example 2:

Input: nums = [0,0,0], target = 1
Output: 0
Explanation: The sum that is closest to the target is 0. (0 + 0 + 0 = 0).
 

Constraints:

3 <= nums.length <= 500
-1000 <= nums[i] <= 1000
-104 <= target <= 104

'''

import math


def closest():
        nums = [-1,2,1,-4]
        # nums = [0,0,0]
        target = 1
        arr = []
        arr2 =[]
        nums.sort()
        for i,a in enumerate(nums):
            l = i +1
            r = len(nums)-1
            while l < r:
                threesum = a + nums[r] + nums[l]
                if threesum > target:
                    arr.append(threesum-target)
                    arr2.append(threesum)
                    r -= 1
                elif threesum < target:
                    arr.append(target-threesum)
                    arr2.append(threesum)
                    l += 1
                else:
                    return threesum
                    
        arr3 = arr.copy()
        arr3.sort()
        count = 0
        for i in range(len(arr)):
            if arr3[0] == arr[i]:
                count = i
                
        print(arr2[count])
        
closest()


# Method 2

def clost():
        nums = [0,0,0]
        target = 1
        nums.sort()
        closest = math.inf
        res = 0
        
        for ptr1 in range(len(nums)-2):
            cur_target = target - nums[ptr1]
            ptr2, ptr3 = ptr1+1, len(nums)-1
            while ptr3 - ptr2 > 0:
                s = nums[ptr2] + nums[ptr3]
                if abs(cur_target - s) < closest:
                    closest = abs(cur_target - s)
                    res = s + nums[ptr1]
                if cur_target < s:
                    ptr3 -= 1
                elif cur_target > s:
                    ptr2 += 1
                else:
                    # found the closest sum possible; target itself
                    return target
                
        print(res)
        
clost()
