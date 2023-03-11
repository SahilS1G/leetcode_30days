def lp():
    strs = ["flower","flow","flight"]
    pr = ""
    if not strs:
        return pr
    for i in range(len(strs[0])):
        char = strs[0][i]
        for j in range(1,len(strs)):
            if i == len(strs[j]) or strs[j][i] != char:
                return pr 
        pr += char
    return char

print(lp())