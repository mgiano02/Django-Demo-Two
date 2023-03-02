from django.shortcuts import render
from receipts.models import Receipt

# Create your views here.
def home(request):
    receipt_item = Receipt.objects.all()
    context = {
        "receipt_item": receipt_item,
    }
    return render(request, "receipts/list.html", context)
