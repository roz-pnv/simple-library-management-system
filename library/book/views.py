from django.shortcuts import render, get_object_or_404, HttpResponseRedirect, redirect
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
    query = request.GET.get('query', None)

    if query:

        book_name_search = Book.objects.filter(name__icontains= query)
        if book_name_search.exists():
            return render(request, 'book/list.html', {'books':book_name_search})
        
        try:
            author = Author.objects.get(name__icontains=query)
            auther_name_search = Book.objects.filter(author=author)
            return render(request, 'book/list.html', {'books':auther_name_search})
        except Author.DoesNotExist:
            return render(request, 'book/list.html', {'books':[]})

    return render(request, 'book/list.html', {'books':Book.objects.all()})



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
            new_author_name = form.cleaned_data['author_name']
            author, _ = Author.objects.get_or_create(name=new_author_name)

            new_price_value = form.cleaned_data['price_amount']
            price, _ = Price.objects.get_or_create(price=int(new_price_value))

            book.author = author
            book.price = price
            book.name = form.cleaned_data['name']
            book.category = form.cleaned_data['category']

            book.save()
            return HttpResponseRedirect("/books")
    else:
        form = EditBookForm(instance=book)

    context['form']=form
    context['book']=book
    return render(request, 'book/edit.html', context)
    


def delete_book(request, id):
    context = {}

    book = get_object_or_404(Book, id=id)

    if request.method == "POST":
        book.delete()
        return HttpResponseRedirect("/books")
        
    return render(request, 'book/delete.html', context)


def filter_books(request):
    price = request.GET.get('price', None)
    published_year = request.GET.get('date', None)
    books = Book.objects.all()

    if price:
        books = books.filter(price__price__lte=int(price))
    if published_year:
        books = books.filter(published_at__year=int(published_year))

    return render(request, 'book/list.html', {'books':books})


def delete_filtered_books(request):
    pass 