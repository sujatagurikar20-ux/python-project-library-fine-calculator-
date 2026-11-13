LIBRARY FINE CALCULATOR - PYTHON PACKAGE

Structure:
Library_Fine_Calculator/
    library_pkg/
        __init__.py
        ActualTask.py
    main.py
    test_cases.py
    README.txt
    Activity_2_Report.txt

Package: library_pkg
Module: ActualTask.py

Six user-defined functions:
1. overdue_days(due_date, return_date): finds late days.
2. calculate_fine(days, fine_per_day=2): calculates the basic fine.
3. payment_summary(book_title, days, ...): creates a payment summary.
4. calculate_due_date(issue_date, loan_period=14): calculates the due date.
5. calculate_discounted_fine(fine, discount_percent=0): applies a discount.
6. get_return_status(days): tells whether the book was returned on time or late.

Run from this folder:
python main.py

Run tests:
python test_cases.py

Enter dates in YYYY-MM-DD format. Default fine is Rs. 2 per overdue day.
