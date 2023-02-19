elif (i!=0 and height[i]< height[i+1] and height[i]<height[i-1]):
                    if height[i-1]>height[i+1]:
                        count+= height[i+1] - height[i]
                    else:
                        count+= height[i-1] - height[i]