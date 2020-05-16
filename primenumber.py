prime_input = int(input())
i = 0
prime_tester = 0

while i < 999:
    i += 1
    if prime_input % i == 0:
        prime_tester += 1
    if prime_tester > 2:
        break

if prime_tester == 2:
    print("This number is prime")
else:
    print("This number is not prime")
