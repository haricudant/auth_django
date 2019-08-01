import sys

from django.shortcuts import render,redirect, HttpResponse
from django.views import generic
from interface_app.models import Book, Author, BookInstance, Genre
from django.shortcuts import get_object_or_404, Http404


from django.contrib.auth import(

    authenticate,
    get_user_model,
    login,
    logout

)


from .forms import UserLoginForm, UserRegisterForm


def loginView(request):
    next = request.GET.get('next') ##
    form =UserLoginForm(request.POST or None)
    if form.is_valid():
        username =form.cleaned_data.get('username')
        password =  form.cleaned_data.get('password')
        user  =authenticate(username=username, password = password)
        login(request, user)
        if next:
            return redirect(next)
        return redirect('/')

    context ={
        'form' :form,
    }
    return render(request, "login.html", context)


def register_view(request):
    next = request.GET.get('next')
    form =UserRegisterForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        password = form.cleaned_data.get('password')
        user.set_password (password)
        user.save()
        new_user =authenticate(username = user.username, password = password)
        login(request, new_user)
        if next:
            return redirect(next)
        return redirect('/')

    context ={
        'form':form

    }
    return render(request, "sign_up.html", context)

# Create your views here.


def logout_view(request):
    logout(request)
    return redirect('/')

def index(request):
    my_dict={'insert_me':"Hello Iam from Views.py"}

class BookListView(generic.ListView):
     model = Book


class BookListView(generic.ListView):
    model = Book
    context_object_name = 'book_list'  # your own name for the list as a template variable
    # queryset = Book.objects.filter(title__icontains='war')[:5]  # Get 5 books containing the title war
    template_name = 'book_list.html'  # Specify your own template name/location

class BookDetailView(generic.DetailView):
    model = Book


    def book_detail_view(request, primary_key):
        try:
            book = Book.objects.get(pk=primary_key)

        except Book.DoesNotExist:
            raise Http404('Book does not exist')

        return render(request, '../templates/book_detail.html', context={'book-detail': book})


