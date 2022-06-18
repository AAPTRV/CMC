import sys


def get_ip_state(ip_str):
    state = True
    input_ip = ip_str.split(".")
    if len(input_ip) != 4:
        state = False

    for item in input_ip:
        try:
            if int(item) > 255 or int(item) < 0:
                state = False
        except Exception:
            state = False
    return state


def encode(num):
    dict = {"M": 1000, "CM": 900, "D": 500, "CD": 400,
            "C": 100, "XC": 90, "L": 50, "XL": 40,
            "X": 10, "IX": 9, "V": 5, "IV": 4, "I": 1}
    number = int(num)
    str = ""
    for i in dict:
        while number >= int(dict[i]):
            str += i
            number -= int(dict[i])
    return str


def spiralPrint(m, n, a):
    k = 0;
    l = 0
    ''' k - starting row index 
        m - ending row index 
        l - starting column index 
        n - ending column index 
        i - iterator '''
    while (k < m and l < n):
        # Print the last column from
        # the remaining columns 6-9
        for i in range(k, m):
            print(a[i][n - 1], end=" ")
        n -= 1
        # Print the first row from
        # the remaining rows 1-2-3
        for i in range(l, n):
            print(a[k][i], end=" ")
        k += 1

        # Print the last row from
        # the remaining rows 8-7
        if (k < m):
            for i in range(n - 1, (l - 1), -1):
                print(a[m - 1][i], end=" ")
            m -= 1
        # Print the first column from
        # the remaining columns -4-
        if (l < n):
            for i in range(m - 1, k - 1, -1):
                print(a[i][l], end=" ")
            l += 1


def reversePrint(m, n, a):
    k = 0;
    l = 0
    ''' k - starting row index 
        m - ending row index 
        l - starting column index 
        n - ending column index 
        i - iterator '''
    while (k < m and l < n):
        # Print the first row from
        # the remaining rows 1-2-3
        for i in range(l, n):
            print(a[k][i], end=" ")
        k += 1
        # Print the last column from
        # the remaining columns
        for i in range(k, m):
            print(a[i][n - 1], end=" ")
        n -= 1
        # Print the last row from
        # the remaining rows
        if (k < m):
            for i in range(n - 1, (l - 1), -1):
                print(a[m - 1][i], end=" ")
            m -= 1
        # Print the first column from
        # the remaining columns
        if (l < n):
            for i in range(m - 1, k - 1, -1):
                print(a[i][l], end=" ")
            l += 1


def anticlockwiseSpiral(metrix, startRow,
                        startCol, endRow, endCol, element):
    #  Top to bottom direction
    i = startRow
    while (i <= endRow and element > 0):
        print(metrix[i][startRow], end="  ")
        i += 1
        element -= 1
    #  Left to right direction
    i = startRow + 1
    while (i <= endCol and element > 0):
        print(metrix[endRow][i], end="  ")
        i += 1
        element -= 1
    #  Bottomt to top direction
    i = endRow - 1
    while (i > startRow and element > 0):
        print(metrix[i][endCol], end="  ")
        i -= 1
        element -= 1
    #  Bottom to top direction
    i = endCol
    while (i > startCol and element > 0):
        print(metrix[startRow][i], end="  ")
        i -= 1
        element -= 1
    if (startRow + 1 <= endRow - 1 and element > 0):
        #  Recursive call
        anticlockwiseSpiral(metrix, startRow + 1,
                            startCol + 1, endRow - 1, endCol - 1, element)


def matched(str):
    count = 0
    for i in str:
        if i == "(":
            count += 1
        elif i == ")":
            count -= 1
        if count < 0:
            return False
    return count == 0


