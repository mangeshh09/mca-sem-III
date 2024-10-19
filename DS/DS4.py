import math

# Function to calculate the binomial coefficient (n choose k)
def binomial_coefficient(n, k):
    return math.factorial(n) // (math.factorial(k) * math.factorial(n - k))

# Function to calculate the binomial distribution probability
def binomial_distribution(n, p, k):
    # Calculate binomial coefficient
    binom_coeff = binomial_coefficient(n, k)
    # Calculate binomial probability
    probability = binom_coeff * (p ** k) * ((1 - p) ** (n - k))
    return probability

# Real-time example: Coin flips
n = 10  # Number of coin flips
p = 0.5  # Probability of getting heads
k = 6  # Number of heads we are interested in

# Calculate binomial probability
binom_prob = binomial_distribution(n, p, k)

# Output the result
print(f"The probability of getting exactly {k} heads in {n} coin flips is: {binom_prob}")
