def read_grade(prompt):
    """Reads a valid integer grade from 0 to 100."""
    while True:
        value = input(prompt)

        if not value.isdigit():
            print("Error: digits only")
            continue

        grade = int(value)

        if grade < 0 or grade > 100:
            print("Error: the value must be between 0 and 100")
            continue

        return grade


def to_letter(grade):
    """Converts a numeric grade to a letter grade."""
    if grade >= 10:
        return "A"
    if grade >= 9:
        return "B"
    if grade >= 7:
        return "C"
    if grade >= 6:
        return "D"
    if grade >= 4:
        return "E"
    return "F"


def average(grades):
    """Returns the arithmetic mean of grades."""
    return sum(grades) / len(grades)


def count_above(grades, limit):
    """Returns the number of grades greater than the limit."""
    count = 0

    for grade in grades:
        if grade > limit:
            count += 1

    return count


def print_report(name, group, grades):
    """Prints a report with student grades and statistics."""
    avg = average(grades)

    print("--- Report ---")
    print(f"Student: {name}, group {group}")
    print("Grades:", *grades)
    print(f"Average: {avg:.2f} -> {to_letter(avg)}")
    print(f"Best: {max(grades)}, worst: {min(grades)}")
    print(f"Above average: {count_above(grades, avg)}")


def main():
    """Runs the program."""
    name = "Vlad"
    group = "IT-32"
    grades = [8, 7, 9, 10]

    print_report(name, group, grades)


main()
