from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from .models import Book

def book_list(request):
    books = Book.objects.all()
    return render(request, 'book/list.html', {'books' : books})


def book_detail(request, id):
    book = get_object_or_404(Book, id = id)
    return render(request, 'book/detail.html', {'book' : book})


def search_books(request):
    pass


def add_book(request):
    pass  


def edit_book(request, pk):
    pass


def delete_book(request, pk):
    pass


def filter_books(request):
    pass


def delete_filtered_books(request):
    pass 