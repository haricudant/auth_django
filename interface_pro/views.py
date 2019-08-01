from django.shortcuts import render, HttpResponse
from django.contrib.auth.decorators import login_required
from interface_app.models import Book, Author, BookInstance, Genre
from django.views import generic

@login_required()
def home(request):
        """View function for home page of site."""

        # Generate counts of some of the main objects
        num_books = Book.objects.all().count()
        num_instances = BookInstance.objects.all().count()

        # Available books (status = 'a')
        num_instances_available = BookInstance.objects.filter(status__exact='a').count()

        # The 'all()' is implied by default.
        num_authors = Author.objects.count()

        context = {
            'num_books': num_books,
            'num_instances': num_instances,
            'num_instances_available': num_instances_available,
            'num_authors': num_authors,
        }

        # Render the HTML template index.html with the data in the context variable
        return render(request, 'home.html', context=context)
