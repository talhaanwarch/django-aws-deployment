from django.shortcuts import render
from .forms import MyForm
# Create your views here.

def home(request):
    form=MyForm(request.POST,request.FILES)
    if request.method=='POST':
        if form.is_valid():
            form.save()
    return render(request,"home.html",{"form":form})