
import pytest

from expenses import parse_line, load_expenses, total_by_category



def test_parse_line_valid():
    record = parse_line("2026-09-21;food;85.50;lunch")

    assert record["date"] == "2026-09-21"
    assert record["category"] == "food"
    assert record["amount"] == 85.5
    assert record["comment"] == "lunch"


def test_parse_line_transport():
    record = parse_line("2026-09-22;transport;50.00;bus")

    assert record["category"] == "transport"
    assert record["amount"] == 50.0


def test_parse_line_fun():
    record = parse_line("2026-09-23;fun;100.00;cinema")

    assert record["category"] == "fun"
    assert record["amount"] == 100.0



def test_parse_line_wrong_fields():
    with pytest.raises(ValueError):
        parse_line("2026-09-21;food;85.50")


def test_parse_line_bad_amount():
    with pytest.raises(ValueError):
        parse_line("2026-09-21;food;abc;lunch")



@pytest.mark.parametrize(
    "line, expected_category, expected_amount",
    [
        (";food;150.50;", "food", 150.50),
        (";food;200.00;", "food", 200.00),
        (";food;120.00;", "food", 120.00),
        (";transport;50.00;", "transport", 50.00),
        (";fun;250.00;", "fun", 250.00),
    ]
)
def test_parse_line_parametrized(line, expected_category, expected_amount):
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



def test_real_expenses():
    records = load_expenses("data/expenses.csv")
    totals = total_by_category(records)

    assert totals == {
        "food": 470.50,
        "transport": 165.00,
        "fun": 350.00
    }
