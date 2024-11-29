numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []

for number in numbers:
    if number == 1:
        continue
    prime_ = True
    for i in range(2, number):
        if number % i == 0:
            prime_ = False
            break
    if prime_:
        primes.append(number)
    else:
        not_primes.append(number)

print("Primes:", primes)
print("Not Primes:", not_primes)