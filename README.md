# 📚 Library Management System

A simple and clean Django REST Framework-based library management system with a web interface for managing books and authors.

## 🎯 Features

- **REST API** - Full CRUD operations using Django REST Framework
- **Web Interface** - Beautiful and responsive HTML templates
- **Search & Filter** - Search books by title and filter by availability
- **Book Management** - Add, edit, view, and delete books
- **Author Management** - Manage authors through Django Admin
- **Responsive Design** - Works on desktop and mobile devices

## 📋 Project Structure

```
library_project/
├── books/
│   ├── migrations/
│   ├── templates/books/
│   │   ├── base.html              # Base template with CSS & JS
│   │   ├── index.html             # Home page with stats
│   │   ├── books_list.html        # List all books
│   │   ├── add_book.html          # Add new book form
│   │   ├── edit_book.html         # Edit book form
│   │   └── delete_book.html       # Delete confirmation
│   ├── admin.py                   # Django admin configuration
│   ├── apps.py
│   ├── models.py                  # Book & Author models
│   ├── serializers.py             # DRF serializers
│   ├── views.py                   # API views & web views
│   ├── urls.py                    # App URL routing
│   └── tests.py
├── library_project/
│   ├── settings.py                # Django settings
│   ├── urls.py                    # Main URL configuration
│   ├── wsgi.py
│   └── asgi.py
├── db.sqlite3                     # SQLite database
├── manage.py
└── README.md
```

## 🚀 Quick Start

### 1. Run Migrations
```bash
python manage.py migrate
```

### 2. Create Superuser (Optional - for Admin Panel)
```bash
python manage.py createsuperuser
```

### 3. Run Development Server
```bash
python manage.py runserver
```

The application will be available at `http://localhost:8000/`

## 📖 Usage

### Web Interface Routes

| URL | Description |
|-----|-------------|
| `/` | Home page with library statistics |
| `/books/` | List all books |
| `/books/add/` | Add new book form |
| `/books/<id>/edit/` | Edit existing book |
| `/books/<id>/delete/` | Delete book confirmation |

### REST API Routes

Base URL: `http://localhost:8000/api/`

#### Books Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/api/books/` | Get all books |
| POST | `/api/books/` | Create new book |
| GET | `/api/books/{id}/` | Get book details |
| PUT | `/api/books/{id}/` | Update book |
| DELETE | `/api/books/{id}/` | Delete book |
| GET | `/api/books/available/` | Get available books only |

#### Authors Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/api/authors/` | Get all authors |
| POST | `/api/authors/` | Create new author |
| GET | `/api/authors/{id}/` | Get author details |
| PUT | `/api/authors/{id}/` | Update author |
| DELETE | `/api/authors/{id}/` | Delete author |

## 🔌 API Examples

### Get All Books
```bash
curl http://localhost:8000/api/books/
```

### Create Book (requires author to exist first)
```bash
curl -X POST http://localhost:8000/api/books/ \
  -H "Content-Type: application/json" \
  -d '{
    "title": "Django for Beginners",
    "author": 1,
    "published": "2024-01-15",
    "isbn": "1234567890123",
    "available": true
  }'
```

### Update Book
```bash
curl -X PUT http://localhost:8000/api/books/1/ \
  -H "Content-Type: application/json" \
  -d '{
    "title": "Updated Title",
    "author": 1,
    "published": "2024-01-15",
    "isbn": "1234567890123",
    "available": false
  }'
```

### Delete Book
```bash
curl -X DELETE http://localhost:8000/api/books/1/
```

### Get Available Books Only
```bash
curl http://localhost:8000/api/books/available/
```

## 📊 Database Models

### Author Model
- `name` (CharField) - Author's full name
- `bio` (TextField) - Author's biography (optional)

### Book Model
- `title` (CharField) - Book title
- `author` (ForeignKey) - Reference to Author
- `published` (DateField) - Publication date
- `isbn` (CharField) - 13-digit unique ISBN
- `available` (BooleanField) - Availability status

## 🎨 Features in Detail

### Web Interface
- **Modern Design** - Clean and professional UI with gradient backgrounds
- **Search Functionality** - Real-time search by book title
- **Filter Options** - Filter books by availability status
- **Form Validation** - Client-side and server-side validation
- **Responsive Layout** - Mobile-friendly design
- **Statistics Dashboard** - View library statistics on homepage

### REST API
- **Serializers** - Full data serialization with nested author information
- **ViewSets** - DRF ModelViewSet for standard CRUD operations
- **Custom Actions** - Filter available books through custom API endpoint
- **Browsable API** - Use Django REST Framework's browsable API interface

## 🔧 Customization Tips

### Add More Fields to Book Model
Edit `books/models.py`:
```python
class Book(models.Model):
    # ... existing fields ...
    pages = models.IntegerField(default=0)
    price = models.DecimalField(max_digits=6, decimal_places=2, default=0)
```

Then update serializer and create migration:
```bash
python manage.py makemigrations
python manage.py migrate
```

### Add Authentication to API
In `settings.py`:
```python
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.TokenAuthentication',
    ],
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',
    ]
}
```

### Add Pagination
In `settings.py`:
```python
REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 10
}
```

## 📝 Admin Panel

Access Django Admin at `http://localhost:8000/admin/`

- Username: (your superuser username)
- Password: (your superuser password)

Add, edit, or delete books and authors directly from the admin panel.

## 🐛 Troubleshooting

**Port 8000 already in use:**
```bash
python manage.py runserver 8001
```

**Template not found error:**
- Ensure templates directory exists: `books/templates/books/`
- Clear browser cache and hard refresh

**ISBN validation error:**
- ISBN must be 10 or 13 digits
- Ensure no duplicate ISBNs exist

## 📚 Dependencies

- Django 6.0.5
- djangorestframework
- Python 3.8+

## 🎓 Learning Resources

- [Django Documentation](https://docs.djangoproject.com/)
- [Django REST Framework Guide](https://www.django-rest-framework.org/)
- [Django Templates](https://docs.djangoproject.com/en/6.0/topics/templates/)

## 📄 License

Open source project for educational purposes.

---

**Built with ❤️ as a simple library management system**
