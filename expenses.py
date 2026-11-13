
def parse_line(line):
    parts = line.strip().split(";")

    if len(parts) != 4:
        raise ValueError("Incorrect number of fields")

    try:
        amount = float(parts[2])
    except ValueError:
        raise ValueError("Amount must be a number")

    return {
        "date": parts[0],
        "category": parts[1],
        "amount": amount,
        "comment": parts[3]
    }


def total_by_category(records):
    totals = {}

    for record in records:
        category = record["category"]
        amount = record["amount"]

        if category not in totals:
            totals[category] = 0

        totals[category] += amount

    for category in totals:
        totals[category] = round(totals[category], 2)

    return totals


def load_expenses(path):
    records = []

    with open(path, "r", encoding="utf-8") as file:
        for line in file:
            line = line.strip()

            if not line or line.startswith("#"):
                continue

            if line.startswith("date;"):
                continue

            records.append(parse_line(line))

    return records