def solution(roman):
    try:
        dict_priotity = {
            "M": 1,
            "D": 2,
            "C": 3,
            "L": 4,
            "X": 5,
            "V": 6,
            "I": 7
        }
        letter_list = list(roman)
        priority_list = []
        for letter in letter_list:
            priority_list.append(dict_priotity[letter])
        i = 7
        for item in priority_list:
            if item > i:
                return 0
            i = item
    except Exception:
        return 0

    dict = {
        "M": 1000,
        "D": 500,
        "C": 100,
        "L": 50,
        "X": 10,
        "V": 5,
        "I": 1
    }

    last, total = 0, 0
    for c in list(roman)[::-1]:
        if last == 0:
            total += dict[c]
        elif last > dict[c]:
            total -= dict[c]
        else:
            total += dict[c]
        last = dict[c]
    return total


def reformat_result(str):
    result = str
    arr = str.split("/")
    numerator = int(arr[0])
    denominator = int(arr[1])
    for i in range(2, 10, 1):
        if numerator % i == 0:
            if denominator % i == 0:
                numerator = numerator / i
                denominator = denominator / i
                result = f"{int(numerator)}/{int(denominator)}"
    if numerator % denominator == 0:
        numerator = numerator / denominator
        denominator = 1
        result = f"{int(numerator)}/{int(denominator)}"
    if denominator % numerator == 0:
        denominator = denominator / numerator
        numerator = 1
        result = f"{int(numerator)}/{int(denominator)}"

    return result


def calculate(str):
    result = ""
    overall_list = list(str)
    if "+" in overall_list:
        common_list = str.strip().split(" + ")
        print(common_list)
        values = []
        for number in common_list:
            values.append(number.split("/"))
        print(values)
        if values[0][1] == values[1][1]:
            result = f"{int(values[0][0]) + int(values[1][0])}/{values[0][1]}"
            return reformat_result(result)
        else:
            multiplier_left = int(values[1][1])
            multiplier_right = int(values[0][1])
            values[0][0] = int(values[0][0]) * multiplier_left
            values[0][1] = int(values[0][1]) * multiplier_left
            values[1][0] = int(values[1][0]) * multiplier_right
            values[1][1] = int(values[1][1]) * multiplier_right
            result = f"{int(values[0][0]) + int(values[1][0])}/{values[0][1]}"
            return reformat_result(result)
    if "-" in overall_list:
        common_list = str.strip().split(" - ")
        print(common_list)
        values = []
        for number in common_list:
            values.append(number.split("/"))
        print(values)
        if values[0][1] == values[1][1]:
            result = f"{int(values[0][0]) - int(values[1][0])}/{values[0][1]}"
            return reformat_result(result)
        else:
            multiplier_left = int(values[1][1])
            multiplier_right = int(values[0][1])
            values[0][0] = int(values[0][0]) * multiplier_left
            values[0][1] = int(values[0][1]) * multiplier_left
            values[1][0] = int(values[1][0]) * multiplier_right
            values[1][1] = int(values[1][1]) * multiplier_right
            result = f"{int(values[0][0]) - int(values[1][0])}/{values[0][1]}"
            return reformat_result(result)
    if "*" in overall_list:
        common_list = str.strip().split(" * ")
        print(common_list)
        values = []
        for number in common_list:
            values.append(number.split("/"))
        result = f"{int(values[0][0]) * int(values[1][0])}/{int(values[0][1]) * int(values[1][1])}"
        return reformat_result(result)
    else:
        common_list = str.strip().split(" / ")
        print(common_list)
        values = []
        for number in common_list:
            values.append(number.split("/"))
        result = f"{int(values[0][0]) * int(values[1][1])}/{int(values[0][1]) * int(values[1][0])}"
        return reformat_result(result)


print(solution("VIV"))
print("CALCULATION")
print(calculate("2/3 / 3/7"))


str_1 = ")()()("
str_2 = "(()"
str_3 = "(()())"
str_4 = ")("
print(matched(str_1))
print(matched(str_2))
print(matched(str_3))
print(matched(str_4))
print(reformat_result("17/34"))

#  Matrix elements
matrix = [
    [1, 2, 3], [4, 5, 6], [7, 8, 9]
]
#  Get the size of matrix element
row = len(matrix)
col = len(matrix[0])
#  Get number of element
element = row * col
#  Print result
anticlockwiseSpiral(matrix, 0, 0, row - 1, col - 1, element)
