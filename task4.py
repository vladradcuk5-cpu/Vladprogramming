print("Radchuk Vlad, IT-32")

score = int(input("Enter your score (integer, 0-100): "))
missed = int(input("Enter the number of missed classes (integer): "))

if score < 0 or score > 100:
    print("Error: score must be between 0 and 100")
else:
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

    if score >= 60:
        status = "passed"
    else:
        status = "failed"

    print(f"Score: {score}, Grade: {grade}, Status: {status}")

    total_classes = 16
    missed_percent = missed / total_classes * 100

    if missed_percent > 30:
        print("Warning: more than 30% of classes were missed. Not admitted.")