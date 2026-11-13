
import pytest
from pathlib import Path

from expenses import parse_line, load_expenses, total_by_category



def test_parse_line_valid():
    record = parse_line("2026-09-21;food;85.50;lunch")
    assert record["category"] == "food"
    assert record["amount"] == 85.5


def test_parse_line_date():
    record = parse_line("2026-09-21;food;85.50;lunch")
    assert record["date"] == "2026-09-21"


def test_parse_line_comment():
    record = parse_line("2026-09-21;food;85.50;lunch")
    assert record["comment"] == "lunch"



def test_parse_line_bad_amount():
    with pytest.raises(ValueError):
        parse_line("2026-09-21;food;abc;lunch")


def test_parse_line_wrong_fields():
    with pytest.raises(ValueError):
        parse_line("2026-09-21;food;85.50")



@pytest.mark.parametrize(
    "line, expected_category, expected_amount",
    [
        ("2026-10-01;Food;250;Groceries", "Food", 250.0),
        ("2026-10-02;Transport;80;Bus", "Transport", 80.0),
        ("2026-10-03;Food;320;Lunch", "Food", 320.0),
        ("2026-10-04;Entertainment;200;Cinema", "Entertainment", 200.0),
        ("2026-10-08;Education;350;Books", "Education", 350.0),
    ]
)
def test_parse_line_parametrize(line, expected_category, expected_amount):
    record = parse_line(line)
    assert record["category"] == expected_category
    assert record["amount"] == expected_amount



def test_total_by_category(tmp_path):
    path = tmp_path / "expenses.csv"

    path.write_text(
        "# date;category;amount;comment\n"
        "2026-09-21;food;85.50;lunch\n"
        "\n"
        "2026-09-22;food;14.50;coffee\n",
        encoding="utf-8",
    )

    totals = total_by_category(load_expenses(path))

    assert totals == {"food": 100.0}



def test_total_by_category_real_file():
    path = Path(__file__).parent / "data" / "expenses.csv"

    records = load_expenses(path)
    totals = total_by_category(records)

    assert totals == {
        "Food": 2110.0,
        "Transport": 360.0,
        "Entertainment": 350.0,
        "Education": 350.0
    }
