import decimal
from decimal import Decimal, getcontext

def pi_bbp(digits):
    getcontext().prec = digits + 2  # Set decimal precision to desired digits + 2

    pi = Decimal(0)
    k = 0
    while k < digits + 1:
        pi += (Decimal(1)/(16**k)) * (
            Decimal(4)/(8*k+1) -
            Decimal(2)/(8*k+4) -
            Decimal(1)/(8*k+5) -
            Decimal(1)/(8*k+6)
        )
        k += 1

    return pi

# Calculate 10,000 digits of Pi (it will take some time)
num_digits = 10000
pi_value = pi_bbp(num_digits)
print(pi_value)
