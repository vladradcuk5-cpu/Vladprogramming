# Task 1
# Radchuk
# Group IT-32

birth_day = 12
height = 1.87
full_name = "Vlad Radchuk"
has_driver_license = True

print(f"birth_day = {birth_day}, type = {type(birth_day)}")
print(f"height = {height}, type = {type(height)}")
print(f"full_name = {full_name}, type = {type(full_name)}")
print(f"has_driver_license = {has_driver_license}, type = {type(has_driver_license)}")

print("\nBefore changing types:")
print(f"birth_day = {birth_day}, type = {type(birth_day)}")
print(f"has_driver_license = {has_driver_license}, type = {type(has_driver_license)}")

birth_day = "one"
has_driver_license = 1.0

print("\nAfter changing types:")
print(f"birth_day = {birth_day}, type = {type(birth_day)}")
print(f"has_driver_license = {has_driver_license}, type = {type(has_driver_license)}")

birth_day + 1