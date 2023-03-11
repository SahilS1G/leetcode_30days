def plus():
        digits = [4,3,2,1]
        output = []
        digits_str = list(map(str, digits))
        num_str = ''.join(digits_str)
        num = int(num_str)
        num2 = num +1
        num3 = str(num2)
        for i in range(len(num3)):
            output.append(int(num3[i]))
        print(output)
    
plus()