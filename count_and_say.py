def countAndSay():

    string = "2121"

    count = 1

    arr = []
    final = []
    for i in range(len(string)):
        if string[0] == string[i]:
            return (str(len(string)) + string[0])

    if len(string) == 1:
        green = "1" + string[0]
        return green

    for i in range(len(string)):
        if i != 0:
            if string[i-1] == string[i]:
                count += 1
            else:
                arr.append(str(count))
                arr.append(string[i-1])
                final.append(''.join(arr))
                arr = []
                count = 1

    count2 = 1
    j = len(string)-1
    while (j >= 0):
        if string[j] == string[j+1]:
            count2 += 1
        else:
            arr.append(str(count2))
            arr.append(string[len(string)-1])
            final.append(''.join(arr))
            break

        j -= 1

    return ''.join(final)


r = countAndSay()

print(r)
