numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
for i in numbers:
    s = 0
    for j in range(2,16):
        if i%j == 0:
            s += 1
    if s > 1:
        not_primes += [i]
    else:
        primes += [i]

primes.remove(1)


print(not_primes)
print(primes)

