name = "Vlad"
surname = "Radchuk"
group = "IT-32"
y = 2009


def print_card():
    print(f"Name: {name} {surname}")
    print(f"Group: {group}")
    print(f"Birth year: {y}")


print("--- no parameters, call 1 ---")
print_card()

print("--- no parameters, call 2 ---")
print_card()

print("--- no parameters, call 3 ---")
print_card()


def print_card_args(name, surname, year, group=group):
    print(f"{name} {surname}, {group}, {year}")


print("--- positional arguments ---")
print_card_args("Vlad", "Radchuk", 2009, "IT-32")

print("--- keyword arguments ---")
print_card_args(year=2009, group="IT-32", surname="Radchuk", name="Vlad")

print("--- mixed arguments ---")
print_card_args("Vlad", "Radchuk", year=2009, group="IT-32")

print("--- default group ---")
print_card_args("Vlad", "Radchuk", 2009)


print("--- error ---")
try:
    print_card_args("Ivan")
except TypeError as error:
    print(error)
