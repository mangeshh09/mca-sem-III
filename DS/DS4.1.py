import math

# Function to manually calculate factorial
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result

# Function to manually calculate binomial coefficient (n choose k)
def binomial_coefficient(n, k):
    return factorial(n) // (factorial(k) * factorial(n - k))

# Function to manually calculate binomial distribution probability
def binomial_distribution_manual(n, p, k):
    # Step 1: Calculate binomial coefficient
    binom_coeff = binomial_coefficient(n, k)
    
    # Step 2: Calculate p^k and (1-p)^(n-k)
    p_to_the_power_k = p ** k
    q_to_the_power_n_minus_k = (1 - p) ** (n - k)
    
    # Step 3: Calculate probability
    probability = binom_coeff * p_to_the_power_k * q_to_the_power_n_minus_k
    
    # Show all the steps for manual calculation
    print(f"Factorial of n ({n}): {factorial(n)}")
    print(f"Factorial of k ({k}): {factorial(k)}")
    print(f"Factorial of (n-k) ({n-k}): {factorial(n - k)}")
    print(f"Binomial Coefficient (n choose k): {binom_coeff}")
    print(f"p^k = {p}^{k} = {p_to_the_power_k}")
    print(f"(1-p)^(n-k) = (1-{p})^{n-k} = {q_to_the_power_n_minus_k}")
    print(f"Binomial Probability: {probability}")
    
    return probability

# Real-time example: Coin flips
n = 10  # Number of coin flips
p = 0.5  # Probability of getting heads
k = 6  # Number of heads we are interested in

# Calculate binomial probability manually
binom_prob = binomial_distribution_manual(n, p, k)

# Output the result
print(f"\nThe probability of getting exactly {k} heads in {n} coin flips is: {binom_prob}")
