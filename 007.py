primes = [2]

index = 3

while len(primes) < 10001:
    for prime in primes:
        if prime > index ** (1/2):
            primes.append(index)

            break

        if index / prime % 1 == 0:
            break
    
    index += 2

print(primes[10000])