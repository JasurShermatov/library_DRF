from django.core.exceptions import ValidationError
from rest_framework import serializers
from .models import Book


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ("id", "title", "subtitle", "content", "author", "isbn", "price")


    def validate(self, data):
        title = data.get("title", None)
        author = data.get("author", None)

        if not title.isalpha():
            raise ValidationError(
                {
                    'status': False,
                    'message': "Kitob sarlvhasi harflardan tashkil topishi kerak!"
                }
            )

        if Book.objects.filter(title=title, author=author).exists():
            raise ValidationError(
                {
                    'status': False,
                    'message':"Kitob sarlavhasi va auithori bir xil botni post qila olmaysiz!"
                }
            )
        return data

    def validate_price(self, price):
        if price < 0 or price > 10000000:
            raise ValidationError(
                {
                    'status': False,
                    'message': "kitob narsi 0 dan katta bo'lisi va 10 ml dan kichik bo'lishi kerak"
                }
            )