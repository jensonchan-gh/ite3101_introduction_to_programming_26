def digit_sum(n:int)->int:
    sum = 0
    for char in str(n):
        sum += int(char)
    return sum


print(digit_sum(1234))