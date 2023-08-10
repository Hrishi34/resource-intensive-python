def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

limit = 100000
primes = [num for num in range(2, limit) if is_prime(num)]
