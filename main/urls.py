from django.urls import path
from .views import (
    AllView, 
    SingleAuthorView,
    NewAuthorView,
    UpdateAuhtorView,
    DeleteAuthorView,
    ListBooksView,
    CreateBookView,
    UpdateBookView
)

urlpatterns = [
    path('', AllView.as_view(), name='home'),
    path('author/create/', NewAuthorView.as_view(), name='new_author'),
    path('author/detail/<int:pk>/', SingleAuthorView.as_view(), name='author_detail'),
    path('author/update/<int:pk>/', UpdateAuhtorView.as_view(), name='author_update'),
    path('author/delete/<int:pk>/', DeleteAuthorView.as_view(), name='author_delete'),
    path('book/', ListBooksView.as_view(), name='book'),
    path('book/create/', CreateBookView.as_view(), name='book_create'),
    path('book/detail/<int:pk>/', UpdateBookView.as_view(), name = 'all_detail_book'),
]
