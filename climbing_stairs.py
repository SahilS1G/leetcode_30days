def fact(num):
    if num == 0 or num == 1:
        return 1
    else:
        green = num * fact(num-1)
        return green
    return -1

def climbing(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        count = 1
        num = round(n/2)
        for i in range(1,num+1):
            if (n-(2*i) >= 0 and (n-i) >=0):
                count += fact(n-i)/(fact(i) * fact(n-(2*i)))
        
        count2 = int(count)
        
    print(count2)

a = int(input())
climbing(a)   
