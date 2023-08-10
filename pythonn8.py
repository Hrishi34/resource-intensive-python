import math

def compute_sum(limit):
    total_sum = 0.0
    for i in range(1, limit + 1):
        total_sum += 1.0 / math.sqrt(i)
    return total_sum

# Calculate the sum for a large range (adjust the limit as needed)
sum_limit = 100000000
result = compute_sum(sum_limit)
print(result)