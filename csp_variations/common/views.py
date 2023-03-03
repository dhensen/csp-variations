from django.shortcuts import render
from django.shortcuts import render

# Create your views here.

def foobar(request):
    return render(request, "common/index.html", {})
