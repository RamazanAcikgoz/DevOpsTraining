def is_prime_checker(n, divisor = None):
    if n <= 1:
        return False
    if divisor is None:
        divisor = n - 1
    if divisor == 1:
        return True
    if n % divisor == 0:
        return False
    return is_prime_checker(n, divisor - 1)


num = 9
if is_prime_checker(num):
    print(num, "is a prime number")
else:
    print(num, "is not a prime number")