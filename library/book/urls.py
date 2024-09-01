from django.urls import path
from . import views

app_name = 'book'

urlpatterns = [
    path('books/', views.book_list, name='book_list'),
    path('books/<int:id>', views.book_detail, name='book_detail'),
    path('search/', views.search_books, name='search_books'),
    path('books/add/', views.add_book, name='add_book'),
    path('books/<int:id>/edit/', views.edit_book, name='edit_book'),
    path('books/<int:id>/delete/', views.delete_book, name='delete_book'),
    path('filter', views.filter_books, name='filter_books'),
    path('delete_filtered', views.delete_filtered_books, name='delete_filtered_books'),
]