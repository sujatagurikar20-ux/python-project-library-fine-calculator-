from library_pkg import calculate_due_date, overdue_days, payment_summary, get_return_status

def main():
    print("===================================")
    print("       LIBRARY FINE CALCULATOR")
    print("===================================")
    try:
        title = input("Enter book title: ").strip()
        issue_date = input("Enter issue date (YYYY-MM-DD): ").strip()
        loan_period = int(input("Enter allowed loan period in days (e.g. 14): "))
        due_date = calculate_due_date(issue_date, loan_period)
        print("Calculated due date:", due_date)

        return_date = input("Enter return date (YYYY-MM-DD): ").strip()
        discount = float(input("Enter membership discount percentage (0 if none): "))

        days = overdue_days(due_date, return_date)
        summary = payment_summary(title, days, discount_percent=discount)

        print("\n----------- PAYMENT SUMMARY -----------")
        print("Book title       :", summary["book_title"])
        print("Due date         :", due_date)
        print("Overdue days     :", summary["overdue_days"])
        print("Fine per day     : Rs.", summary["fine_per_day"])
        print("Basic fine       : Rs.", summary["basic_fine"])
        print("Discount         :", str(summary["discount_percent"]) + "%")
        print("Total fine       : Rs.", summary["total_fine"])
        print("Status           :", get_return_status(days))
    except (ValueError, TypeError) as error:
        print("\nInput Error:", error)

if __name__ == "__main__":
    main()
