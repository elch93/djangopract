from django.shortcuts import render, HttpResponse, redirect, reverse, get_object_or_404
from .models import Book, Author
from .forms import BookForm, AuthorForm
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib import messages

# Create your views here.
def index(request):
    books = Book.objects.all()
    authors = Author.objects.all()
    return render(request, 'books/index.template.html',{'books':books, 'authors': authors})

@login_required
def create_book(request):
    if request.method == 'GET':
        create_form = BookForm()
        return render(request, 'books/create.template.html',{
            'form':create_form
        })
    elif request.method == 'POST':
        create_form = BookForm(request.POST)

        if create_form.is_valid():
            saved_form = create_form.save()
            messages.success(request, f"New Book '{saved_form.title}' has been created!")
            return redirect(reverse(index))
        else:
            return render(request, 'books/create.template.html', {
                'form': create_form
            })

def create_author(request):
    if request.method == 'GET':
        create_form = AuthorForm()
        return render(request, 'books/create.template.html', {
            'form': create_form
        })
    elif request.method == 'POST':
        create_form = AuthorForm(request.POST)
        if create_form.is_valid():
            saved_form = create_form.save()
            messages.success(request, f"New Author '{saved_form.first_name}' has been created!")
            return redirect(reverse(index))
        else:
            return render(request, 'books/create.template.html', {
                'form': create_form
            })

def update_book(request, dataid):
    book_being_updated = get_object_or_404(Book, pk=dataid)
    if request.method == 'POST':
        book_form = BookForm(request.POST, instance=book_being_updated)
        if book_form.is_valid():
            saved_form = book_form.save()
            messages.success(request, f"Book '{saved_form.title}' has been updated!")
            return redirect(reverse(index))
        else:
            return render(request, 'books/create.template.html', {
                'form': book_form
            })

    book_form = BookForm(instance=book_being_updated)
    return render(request, 'books/create.template.html', {
                'form': book_form
            })

def update_author(request, dataid):
    author_being_updated = get_object_or_404(Author, pk=dataid)
    if request.method == 'POST':
        author_form = AuthorForm(request.POST, instance=author_being_updated)
        if author_form.is_valid():
            saved_form = author_form.save()
            messages.success(request, f"Author '{saved_form.first_name}' has been updated!")
            return redirect(reverse(index))
        else:
            return render(request, 'books/create.template.html', {
                'form': author_form
            })
    author_form = AuthorForm(instance=author_being_updated)
    return render(request, 'books/create.template.html', {
                'form': author_form
            })

def delete_book(request, dataid):
    book_to_delete = get_object_or_404(Book, pk=dataid)
    if request.method == 'POST':
        saved_form = book_to_delete.delete()
        messages.success(request, f"Book '{book_to_delete.title}' has been deleted")

        return redirect(reverse(index))
    else:
        return render(request, 'books/delete.template.html', {
            'form': book_to_delete
        })

def delete_author(request, dataid):
    author_to_delete = get_object_or_404(Author, pk=dataid)
    if request.method == 'POST':
        saved_form = author_to_delete.delete()
        messages.success(request, f"Author '{author_to_delete.first_name}' has been deleted")
        return redirect(reverse(index))
    else:
        return render(request, 'books/delete.template.html', {
            'form': author_to_delete
        }) 