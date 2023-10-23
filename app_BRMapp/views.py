from django.shortcuts import render
from app_BRMapp.forms import NewBookForm
from app_BRMapp.models import Book
from django.http import HttpResponse,HttpResponseRedirect

# Create your views here.

def delete(request):
    bookid=request.GET['bookid']
    book=Book.objects.filter(id=bookid)
    book.delete()
    return HttpResponseRedirect("app_BMRapp/view_books")

def editBook(request):    #pehla aapde edit krva book choose kri
    book=Book.objects.get(id=request.GET['bookid'])
    fields={'title':book.title,'price':book.price,'author':book.author,'publisher':book.publisher}
    form=NewBookForm(initial=fields)
    return render(request,'app_BMRapp/edit_book.html',{'form':form,'book':book})

def edit(request):      #now we have edited and saved it back in database
    if request.method =="POST":
        form=NewBookForm(request.POST)
        if form.is_valid:
            form.save()
    return HttpResponseRedirect("app_BMRapp/view_books")
def viewBook(request):    #view all book from database
    books=Book.objects.all()
    return render(request,'app_BMRapp/view_book.html',{'books':books})

def newBook(request):   #add new book form 
    form=NewBookForm()
    return render (request,'app_BMRapp/new_book.html',{'form':form})

def add(request):     #New Book will store in database
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


