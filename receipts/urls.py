from django.urls import path
from receipts.views import (
    home,
    create_receipt,
    list_expenses,
    list_accounts,
    create_expense_view,
    create_account_view,
)

urlpatterns = [
    path("", home, name="home"),
    path("create/", create_receipt, name="create_receipt"),
    path("categories/", list_expenses, name="category_list"),
    path("accounts/", list_accounts, name="account_list"),
    path("categories/create/", create_expense_view, name="create_category"),
    path("accounts/create/", create_account_view, name="create_account"),
]
