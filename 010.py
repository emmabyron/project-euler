primes = [2]

index = 3

while primes[-1] <= 2000000:
    for p in primes:
        if p > index ** (1/2):
            primes.append(index)

            break

        if index / p % 1 == 0:
            break
    
    index += 2

primes = primes[:-1]

print(sum(primes))