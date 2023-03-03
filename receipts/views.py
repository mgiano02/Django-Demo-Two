from django.shortcuts import render, redirect
from receipts.models import Receipt, ExpenseCategory, Account
from receipts.forms import RecipeForm, ExpenseCatForm
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def home(request):
    receipt_item = Receipt.objects.filter(purchaser=request.user)
    context = {
        "receipt_item": receipt_item,
    }
    return render(request, "receipts/list.html", context)


@login_required
def create_receipt(request):
    if request.method == "POST":
        form = RecipeForm(request.POST)
        if form.is_valid():
            receipt = form.save(False)
            receipt.purchaser = request.user
            receipt.save()
            return redirect("home")
    else:
        form = RecipeForm()

    context = {
        "form": form,
    }
    return render(request, "receipts/create.html", context)


def list_expenses(request):
    expense_item = ExpenseCategory.objects.filter(owner=request.user)
    context = {
        "expense_item": expense_item,
    }
    return render(request, "receipts/categories.html", context)


def create_expense_view(request):
    if request.method == "POST":
        form = ExpenseCatForm(request.POST)
        if form.is_valid:
            expense = form.save(False)
            expense.owner = request.user
            expense.save()
            return redirect("category_list")
    else:
        form = ExpenseCatForm()
    context = {
        "form": form,
    }
    return render(request, "receipts/create_expense.html", context)


def list_accounts(request):
    account_item = Account.objects.filter(owner=request.user)
    context = {
        "account_item": account_item,
    }
    return render(request, "receipts/accounts.html", context)
