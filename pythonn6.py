import random

num_simulations = 1000000

def monte_carlo_simulation():
    # Some complex simulation logic
    x = random.random()
    y = random.random()
    return x ** 2 + y ** 2 < 1

results = [monte_carlo_simulation() for _ in range(num_simulations)]
