name = "Vlad"
surname = "Radchuk"
group = "IT-32"

print(f"{name} {surname}, {group}")

number = int(input("Enter an integer: "))

if number <= 0:
    print("Please enter a positive integer.")
else:
    count = 0
    total = 0
    max_digit = 0
    min_digit = 9
    reversed_number = 0

    while number > 0:
        digit = number % 10

        count += 1
        total += digit

        if digit > max_digit:
            max_digit = digit

        if digit < min_digit:
            min_digit = digit

        reversed_number = reversed_number * 10 + digit
        number = number // 10

    print(f"Digits: {count}")
    print(f"Sum of digits: {total}")
    print(f"Max digit: {max_digit}, min digit: {min_digit}")
    print(f"Reversed: {reversed_number}")