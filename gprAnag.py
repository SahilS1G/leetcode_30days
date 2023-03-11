def grpAnag():
        strs = ["eat","tea","tan","ate","nat","bat"]
        # l = 0
        # r = len(strs) - 1
        arr = []
        indices = []
        for i in range(len(strs)):
            arr2 = []
            arr2.append(strs[i])
            if i in indices:
                continue
            for j in range(i+1,len(strs)):
                if sorted(strs[i]) == sorted(strs[j]):
                    arr2.append(strs[j])
                    indices.append(j)
            arr.append(arr2)
        return arr

print(grpAnag())