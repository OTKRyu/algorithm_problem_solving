from itertools import combinations

def isPrime(n):
    for i in range(2, n):
    	if n % i == 0:		
            return False
    return True

def solution(nums):
    answer = -1
    combs = list(combinations(nums, 3))
    primes = []
    for comb in combs:
        tmp = sum(comb)
        if isPrime(tmp):
            primes.append(tmp)
    answer = len(primes)
    return answer


	