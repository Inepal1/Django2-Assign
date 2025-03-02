from .models import BookInstance
from django import forms
from .models import Book, BookInstance


class LoanBookForm(forms.ModelForm):
    """Form for a librarian to loan books."""
    # Disable the book field to prevent user from entering a book
    # book_title is for display purposes only - set required=False
    book_title = forms.CharField(disabled=True, required=False)

    class Meta:
        # display only the book title and the borrower to the librarian
        model = BookInstance
        fields = ('book_title', 'borrower',)

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'summary', 'isbn', 'genre', 'book_image']
        widgets = {
            'genre': forms.CheckboxSelectMultiple(),  # Since genre is a many-to-many field
        }