def complex_function_4(lst):
    result = []
    for num in lst:
        if num % 2 == 0:
            s = 0
            str_num = str(num)
            for i in range(len(str_num)):
                s += int(str_num[i])
            result.append(s)
        else:
            rev = []
            str_num = str(num)
            for i in range(len(str_num) - 1, -1, -1):
                rev.append(str_num[i])
            result.append(int("".join(rev)))

    return result

