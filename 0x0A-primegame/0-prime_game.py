#!/usr/bin/python3
""" Prime game module"""


def isWinner(x, nums):
    """Checks the winner b/w a set of prime number

    Args:
        nums: set of prime numbers

    Returns: prime
    """
    def sieve_of_eratosthenes(max_num):
        """ Sieve of eratothesnes"""
        is_prime = [True] * (max_num + 1)
        p = 2
        while (p * p <= max_num):
            if is_prime[p]:
                for i in range(p * p, max_num + 1, p):
                    is_prime[i] = False
            p += 1
        is_prime[0] = is_prime[1] = False
        return [num for num, prime in enumerate(is_prime) if prime]

    max_n = max(nums)
    primes = sieve_of_eratosthenes(max_n)
    prime_set = set(primes)

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        current_set = set(range(1, n + 1))

        maria_turn = True
        while True:
            available_primes = [p for p in primes if p in current_set]

            if not available_primes:
                if maria_turn:
                    ben_wins += 1
                else:
                    maria_wins += 1
                break

            chosen_prime = min(available_primes)

            for multiple in range(chosen_prime, n + 1, chosen_prime):
                if multiple in current_set:
                    current_set.remove(multiple)

            maria_turn = not maria_turn

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
