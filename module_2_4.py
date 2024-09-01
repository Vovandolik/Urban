numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
for i in range(1, len(numbers)):
    k = 0
    for j in range(1, i + 1):
        if numbers[i] % j == 0:
            k = k + 1
        if k > 1:
            not_primes.append(i + 1)
            break
        elif k == 1 and numbers[i] == j + 1:
            primes.append(i + 1)
print("Простые:", primes)
print("Не простые:", not_primes)