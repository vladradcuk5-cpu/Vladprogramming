name = "Vlad"
surname = "Radchuk"
group = "IT-32"

d = 12
c = 7
n = d * c

print(f"{name} {surname}, {group}")
print(f"n = {d} * {c} = {n}")

divisors = []
total = 0

for i in range(1, n + 1):
    if n % i == 0:
        divisors.append(i)
        total += i

print("Divisors:", *divisors)
print(f"Divisors count: {len(divisors)}, sum: {total}")

for i in range(2, n):
    if n % i == 0:
        print(f"{n} is not prime")
        break
else:
    print(f"{n} is prime")

primes = []

for number in range(2, n + 1):
    for i in range(2, number):
        if number % i == 0:
            break
    else:
        primes.append(number)

print("Primes up to", n, ":", *primes)
print(f"Primes count: {len(primes)}")