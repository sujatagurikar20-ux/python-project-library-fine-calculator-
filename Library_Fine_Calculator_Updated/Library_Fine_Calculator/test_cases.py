from library_pkg import (
    overdue_days, calculate_fine, payment_summary,
    calculate_due_date, calculate_discounted_fine, get_return_status
)

def run_tests():
    assert overdue_days("2026-11-10", "2026-11-13") == 3
    assert calculate_fine(3) == 6
    assert get_return_status(3) == "Book returned late. Fine payable."
    assert overdue_days("2026-11-10", "2026-11-10") == 0
    assert get_return_status(0) == "Returned on time. No fine."
    assert calculate_due_date("2026-11-01", 14) == "2026-11-15"
    assert calculate_discounted_fine(100, 10) == 90
    assert payment_summary("Python Basics", 5, discount_percent=10)["total_fine"] == 9

    for function, args in [
        (overdue_days, ("10-11-2026", "2026-11-13")),
        (calculate_discounted_fine, (100, 120))
    ]:
        try:
            function(*args)
        except ValueError:
            pass
        else:
            raise AssertionError("Expected invalid input to raise ValueError")
    print("All test cases passed.")

if __name__ == "__main__":
    run_tests()
