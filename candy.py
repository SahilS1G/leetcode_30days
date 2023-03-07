
def candy():
        ratings = [1,2,87,87,87,2,1]
        # ratings = [1,2,2]
        count = 0 
        i = 0
        while (i < len(ratings)):
            if i == 0 and ratings[i] < ratings[i+1]:
                count += 1
                i += 1
                continue
            elif i == 0 and ratings[i] > ratings[i+1]:
                count += 2
                i+=1
                continue
            elif i == 0 and ratings[i] == ratings[i+1]:
                count +=3
                i+=2
                continue
            
            if i == len(ratings)-1:
                if ratings[i] < ratings[i-1]:
                    count += 1
                elif ratings[i] > ratings[i-1]:
                    count += 2
                else:
                    count+=3
            else:
                if ratings[i] == ratings[i+1]:
                    count += 3
                    i += 1
                elif ratings[i] > ratings[i-1] or ratings[i] > ratings[i+1]:
                    count += 2
                elif ratings[i] < ratings[i-1] or ratings[i] < ratings[i+1]:
                    count += 1
            i += 1
        # return count 
        print(count)
    
candy()

def candy2():
        ratings = [1,2,87,87,87,2,1]
        i = 0
        n = len(ratings)
        candy =[1] * n
        while(i<n):
            if ratings[i] > ratings[i+1]:
                candy[i] = candy[i+1] + 1
            
            i+=1
        j = len(ratings) -1
        while (j >= 0):
            
            j -= 1
            
    
