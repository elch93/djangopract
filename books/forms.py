from django import forms
from .models import Book, Author

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ('title', 'desc', 'ISBN')


class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ('first_name','last_name','date_of_birth')