from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Book
from .serializers import BookSerializer
from rest_framework.viewsets import ModelViewSet


# class BookSelectView(generics.ListAPIView, generics.RetrieveAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer


class BookSelectView(APIView):
    def get(self, request, pk=None):
        if pk:
            try:
                book = Book.objects.get(pk=pk)
                serializer = BookSerializer(book)
                return Response({"status": "success", "book": serializer.data})
            except Exception:
                return Response(
                    {"status": "error", "message": "Kitob topilmadi"},
                    status=status.HTTP_404_NOT_FOUND,
                )

        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        return Response({"status": "success", "books": serializer.data})


# class BookCreateView(generics.CreateAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer


class BookCreateView(APIView):
    def post(self, request):
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {"status": "success", "book": serializer.data},
                status=status.HTTP_201_CREATED,
            )
        return Response(
            {"status": "error", "errors": serializer.errors},
            status=status.HTTP_400_BAD_REQUEST,
        )


# class BookUpdateView(generic.UpdateApiView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer


class BookUpdateView(APIView):
    def put(self, request, pk):
        try:
            book = Book.objects.get(pk=pk)
            serializer = BookSerializer(book, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({"status": "success", "book": serializer.data})
            return Response(
                {"status": "error", "errors": serializer.errors},
                status=status.HTTP_400_BAD_REQUEST,
            )
        except Exception:
            return Response(
                {"status": "error", "message": "Kitob topilmadi"},
                status=status.HTTP_404_NOT_FOUND,
            )

    def patch(self, request, pk):
        try:
            book = Book.objects.get(pk=pk)
            serializer = BookSerializer(book, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response({"status": "success", "book": serializer.data})
            return Response(
                {"status": "error", "errors": serializer.errors},
                status=status.HTTP_400_BAD_REQUEST,
            )
        except Exception:
            return Response(
                {"status": "error", "message": "Kitob topilmadi"},
                status=status.HTTP_404_NOT_FOUND,
            )


# class BookDeleteView(generics.RetrieveDestroyAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer


class BookDeleteView(APIView):
    def delete(self, request, pk):
        try:
            book = Book.objects.get(pk=pk)
            book.delete()
            return Response(
                {"status": "success", "message": "Kitob o'chirildi"},
                status=status.HTTP_204_NO_CONTENT,
            )
        except Exception:
            return Response(
                {"status": "error", "message": "Kitob topilmadi"},
                status=status.HTTP_404_NOT_FOUND,
            )




