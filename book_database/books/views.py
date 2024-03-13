from django.shortcuts import render, redirect, get_object_or_404
from .forms import BookForm, StatusChangeForm
from .models import Book

# Create your views here.
def add_book(request):
    if request.method == "POST":
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            #commit == False lets us modify the form before we save it
            book = form.save(commit=False)
            #in this case we set the status acording to the value returned by the button
            book.status = request.POST.get("action") == "have"
            book.save()
            return redirect("add_book")
    else:
        form = BookForm()
    
    books_have = Book.objects.filter(status=True)
    books_want = Book.objects.filter(status=False)

    return render(request, 'books/add_book.html', {'form': form, 'books_have': books_have, 'books_want': books_want})

def book_details(request, slug):
    book = get_object_or_404(Book, slug=slug)
    return render(request, 'books/book_details.html', {'book': book})

def change_status(request, slug):
    book = get_object_or_404(Book, slug=slug)

    if request.method == 'POST':
        form = StatusChangeForm(request.POST)
        if form.is_valid():
            new_status = form.cleaned_data['new_status'] == "have"
            book.status = new_status
            book.save()
            return redirect('book_details', slug=slug)

    return redirect('book_details', slug=slug)

    
