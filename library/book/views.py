from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, Http404
from .models import *
from .forms import AddBookForm, EditBookForm

def book_list(request):
    books = Book.objects.all()
    return render(request, 'book/list.html', {'books' : books})


def book_detail(request, id):
    book = get_object_or_404(Book, id = id)
    return render(request, 'book/detail.html', {'book' : book})


def search_books(request):
    pass


def add_book(request):
    context = {}
    if request.method == 'POST':
        form = AddBookForm(request.POST)
        if form.is_valid():
            author = form.cleaned_data['author']
            new_author_name = form.cleaned_data['new_author']
            price = form.cleaned_data['price']
            new_price_value = form.cleaned_data['new_price']

            if not author and new_author_name:
                author, created = Author.objects.get_or_create(name=new_author_name)

            if not price and new_price_value:
                price, created = Price.objects.get_or_create(price=new_price_value)

            book = form.save(commit=False)
            book.author = author
            book.price = price
            book.save()
    else:
        form = AddBookForm()

    context['form']=form
    return render(request, 'book/add.html', context)


def edit_book(request, id):
    context = {}
    book = get_object_or_404(Book, id=id)
    if request.method == 'POST':
        form = EditBookForm(request.POST, instance=book)
        if form.is_valid():
            new_author_name = form.cleaned_data['author']
            new_price_value = form.cleaned_data['price']

            author, created = Author.objects.get_or_create(name=new_author_name)

            price, created = Price.objects.get_or_create(price=new_price_value)

            book.name = form.changed_data['name']
            book.author = author
            book.price = price
            book.category = form.changed_data['category']

            book.save()
    else:
        form = EditBookForm(instance=book)

    context['form']=form
    context['book']=book
    return render(request, 'book/edit.html', context)
    


def delete_book(request, pk):
    pass


def filter_books(request):
    pass


def delete_filtered_books(request):
    pass 