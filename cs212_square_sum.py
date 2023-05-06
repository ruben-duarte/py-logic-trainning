def square_sum(n):
    sum = 0
    for number in range(n+1):
        sum += number**2
    return sum


def square_sum2(n):
    return sum(number**2 for number in range(n+1))

result1 = square_sum(3) 
result2 = square_sum2(3) 
print(result1)
print(result2)