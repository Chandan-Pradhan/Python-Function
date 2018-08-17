def check_perfect(number):
    sum = 0
    for x in range(1,number):
        if number % x == 0:
            sum = sum + x
        else:
            pass

    return number == sum

print(check_perfect(28))
