from itertools import permutations

def isPrime(num):
    if num <= 1:
        return False
    if num == 2:
        return True
    for i in range(2, num):
        if num % i == 0:
            return False
    return True
    
    
def solution(numbers):
    primes = set()
    for idx in range(1, len(numbers)+1):
        pers = list(map(int, map(''.join, list(permutations(numbers, idx)))))
        print(pers)
        for per in pers:
            if isPrime(per):
                primes.add(per)
    answer = len(primes)
    return answer