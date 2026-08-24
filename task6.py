# Task 6
# Radchuk
# Group IT-32

name = input("Enter your name: ")
age = int(input("Enter your age: "))

age_in_range = 18 <= age <= 60
age_is_even = age % 2 == 0
both_conditions = age_in_range and age_is_even
one_condition = age_in_range or age_is_even
years_to_60 = 60 - age

print(f"Hello, {name}!")
print(f"Age is between 18 and 60: {age_in_range}")
print(f"Age is even: {age_is_even}")
print(f"Both conditions are true: {both_conditions}")
print(f"At least one condition is true: {one_condition}")
print(f"Years to 60: {years_to_60}")