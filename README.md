# FJ-BE-R2-Rahul-Manglani-NIT-Rourkela

1. User Authentication: Use Django's in-built authentication system to implement user authentication. The users
should be able to register, log in, and manage their profiles.
2. Database Structure: Create a well-defined database structure and implement it using Django models. The
database should support the tracking of various financial details, including:
a. Income sources and the amount from each source
b. Expense categories and the amount spent in each
c. An item (or transaction) should have a date, amount, and a description
3. Transaction Management: Allow users to add, edit, and delete income and expense transactions.
4. Dashboard: Develop a user-friendly dashboard that provides an overview of the user's financial status,
including graphical representations of income, expenses, and savings.
5. Reporting: Users should be able to generate reports on their financial data, such as monthly income vs.
expenses report.
6. Budgeting: Allow users to set budget goals for different expense categories and track their progress.

1. OAuth Integration: Allow users to sign up using Google through Django Allauth or Google's API client library.
2. Notification System: Set up a system to notify users about budget overruns, etc., using email notifications
through Sendgrid or another service.
3
3. Database Upgrade: Transition from SQLite to MySQL to enhance the robustness of your database setup.
4. Expense Splitting: Introduce a feature to split expenses with others and keep track of who owes whom.
5. Receipt Uploading: Allow users to upload and store receipts for their transactions


[name='home']
signup/ [name='signup']
users/ [name='users']
login/ [name='login']
logout/ [name='logout']
add_income/ [name='add_income']
add_expense/ [name='add_expense']
edit_income/<int:income_id>/ [name='edit_income']
delete_income/<int:income_id>/ [name='delete_income']
edit_expense/<int:expense_id>/ [name='edit_expense']
delete_expense/<int:expense_id>/ [name='delete_expense']
income_expenses/ [name='income_expenses_list']
transactions/ [name='transactions']
budget_view/ [name='budget_view']
budget/ [name='budget']
budget/<int:goal_id>/ [name='budget_id']
edit_budget_goal/<int:goal_id>/ [name='edit_budget_goal']
delete_budget_goal/<int:goal_id>/ [name='delete_budget_goal']
financial_report/ [name='financial_report']
create_shared_expense/ [name='create_shared_expense']
list_shared_expenses/ [name='list_shared_expenses']
debt_status/ [name='debt_status']
dashboard/ [name='dashboard']
contact/ [name='contact']
shared-expenses/ [name='share_with_friend']
accounts/
admin/
^media/(?P<path>.*)$

