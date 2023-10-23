from django.shortcuts import render
from app_BRMapp.forms import NewBookForm
from app_BRMapp.models import Book
from django.http import HttpResponse
# Create your views here.

def viewBook(request):
    books=Book.objects.all()

def newBook(request):
    form=NewBookForm()
    return render (request,'app_BMRapp/new_book.html',{'form':form})

def add(request):
    if request.method=="POST":
        form=NewBookForm(request.POST)
        if form.is_valid():
            nm=form.cleaned_data['title']
            em=form.cleaned_data['price']
            pw=form.cleaned_data['author']
            sw=form.cleaned_data['publisher']
            
            reg=Book(title=nm,price=em,author=pw,publisher=sw)
            reg.save()
            # fm=NewBookForm()
    s="Recore Submitted <br><a href='/app_BRMapp/view-books'>View All Books</a>"
    return HttpResponse(s)


