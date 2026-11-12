import csv
import math
import random
import sys
from pathlib import Path
from datetime import datetime, timedelta


NAME = "Vladyslav Radchuk"
GROUP = "IT-32"
BIRTH_YEAR = 2009

BASE_DIR = Path(__file__).resolve().parent
RESULTS_DIR = BASE_DIR / "results"
HISTORY_FILE = RESULTS_DIR / "history.csv"


def generate_questions():
    random.seed(BIRTH_YEAR)

    questions = []

    a = random.randint(5, 15)
    questions.append((
        f"Знайдіть цілу частину квадратного кореня з {a * a + random.randint(1, 20)}:",
        math.isqrt(a * a + random.randint(1, 20))
    ))

    number = random.randint(4, 7)
    questions.append((
        f"Чому дорівнює факторіал числа {number}?",
        math.factorial(number)
    ))

    a = random.randint(20, 60)
    b = random.randint(10, 40)
    questions.append((
        f"Знайдіть НСД чисел {a} і {b}:",
        math.gcd(a, b)
    ))

    n = random.randint(5, 10)
    k = random.randint(2, n - 1)
    questions.append((
        f"Обчисліть кількість комбінацій C({n}, {k}):",
        math.comb(n, k)
    ))

    number = random.randint(100, 500)
    percent = random.choice([10, 15, 20, 25])
    questions.append((
        f"Скільки становить {percent}% від числа {number}?",
        number * percent / 100
    ))

    return questions


def save_result(score, elapsed):
    RESULTS_DIR.mkdir(parents=True, exist_ok=True)

    file_exists = HISTORY_FILE.exists() and HISTORY_FILE.stat().st_size > 0

    with HISTORY_FILE.open("a", newline="", encoding="utf-8") as file:
        writer = csv.writer(file, delimiter=";")

        if not file_exists:
            writer.writerow(["name", "group", "date", "score", "time_seconds"])

        writer.writerow([
            NAME,
            GROUP,
            datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            score,
            round(elapsed, 2)
        ])


def show_history():
    if not HISTORY_FILE.exists():
        print("\nІсторія результатів поки порожня.")
        return

    with HISTORY_FILE.open("r", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file, delimiter=";")
        results = list(reader)

    if not results:
        print("\nІсторія результатів поки порожня.")
        return

    best = max(
        results,
        key=lambda item: (
            int(item["score"]),
            -float(item["time_seconds"])
        )
    )

    print("\nІСТОРІЯ РЕЗУЛЬТАТІВ")
    print(f"Кількість спроб: {len(results)}")
    print(f"Найкращий результат: {best['score']} з 5")
    print(f"Час виконання: {best['time_seconds']} секунд")
    print(f"Дата: {best['date']}")


def main():
    print("=" * 40)
    print("МАТЕМАТИЧНА ВІКТОРИНА")
    print(NAME, GROUP)
    print("=" * 40)

    questions = generate_questions()

    score = 0

    start_time = datetime.now()

    for index, (question, correct_answer) in enumerate(questions, start=1):
        print(f"\nПитання {index} з {len(questions)}")
        print(question)

        try:
            user_answer = float(input("Ваша відповідь: "))

            if math.isclose(user_answer, correct_answer):
                print("Правильно!")
                score += 1
            else:
                print(f"Неправильно. Правильна відповідь: {correct_answer}")

        except ValueError:
            print("Помилка: потрібно ввести число.")

    end_time = datetime.now()
    elapsed = (end_time - start_time).total_seconds()

    duration = timedelta(seconds=elapsed)

    print("\n" + "=" * 40)
    print("РЕЗУЛЬТАТИ ВІКТОРИНИ")
    print(f"Правильних відповідей: {score} з 5")
    print(f"Час виконання: {duration.total_seconds():.2f} секунд")
    print("=" * 40)

    save_result(score, elapsed)
    show_history()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nВиконання перервано.")
        sys.exit(1)
    except OSError as error:
        print(f"Помилка роботи з файлами: {error}", file=sys.stderr)
        sys.exit(1)