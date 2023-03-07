
def power(n):
        if n == 1:
            return True
        elif n <=0:
            return False
        else:
            for i in range(1,int(round(n/2))+1):
                if 2**i == n:
                    return True
        return False
    
print(power(-3))