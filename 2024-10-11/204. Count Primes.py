from typing import List

# 204. Count Primes

# Given an integer n, return the number of prime numbers that are strictly less than n.

 
# Example 1:

# Input: n = 10
# Output: 4
# Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.
# Example 2:

# Input: n = 0
# Output: 0
# Example 3:

# Input: n = 1
# Output: 0
 

# Constraints:

# 0 <= n <= 5 * 10^6

class Solution:
    def countPrimes(self, n: int) -> int:
        if n == 0 or n == 1:
            return 0
        if n == 2:
            return 1
        ct = 1
        for i in range(3,n + 1): # ct = 4  10  i = 10
            for j in range(2, i + 1):# j = 2 
                if i % j == 0:
                    break
                if j == i:
                    ct += 1
        return ct # 4
            
                     
                     
            # 2  3  5  7  11  13 17 19 
            # 

# Sieve of Eratosthenes
class Solution:
    def countPrimes(self, n: int) -> int:
        if n <= 2:
            return 0

        # Initialize numbers[0] and numbers[1] as False because 0 and 1 are not prime.
        # Initialze numbers[2] through numbers[n-1] as True because we assume each number
        # is prime until we find a prime number (p) that is a divisor of the number
        numbers = [False, False] + [True] * (n - 2)
        for p in range(2, int(sqrt(n)) + 1):
            if numbers[p]:
                # Set all multiples of p to false because they are not prime.
                for multiple in range(p * p, n, p):
                    numbers[multiple] = False

        # numbers[index] will only be true where index is a prime number
        # return the number of indices whose value is true.
        return sum(numbers)