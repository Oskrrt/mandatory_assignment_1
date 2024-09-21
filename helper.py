def find_prime_factors_original_helper(n, prime_factors=[]):
    i = 2
    loop_iterations = 0
    while i * i <= n:
        loop_iterations += 1
        if n % i == 0:
            prime_factors.append(i)
            n //= i
        else:
            i += 1
    if n > 1:
        prime_factors.append(n)
    return loop_iterations

### Optimized algorithm: ###
def is_edge_case(number):
    return number <= 1

### used to check if n is lower than i*i to use when n is a small number: <9
def is_lower_than_divisor_squared(n, i):
    return n < i * i

def find_prime_factors_helper(n, prime_factors=None):
    if prime_factors is None:
        prime_factors = []

    if is_edge_case(n):
        return prime_factors
    i = 3
    addend = 2
    loop_iterations = 0
    if is_lower_than_divisor_squared(n, i):
        i = 2
        addend = 1
    while i * i <= n:
        loop_iterations += 1
        if n % i == 0:
            prime_factors.append(i)
            n //= i
        else:
            i += addend
    if n > 1:
        prime_factors.append(n)
    return loop_iterations

value = 315245180938241856225939
loop_iterations_original = find_prime_factors_original_helper(value)
loop_iterations_optimized = find_prime_factors_helper(value)
loop_iterations_differential = loop_iterations_original - loop_iterations_optimized
print(f"For n = {value}"
      f"\nLoop iterations for the original algorithm is: {loop_iterations_original}"
      f"\nLoop iterations for the optimized algorithm is: {loop_iterations_optimized}"
      f"\nDifference in loop iterations is: {loop_iterations_differential}")
