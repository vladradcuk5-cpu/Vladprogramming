
import math
import re
import sys
from pathlib import Path
from datetime import datetime

NAME = "Vladyslav Radchuk"
GROUP = "IT-32"

BASE_DIR = Path(__file__).resolve().parent
SOURCE_DIR = BASE_DIR / "files_copy"
REPORT_DIR = BASE_DIR / "reports"

def format_size(size):
    """Повертає розмір файлу у зручних одиницях."""
    units = ["B", "KB", "MB", "GB", "TB"]

    if size == 0:
        return "0 B"

    index = min(int(math.log(size, 1024)), len(units) - 1)
    value = size / (1024 ** index)

    return f"{value:.2f} {units[index]}"


def main():
    print(f"{NAME}, {GROUP}")
    dry_run = "--dry-run" in sys.argv

    if not SOURCE_DIR.exists() or not SOURCE_DIR.is_dir():
        print("Error: папку files_copy не знайдено", file=sys.stderr)
        return 1

    REPORT_DIR.mkdir(parents=True, exist_ok=True)

    files = []

    # Збираємо файли, не обробляючи вже створені папки YYYY-MM
    for path in SOURCE_DIR.rglob("*"):
        if not path.is_file():
            continue

        relative = path.relative_to(SOURCE_DIR)

        if len(relative.parts) > 1 and re.fullmatch(
            r"\d{4}-\d{2}", relative.parts[0]
        ):
            continue

        try:
            stat = path.stat()
            modified = datetime.fromtimestamp(stat.st_mtime)

            files.append({
                "path": path,
                "modified": modified,
                "size": stat.st_size
            })

        except OSError as error:
            print(f"Warning: {path}: {error}", file=sys.stderr)

    if not files:
        print("Немає файлів для сортування.")
        return 0

    # Сортуємо від найстаріших до найновіших
    files.sort(key=lambda item: item["modified"])

    # Формуємо план переміщення
    plan = []

    for item in files:
        source = item["path"]
        month_folder = item["modified"].strftime("%Y-%m")
        destination = SOURCE_DIR / month_folder / source.name

        plan.append({
            "source": source,
            "destination": destination,
            "modified": item["modified"],
            "size": item["size"]
        })

    # Перевіряємо всі конфлікти до переміщення
    destinations = set()
    collisions = []

    for item in plan:
        source = item["source"]
        destination = item["destination"]

        if destination in destinations:
            collisions.append(
                f"Повторна назва у плані: {destination}"
            )
        else:
            destinations.add(destination)

        if destination.exists() and destination != source:
            collisions.append(
                f"Файл уже існує: {destination}"
            )

    if collisions:
        print("Виявлено конфлікти. Жоден файл не переміщено:")
        for collision in collisions:
            print(collision, file=sys.stderr)
        return 2

    # Створюємо звіт
    report_time = datetime.now()
    report_name = report_time.strftime("organize_%Y%m%d_%H%M.txt")
    report_path = REPORT_DIR / report_name

    report_lines = [
        f"{NAME}, {GROUP}",
        f"Дата звіту: {report_time:%d.%m.%Y %H:%M:%S}",
        f"Режим: {'DRY-RUN' if dry_run else 'ЗВИЧАЙНЕ СОРТУВАННЯ'}",
        f"Папка: {SOURCE_DIR}",
        "",
        "Файли (від найстаріших до найновіших):",
        ""
    ]

    print("\nПлан сортування:" if dry_run else "\nСортування файлів:")

    # Переміщуємо файли або лише показуємо план
    for item in plan:
        source = item["source"]
        destination = item["destination"]
        modified = item["modified"]
        size_text = format_size(item["size"])

        if dry_run:
            action = f"[DRY-RUN] {source.name} -> {destination.parent.name}/"
        else:
            try:
                destination.parent.mkdir(parents=True, exist_ok=True)
                source.rename(destination)
                action = f"[MOVED] {source.name} -> {destination.parent.name}/"

            except OSError as error:
                print(f"Error: {error}", file=sys.stderr)
                report_lines.append(f"ERROR: {error}")
                report_path.write_text(
                    "\n".join(report_lines), encoding="utf-8"
                )
                return 1

        print(
            f"{action} | {modified:%Y-%m-%d %H:%M} | {size_text}"
        )

        report_lines.append(
            f"{action} | {modified:%Y-%m-%d %H:%M} | {size_text}"
        )

    report_lines.append("")
    report_lines.append(f"Усього файлів: {len(plan)}")

    report_path.write_text("\n".join(report_lines), encoding="utf-8")

    print(f"\nУсього файлів: {len(plan)}")
    print(f"Звіт збережено: {report_path}")

    if dry_run:
        print("Це був пробний запуск. Файли не переміщувалися.")

    return 0


if __name__ == "__main__":
    sys.exit(main())
