primes = [2]

index = 3

while primes[-1] <= 2000000:
    for prime in primes:
        if prime > index ** (1/2):
            primes.append(index)

            break

        if index / prime % 1 == 0:
            break
    
    index += 2

primes = sum(primes[:-1])

print(primes)