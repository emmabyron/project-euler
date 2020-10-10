for a in range(1, 1001):
    for b in range(a, 1001):
        c = (a ** 2 + b ** 2) ** (1/2)

        if c % 1 == 0:
            if a + b + c == 1000:
                print(a * b * c)