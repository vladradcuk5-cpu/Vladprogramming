
import math
import sys
from pathlib import Path
from datetime import date, timedelta

NAME = "Vladyslav Radchuk"
GROUP = "IT-32"

print(f"{NAME}, {GROUP}")

BASE_DIR = Path(__file__).resolve().parent
FILE_PATH = BASE_DIR / "data" / "expenses.csv"

expenses = {}

try:
    with FILE_PATH.open("r", encoding="utf-8-sig") as file:
        for line_number, line in enumerate(file, start=1):
            line = line.strip()

            if not line or line.startswith("#"):
                continue

            try:
                parts = line.split(";")

                # Пропускаємо заголовок CSV
                if parts[0].strip().lower() == "date":
                    continue

                if len(parts) != 4:
                    raise ValueError("неправильна кількість полів")

                expense_date = date.fromisoformat(parts[0].strip())
                amount = float(parts[2].strip())

                if amount < 0:
                    raise ValueError("сума не може бути від'ємною")

                expenses.setdefault(expense_date, []).append(amount)

            except (ValueError, OverflowError) as error:
                print(
                    f"Warning: line {line_number}: {error}",
                    file=sys.stderr
                )

    if not expenses:
        raise ValueError("у файлі немає коректних записів")

    # Період витрат
    first_date = min(expenses)
    last_date = max(expenses)
    period_days = (last_date - first_date).days + 1

    print(
        f"period: {first_date:%d.%m.%Y} ({first_date:%A}) - "
        f"{last_date:%d.%m.%Y} ({last_date:%A}), "
        f"{period_days} days"
    )

    # Витрати за кожен день, включно з днями без витрат
    daily_expenses = {}
    current_date = first_date

    while current_date <= last_date:
        daily_expenses[current_date] = math.fsum(
            expenses.get(current_date, [])
        )
        current_date += timedelta(days=1)

    # Сума витрат за днями тижня
    weekdays = [
        "Monday", "Tuesday", "Wednesday",
        "Thursday", "Friday", "Saturday", "Sunday"
    ]

    print("\nweekday      total")

    for weekday_number, weekday_name in enumerate(weekdays):
        total = math.fsum(
            amount
            for day, amount in daily_expenses.items()
            if day.weekday() == weekday_number
        )

        print(f"{weekday_name:<12} {total:8.2f}")

    # Загальна сума, середнє та стандартне відхилення
    total_expenses = math.fsum(daily_expenses.values())
    average = total_expenses / period_days

    deviation = math.sqrt(
        math.fsum(
            (amount - average) ** 2
            for amount in daily_expenses.values()
        ) / period_days
    )

    print(f"\ntotal:        {total_expenses:.2f}")
    print(f"per day:      {average:.2f} +- {deviation:.2f}")

    # День із найбільшими витратами
    top_day = max(daily_expenses, key=daily_expenses.get)

    print(
        f"top day:      {top_day:%d.%m.%Y} "
        f"({top_day:%A}), {daily_expenses[top_day]:.2f}"
    )

    # Кількість днів без витрат
    no_spend_days = sum(
        1 for amount in daily_expenses.values()
        if amount == 0
    )

    print(f"no-spend days: {no_spend_days}")

    # Кількість днів у місяці та прогноз
    if last_date.month == 12:
        next_month = date(last_date.year + 1, 1, 1)
    else:
        next_month = date(last_date.year, last_date.month + 1, 1)

    first_month_day = date(last_date.year, last_date.month, 1)
    days_in_month = (next_month - first_month_day).days
    days_left = days_in_month - last_date.day

    month_forecast = average * days_in_month

    print(
        f"days in {last_date:%B}: "
        f"{days_in_month}, left after {last_date:%d.%m}: {days_left}"
    )

    print(f"month forecast: {month_forecast:.2f}")

    # Перевірка грудня 2026 та лютого 2028
    test_dates = [
        date(2026, 12, 15),
        date(2028, 2, 10)
    ]

    print("\nCalendar tests:")

    for test_date in test_dates:
        if test_date.month == 12:
            next_month = date(test_date.year + 1, 1, 1)
        else:
            next_month = date(
                test_date.year,
                test_date.month + 1,
                1
            )

        month_start = date(test_date.year, test_date.month, 1)
        days = (next_month - month_start).days

        print(
            f"{test_date:%d.%m.%Y}: "
            f"{days} days in month"
        )

except (FileNotFoundError, PermissionError, ValueError) as error:
    print(f"Error: {error}", file=sys.stderr)
    sys.exit(1)
