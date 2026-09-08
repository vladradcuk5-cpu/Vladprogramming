y = 2009


def print_age(year):
    age = 2026 - year
    print(f"Age: {age}")


def get_age(year, current_year=2026):
    if year > current_year or year < 0:
        return -1

    age = current_year - year
    return age
    print("after return")


print_age(y)

print(print_age(y))

age = get_age(y)

print(f"Age from get_age: {age}")
print(f"Age in months: {age * 12}")
print(f"Age in weeks: {age * 52}")
print(f"Age in 2030: {get_age(y, current_year=2030)}")

print(f"Invalid year 3000 gives: {get_age(3000)}")


try:
    print_age(y) * 12
except TypeError as error:
    print(f"TypeError: {error}")