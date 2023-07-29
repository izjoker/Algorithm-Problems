n = input()
args = [int(e) for e in input().split(" ")]
 
def sol(n, args):
    ans = 0
    primes = sieve(max(args))
    for e in args:
        if e in primes:
            ans += 1
    return ans

def sieve(n):
    r = {}
    prime = [True for i in range(n+1)]
    p = 2
    while (p * p <= n):
        if (prime[p] == True):
            for i in range(p * p, n+1, p):
                prime[i] = False
        p += 1
 
    for p in range(2, n+1):
        if prime[p]:
            r[p] = True
    return r

print(sol(n, args))