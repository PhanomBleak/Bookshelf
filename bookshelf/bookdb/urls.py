from django.urls import path,re_path
from . import views
from django.conf.urls import include, url

urlpatterns = [
	path('', views.index , name = 'index'),
    path('authors/', views.authors, name='authors'),
    path('books/',views.list_of_books, name = 'books'),
    path('addauthor/',views.add_author , name = 'addauthor'),
	path('addbook/',views.add_book , name = 'addbook'),
    path('details/<str:author_name>/', views.details, name='details'),
]