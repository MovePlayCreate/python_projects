def is_prime(num):
    check_until = num ** .5
    if num < 2:
        return False
    if num == 2:
        return True
    for i in range(3, int(check_until), 2):
        if num % i == 0:
            return False
    return True
    
is_prime(27)
is_prime(29)
is_prime(31)
#check when at home with pycharm