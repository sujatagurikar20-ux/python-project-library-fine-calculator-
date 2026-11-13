from datetime import datetime, timedelta

def overdue_days(due_date, return_date):
    """Calculate late days using YYYY-MM-DD dates."""
    try:
        due = datetime.strptime(due_date, "%Y-%m-%d").date()
        returned = datetime.strptime(return_date, "%Y-%m-%d").date()
    except ValueError:
        raise ValueError("Dates must be valid and use YYYY-MM-DD format.")
    return max((returned - due).days, 0)

def calculate_fine(days, fine_per_day=2):
    """Calculate the basic fine."""
    if not isinstance(days, int) or isinstance(days, bool) or days < 0:
        raise ValueError("Overdue days must be a non-negative whole number.")
    if not isinstance(fine_per_day, (int, float)) or isinstance(fine_per_day, bool) or fine_per_day < 0:
        raise ValueError("Fine per day must be a non-negative number.")
    return round(days * fine_per_day, 2)

def payment_summary(book_title, days, fine_per_day=2, discount_percent=0):
    """Create a dictionary containing the payment details."""
    if not isinstance(book_title, str) or not book_title.strip():
        raise ValueError("Book title cannot be empty.")
    basic = calculate_fine(days, fine_per_day)
    final = calculate_discounted_fine(basic, discount_percent)
    return {
        "book_title": book_title.strip(), "overdue_days": days,
        "fine_per_day": fine_per_day, "basic_fine": basic,
        "discount_percent": discount_percent, "total_fine": final
    }

def calculate_due_date(issue_date, loan_period=14):
    """Calculate due date from issue date and allowed loan days."""
    try:
        issued = datetime.strptime(issue_date, "%Y-%m-%d").date()
    except ValueError:
        raise ValueError("Issue date must be valid and use YYYY-MM-DD format.")
    if not isinstance(loan_period, int) or isinstance(loan_period, bool) or loan_period <= 0:
        raise ValueError("Loan period must be a positive whole number.")
    return (issued + timedelta(days=loan_period)).isoformat()

def calculate_discounted_fine(fine, discount_percent=0):
    """Apply a membership discount percentage."""
    if not isinstance(fine, (int, float)) or isinstance(fine, bool) or fine < 0:
        raise ValueError("Fine must be a non-negative number.")
    if not isinstance(discount_percent, (int, float)) or isinstance(discount_percent, bool) or not 0 <= discount_percent <= 100:
        raise ValueError("Discount must be between 0 and 100.")
    return round(fine * (1 - discount_percent / 100), 2)

def get_return_status(days):
    """Return whether the book was returned on time or late."""
    if not isinstance(days, int) or isinstance(days, bool) or days < 0:
        raise ValueError("Overdue days must be a non-negative whole number.")
    return "Returned on time. No fine." if days == 0 else "Book returned late. Fine payable."
