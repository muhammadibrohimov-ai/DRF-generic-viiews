import math

from rest_framework import serializers
from .models import Book, Author
from datetime import datetime as dt

class AuthorSerializer(serializers.ModelSerializer):
    """Model Serializer class for Author model"""
    class Meta:
        model = Author
        fields = '__all__'
        read_only_fields = ['id', 'created_at']
        extra_kwargs = {
            'fullname': {
                'required': True,
                'help_text': 'Please enter author\'s full name!',
                'max_length': 50,
                'trim_whitespace': True,
            },
            'year': {
                'required': True,
                'min_value': 1000,
                'max_value': dt.now().year,
            },
            'country': {
                'required': True,
                'help_text': 'Please enter author\'s country name!',
                'max_value': 50,
                'trim_whitespace': True,
            },
        }

    def validate_fullname(self, value):
        """Field-level validation for fullname field"""
        value = value.lower().strip()
        if not value:
            raise serializers.ValidationError('The fullname field is required and can\'t be empty!')
        if value.isdigit():
            raise serializers.ValidationError('The fullname cannot consist of numeric values!')
        if len(value) < 2:
            raise serializers.ValidationError('The fullname field should have at least 2 characters!')

        return value

    def validate_year(self, value):
        """Field-level validation for year field"""
        value = int(value)
        if not value:
            raise serializers.ValidationError('The year filed must be included!')
        if value <= 0:
            raise serializers.ValidationError('The year field must be positive integer!')
        if value <= 1000 or value > dt.now().year:
            raise serializers.ValidationError('The year field must be between 1000 and current year!')

        return value

    def validate_country(self, value):
        """Field-level validation for country field"""
        value = value.lower().strip()
        if not value:
            raise serializers.ValidationError('The country field is required and can\'t be empty!')
        if value.isdigit():
            raise serializers.ValidationError('The country cannot consist of numeric values!')
        if len(value) < 2:
            raise serializers.ValidationError('The country field should have at least 2 characters!')

        return value

    def validate(self, attrs):
        fullname = attrs.get('fullname', '').lower().strip()
        year = attrs.get('year')
        country = attrs.get('country', '').lower().strip()

        authors = Author.objects.filter(
            fullname__exact=fullname,
            year = year,
            country__iexact=country,
        )

        if self.instance:
            authors = authors.exclude(pk=self.instance.pk)

        if authors.exists():
            raise serializers.ValidationError('Author with this name, year, country already exists!')

        return attrs


class BookSerializer(serializers.ModelSerializer):

    author_id = serializers.PrimaryKeyRelatedField(
        queryset=Author.objects.all(),
        source='author',
        write_only=True,
        help_text='Enter author id please',
    )

    class Meta:
        model = Book
        fields = '__all__'
        read_only_fields = ['id', 'created_at']
        extra_kwargs = {
            'name': {
                'required': True,
                'max_length': 150,
                'help_text': 'Please enter book name',
                'trim_whitespace': True,
            },
            'desc': {
                'required': False,
                'max_length': 2000,
                'help_text': 'Enter book description (optional)!',
                'trim_whitespace': True,
            },
            'year': {
                'required': True,
                'min_value': 1000,
                'max_value': dt.now().year,
            },
            'price': {
                'required': True,
                'min_value': 1,
            },
        }

    def validate_name(self, value):
        """Field-level validation for name field"""
        value = value.lower().strip()
        if not value:
            raise serializers.ValidationError('The name field is required and can\'t be empty!')
        if value.isdigit():
            raise serializers.ValidationError('The name cannot consist of numeric values!')
        if len(value) < 2:
            raise serializers.ValidationError('The name field should have at least 2 characters!')

        return value

    def validate_year(self, value):
        """Field-level validation for year field"""
        value = int(value)
        if not value:
            raise serializers.ValidationError('The year filed must be included!')
        if value <= 0:
            raise serializers.ValidationError('The year field must be positive integer!')
        if value <= 1000 or value > dt.now().year:
            raise serializers.ValidationError('The year field must be between 1000 and current year!')

        return value

    def validate_price(self, value):
        """Field-level validation for price field"""
        value = int(value)
        if not value:
            raise serializers.ValidationError('The price filed must be included!')
        if value <= 0:
            raise serializers.ValidationError('The price field must be positive integer!')

        return value

    def validate(self, attrs):
        author = attrs.get('author')
        year = attrs.get('year')

        if year < author.year:
            raise serializers.ValidationError('The year filed must be higher then author\'s year field!')

        name = attrs.get('name')
        




