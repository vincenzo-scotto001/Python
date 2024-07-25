"""
The Sieve of Eratosthenes is an algorithm used to generate all prime numbers smaller than N. 
The method is to take increasingly larger prime numbers, and mark their multiples as composite.

For example, to find all primes less than 100, we would first mark [4, 6, 8, ...] (multiples of two), then [6, 9, 12, ...] (multiples of three), and so on. 
Once we have done this for all primes less than N, the unmarked numbers that remain will be prime.

Implement this algorithm.

"""


def sieve_of_eratosthenes(N):
    # Create a boolean array "is_prime[0..N]" and initialize
    # all entries it as true. A value in is_prime[i] will finally be false if i is Not a prime, else true.
    
    is_prime = [True] * (N + 1)
    print(is_prime)
    is_prime[0] = is_prime[1] = False

    for i in range(2, int(N**0.5) + 1):
        if is_prime[i]:
            # Update all multiples of i
            for j in range(i*i, N+1, i):
                is_prime[j] = False

    # Collect all prime numbers
    primes = [num for num in range(2, N+1) if is_prime[num]]
    
    return primes

# Example usage
N = 100
result = sieve_of_eratosthenes(N)
print(f"Prime numbers smaller than {N}: {result}")