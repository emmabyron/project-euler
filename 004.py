answer = 0
index = 999

while answer == 0:
    palindrome = int(index * 1000 + index % 10 * 100 + index % 100 - index % 10 + (index - index % 100) / 100)

    for number in range(100, 1000):
        if palindrome / number % 1 == 0:
            if palindrome / number < 1000:
                answer = palindrome
    
    index -= 1

print(answer)