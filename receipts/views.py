from django.shortcuts import render, redirect
from receipts.models import Receipt
from receipts.forms import RecipeForm
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
