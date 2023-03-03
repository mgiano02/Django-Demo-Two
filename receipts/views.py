from django.shortcuts import render
from receipts.models import Receipt
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def home(request):
    receipt_item = Receipt.objects.filter(purchaser=request.user)
    context = {
        "receipt_item": receipt_item,
    }
    return render(request, "receipts/list.html", context)
