name = "Vlad"
surname = "Radchuk"
group = "IT-32"

print(f"{name} {surname}, {group}")

attempts = 0

while True:
    score = int(input("Enter your score (0-100): "))
    attempts += 1

    if score < 0:
        print("Score cannot be negative")
    elif score > 100:
        print("Score is too big, maximum is 100")
    else:
        break

print(f"Accepted after {attempts} attempts")

if score >= 90:
    grade = "A"
elif score >= 82:
    grade = "B"
elif score >= 74:
    grade = "C"
elif score >= 64:
    grade = "D"
elif score >= 60:
    grade = "E"
else:
    grade = "F"

print(f"Grade: {grade}")