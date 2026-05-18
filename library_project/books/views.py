from django.shortcuts import render, redirect, get_object_or_404
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Author, Book
from .serializers import AuthorSerializer, BookSerializer


# ============= API ViewSets (REST Framework) =============
class AuthorViewSet(viewsets.ModelViewSet):
    """API endpoint for managing Authors"""
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class BookViewSet(viewsets.ModelViewSet):
    """API endpoint for managing Books with filtering"""
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    
    @action(detail=False, methods=['get'])
    def available(self, request):
        """Get only available books"""
        available_books = Book.objects.filter(available=True)
        serializer = self.get_serializer(available_books, many=True)
        return Response(serializer.data)


# ============= Web Views (HTML Templates) =============
def index(request):
    """Home page"""
    books_count = Book.objects.count()
    authors_count = Author.objects.count()
    available_count = Book.objects.filter(available=True).count()
    
    context = {
        'books_count': books_count,
        'authors_count': authors_count,
        'available_count': available_count,
    }
    return render(request, 'books/index.html', context)


def books_list(request):
    """List all books with search functionality"""
    books = Book.objects.all().select_related('author')
    
    # Search functionality
    search_query = request.GET.get('search', '')
    if search_query:
        books = books.filter(title__icontains=search_query)
    
    # Filter by availability
    available_filter = request.GET.get('available', '')
    if available_filter:
        books = books.filter(available=available_filter == 'true')
    
    context = {
        'books': books,
        'search_query': search_query,
    }
    return render(request, 'books/books_list.html', context)


def add_book(request):
    """Add a new book"""
    authors = Author.objects.all()
    
    if request.method == 'POST':
        title = request.POST.get('title')
        author_id = request.POST.get('author')
        published = request.POST.get('published')
        isbn = request.POST.get('isbn')
        available = request.POST.get('available') == 'on'
        
        if title and author_id and published and isbn:
            author = get_object_or_404(Author, id=author_id)
            Book.objects.create(
                title=title,
                author=author,
                published=published,
                isbn=isbn,
                available=available
            )
            return redirect('books_list')
    
    context = {'authors': authors}
    return render(request, 'books/add_book.html', context)


def edit_book(request, pk):
    """Edit an existing book"""
    book = get_object_or_404(Book, pk=pk)
    authors = Author.objects.all()
    
    if request.method == 'POST':
        book.title = request.POST.get('title', book.title)
        book.author_id = request.POST.get('author', book.author_id)
        book.published = request.POST.get('published', book.published)
        book.isbn = request.POST.get('isbn', book.isbn)
        book.available = request.POST.get('available') == 'on'
        book.save()
        return redirect('books_list')
    
    context = {
        'book': book,
        'authors': authors,
    }
    return render(request, 'books/edit_book.html', context)


def delete_book(request, pk):
    """Delete a book"""
    book = get_object_or_404(Book, pk=pk)
    
    if request.method == 'POST':
        book.delete()
        return redirect('books_list')
    
    context = {'book': book}
    return render(request, 'books/delete_book.html', context)
