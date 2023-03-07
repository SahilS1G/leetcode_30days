
def happy(n):
        set_ = set()
        while n != 1:
            n_lst = [int(x) for x in str(n)]
            n = 0
            for x in n_lst:
                n += x**2
            if n in set_:
                return False
            else:
                set_.add(n)
        return True
            

print(happy(88))
    