import random

size = 1000000
numbers = [random.randint(1, 1000000) for _ in range(size)]

sorted_numbers = sorted(numbers)
