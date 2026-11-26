
import sys
from task2 import test_error


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(
            "Usage: python task4.py "
            "[connection|http|timeout]",
            file=sys.stderr
        )
        sys.exit(1)

    test_error(sys.argv[1])
