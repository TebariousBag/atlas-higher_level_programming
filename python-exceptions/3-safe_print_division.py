#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        total = a / b
    except (TypeError, ValueError, ZeroDivisionError):
        total = None
    finally:
        print(f"Inside result: {total}")
    return (total)
