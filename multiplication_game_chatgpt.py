def get_prime_factors(n):
    """ Return the set of prime factors of the given number n. """
    i = 2
    factors = set()
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.add(i)
    if n > 1:
        factors.add(n)
    return factors

def find_winner(t, x, starter):
    if x == t:
        return starter
    if x > t:
        return "tie"
    
    # Get the prime factors of x
    prime_factors = get_prime_factors(x)
    steps = 0
    
    while x < t:
        # Find the highest multiplier we can get to get close to t
        max_factor = max(prime_factors, default=1)
        if max_factor * x > t:
            break
        x *= max_factor
        steps += 1
    
    if x == t:
        if steps % 2 == 0:
            return starter
        else:
            return "Alice" if starter == "Bob" else "Bob"
    
    return "tie"


def run_tests(test_input):
    lines = test_input.strip().split('\n')
    num_cases = int(lines[0].strip())
    results = []

    for i in range(1, num_cases + 1):
        line = lines[i].strip().split()
        t = int(line[0])
        x = int(line[1])
        starter = line[2]
        result = find_winner(t, x, starter)
        results.append(result)

    return results

# Multiline string containing test cases
test_input = """10
10 Alice
20 Bob
30 Alice
40 Bob
50 Alice
60 Bob
70 Alice
80 Bob
90 Alice
100 Bob"""

# Run the tests and print results
test_results = run_tests(test_input)
for result in test_results:
    print(result)
    
# Reading input
num_cases = int(input().strip())
results = []

for _ in range(num_cases):
    line = input().strip().split()
    t = int(line[0])
    x = int(line[1])
    starter = line[2]
    result = find_winner(t, x, starter)
    results.append(result)

# Printing the results
for result in results:
    print(result)
