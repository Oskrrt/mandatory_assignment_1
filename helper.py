def find_prime_factors_original_helper(n, prime_factors=[]):
    i = 2
    loop_iterations = 0
    divide_count = 0
    while i * i <= n:
        loop_iterations += 1
        if n % i == 0:
            prime_factors.append(i)
            n //= i
            divide_count += 1
        else:
            i += 1
    if n > 1:
        prime_factors.append(n)
    #print(prime_factors)
    print(f"Number of divisions for the original algorithm is: {divide_count}")
    return loop_iterations

### Optimized algorithm: ###
def is_edge_case(number):
    return number <= 1

def find_prime_factors_helper(n, prime_factors=None):
    if prime_factors is None:
        prime_factors = []

    if is_edge_case(n):
        return prime_factors
    i = 2
    addend = 1
    loop_iterations = 0
    divide_count = 0
    while i * i <= n:
        if i == 3:
            addend = 2
        loop_iterations += 1
        if n % i == 0:
            prime_factors.append(i)
            n //= i
            divide_count += 1
        else:
            i += addend
    if n > 1:
        prime_factors.append(n)
    #print(prime_factors)
    print(f"Number of divisions for the optimized algorithm is: {divide_count}")
    return loop_iterations

value = 315245180938241856225939
loop_iterations_original = find_prime_factors_original_helper(value)
loop_iterations_optimized = find_prime_factors_helper(value)
loop_iterations_differential = loop_iterations_original - loop_iterations_optimized
print(f"For n = {value}"
      f"\nLoop iterations for the original algorithm is: {loop_iterations_original}"
      f"\nLoop iterations for the optimized algorithm is: {loop_iterations_optimized}"
      f"\nDifference in loop iterations is: {loop_iterations_differential}")
