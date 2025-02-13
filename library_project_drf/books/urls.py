from django.urls import path


from .views import BookSelectView, BookCreateView, BookUpdateView, BookDeleteView

urlpatterns = [
    path("books/", BookSelectView.as_view(), name="book-list"),
    path("books/<int:pk>/", BookSelectView.as_view(), name="book-detail"),
    path("books/create/", BookCreateView.as_view(), name="book-create"),
    path("books/<int:pk>/update/", BookUpdateView.as_view(), name="book-update"),
    path("books/<int:pk>/delete/", BookDeleteView.as_view(), name="book-delete"),
]
