# Task 4
# Radchuk
# Group IT-32

a = 1
b = 12
c = len("Radchuk")

first_result = a < b
second_result = b > c
third_result = a <= b >= c

fourth_result = a > b
fifth_result = b < c
sixth_result = a != a

print(f"a = {a}, b = {b}, c = {c}")

print(f"{a} < {b} = {first_result}, type = {type(first_result)}")
print(f"{b} > {c} = {second_result}, type = {type(second_result)}")
print(f"{a} <= {b} >= {c} = {third_result}, type = {type(third_result)}")
print(f"{a} > {b} = {fourth_result}, type = {type(fourth_result)}")
print(f"{b} < {c} = {fifth_result}, type = {type(fifth_result)}")
print(f"{a} != {a} = {sixth_result}, type = {type(sixth_result)}")