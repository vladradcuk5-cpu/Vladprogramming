print("Radchuk Vlad, IT-32")

day = int(input("Enter day (integer): "))
month = int(input("Enter month (integer): "))
year = int(input("Enter year (integer): "))

if year <= 0:
    print("Date is invalid: year must be positive")

elif month < 1 or month > 12:
    print("Date is invalid: month must be between 1 and 12")

else:
    if month == 2:
        if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
            max_days = 29
        else:
            max_days = 28

    elif month in [1, 3, 5, 7, 8, 10, 12]:
        max_days = 31

    else:
        max_days = 30

    if day < 1:
        print("Date is invalid: day must be positive")
    elif day > max_days:
        print(f"Date is invalid: month {month} has only {max_days} days")
    else:
        print("Date is valid")