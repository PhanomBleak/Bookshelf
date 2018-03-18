from django.http import HttpResponse,HttpResponseRedirect
from .models import Author,Book
from django.shortcuts import render,redirect
from django.utils import timezone
import datetime
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt

def index(request):
	now = datetime.datetime.now()
	context = {
		'time' : now
	}
	return render(request, 'bookdb/index.html',context)
def authors(request):
	author_list = Author.objects.all()
	context = {
		'author_list' :author_list
	}
	return render(request, 'bookdb/authors.html',context)

def list_of_books(request):
	book_list = Book.objects.all()
	context = {
		'book_list' :book_list
	}
	return render(request, 'bookdb/books.html',context)
@csrf_exempt
def add_author(request):
	if  request.method == 'POST':
		new_name = request.POST['authorname_repeat']
		new_author = Author(name = new_name)
		new_author.save(force_insert=True)
		messages.add_message(request,messages.INFO,'Author added succesfully!')
		return HttpResponseRedirect("/")
	elif request.method == 'GET':
		return render(request , 'bookdb/addauthor.html')
@csrf_exempt
def add_book(request):
	if  request.method == 'POST':
		auth_name = request.POST['authorname']
		book_name = request.POST['bookname']
		author = Author.objects.filter(name = auth_name)
		book = Book.objects.filter(name = book_name)
		if len(author) != 0 and len(book) == 0:
			author[0].book_set.create(name = book_name)
			messages.add_message(request,messages.INFO,'Book added succesfully!')
			return HttpResponseRedirect("/")
		elif len(author) == 0:
			messages.add_message(request,messages.INFO,'Author does not exist')
			return HttpResponseRedirect("/")
		elif len(book) != 0:
			messages.add_message(request , messages.INFO ,'Be creative ! chose a new name ! book name exists')
			return HttpResponseRedirect("/")
	else:
		return render(request , 'bookdb/addbook.html')
def details(request,author_name):
	if request.method == 'GET':
		author_detail = Author.objects.filter(name = author_name)
		book_list = Book.objects.filter(author = author_detail[0])
		book_list.update()
		context = {
			'book_list' : book_list
		}
		return render(request , 'bookdb/details.html',context)