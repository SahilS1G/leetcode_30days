"""
Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.

 

Example 1:

Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.


Example 2:

Input: height = [4,2,0,3,2,5]
Output: 9

Constraints:

n == height.length
1 <= n <= 2 * 104
0 <= height[i] <= 105

"""

# def water():
#         height = [0,1,0,2,1,0,1,3,2,1,2,1]
#         # height = [4,2,0,3,2,5]
#         # height = [4,2,0,3,2,5]
#         count = 0
#         for i in range(len(height)):
#             if i+1 != len(height):
#                 if height[i] > height[i+1]:
#                     count += height[i] - height[i+1]
#                     # for m in range(i+2,len(height)):
#                     #     if (height[i]<=height[m]):
#                     #         continue
#                     #     else:
                        
#                     #         for j in range(i+1,len(height)):
#                     #             if height[j] < height[i] :
#                     #                 count += height[i] - height[j]
#                     #             else:
#                     #                break
#                     #         break
#         print(count)
        
# water()

def water2():
        height = [0,1,0,2,1,0,1,3,2,1,2,1]
        # height = [4,2,0,3,2,5]
        # height = [4,2,3]
        # height = [0,7,1,4,6]
        
        i = 0
        count = 0
        while (i < len(height)):
            if i+1 != len(height):
                green = 0
                pride = 0
                if height[i] >= height[i+1]:
                    for j in range(i+1,len(height)):
                        if (height[i]<=height[j]):
                            green += 1
                            break
                    if green == 0:
                        i+=1
                        continue
                    for j in range(i+1,len(height)):
                        if height[j] < height[i] :
                            count += height[i] - height[j]
                            pride += 1
                        else:
                            break
                    i += pride
                elif (i!=0 and height[i]< height[i+1] and height[i]<height[i-1]):
                    if height[i-1]>height[i+1]:
                        count+= height[i+1] - height[i]
                    else:
                        count+= height[i-1] - height[i]
            i += 1
        print(count)
                    
water2()


def trap():
        height = [0,1,0,2,1,0,1,3,2,1,2,1]
        # height = [4,2,0,3,2,5]
        # height = [4,2,3]
        # height = [0,7,1,4,6]
        total_water = 0
        left_wall = 0
        right_wall = len(height) -1
        max_left_wall = 0
        max_right_wall = 0
        while left_wall < right_wall:
            if height[left_wall] <= height[right_wall]:
                if height[left_wall] >= max_left_wall:
                    max_left_wall = height[left_wall]
                else:
                    total_water += max_left_wall - height[left_wall]
                left_wall +=1
            else:
                if height[right_wall] >= max_right_wall:
                    max_right_wall = height[right_wall]
                else:
                    total_water += max_right_wall - height[right_wall]
                right_wall -=1
        print(total_water)
    
trap()