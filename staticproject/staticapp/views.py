from django.shortcuts import render,redirect
from .models import Book
from .Regform import RegisterForm
from .forms import BookForm
from django.http import HttpResponse
# Create your views here.
def hello(request):
    return render(request,"staticapp/index.html")
def about(request):
    return render(request,"staticapp/about.html")
def contact(request):
    return render(request,"staticapp/contact.html")
def service(request):
    return render(request,"staticapp/service.html")
def dummy(request):
    return render(request,"staticapp/dummy.html")

#book manager
def book_list(request):
    books = Book.objects.all()
    return render(request, 'staticapp/book_list.html', {'books': books})

def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            #return redirect('book_list')
            return HttpResponse("<h1>Book have been added</h1>")
    else:
        form = BookForm()

    return render(request, 'staticapp/add_book.html', {'form': form})
def register(request):
    if request.method=="POST":
        form=RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("<h1>Form ban gaya mera</h1>")
    else:
            form=RegisterForm()
            
    return render(request,"staticapp/reg.html",{'form':form})
def edit_book(request, book_id):
    book = Book.objects.get(pk=book_id)

    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm(instance=book)

    return render(request, 'staticapp/edit_book.html', {'form': form, 'book': book})
