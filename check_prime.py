def check_prime(number):
    if number == 1:
        print('it is not a prime number')
    elif number == 2:
        print('it is a prime number')
    else:
        for x in range(2,number):
            if number%x==0:
                print('the number is not a prime number')
                break
            else:
                print('the number is a prime number')
                break
check_prime(13)
