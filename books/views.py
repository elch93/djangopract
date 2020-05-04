from django.shortcuts import render, HttpResponse, redirect, reverse
from .models import Book, Author
from .forms import BookForm, AuthorForm

# Create your views here.
def index(request):
    books = Book.objects.all()
    authors = Author.objects.all()
    return render(request, 'books/index.template.html',{'books':books, 'authors': authors})

def create_book(request):
    if request.method == 'GET':
        create_form = BookForm()
        return render(request, 'books/create.template.html',{
            'form':create_form
        })
    elif request.method == 'POST':
        create_form = BookForm(request.POST)

        if create_form.is_valid():
            create_form.save()
            return redirect(reverse(index))
        else:
            return render(request, 'books/create.template.html', {
                'form': create_form
            })

def create_author(request):
    if request.method == 'GET':
        create_form = AuthorForm()
        return render(request, 'books/create_author.template.html',{
            'form':create_form
        })
    elif request.method == 'POST':
        create_form = AuthorForm(request.POST)
        if create_form.is_valid():
            return redirect(reverse(index))
        else:
            return render(request, 'books/create_author.template.html', {
                'form': create_form
            })

    
