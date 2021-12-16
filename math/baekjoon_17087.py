import math

n, s = map(int, input().split())
locations = list(map(int, input().split()))
distances = [abs(s-locations[i]) for i in range(n)]
gcd = distances[0]
for i in range(1,n):
    gcd = math.gcd(gcd,distances[i])
print(gcd)