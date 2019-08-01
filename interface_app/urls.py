from django.contrib import admin
from django.urls import path, include,re_path
from .views import BookDetailView, BookListView,BookInstance
from .views import BookListView, BookDetailView
from interface_app.views import loginView, logout_view, register_view

urlpatterns = [
    # path('', views.index, name='index'),

    path('books/', BookListView.as_view(), name='books'),
    path('book/<int:pk>', BookDetailView.as_view(), name='book-detail'),

]