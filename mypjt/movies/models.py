from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.core.exceptions import ValidationError
from decimal import Decimal
# Create your models here.

class Movie(models.Model):
    rating = models.DecimalField(
        max_digits=3,
        decimal_places=1,
        validators=[
            MinValueValidator(0),
            MaxValueValidator(5)
            ])
    GENRE_CHOICES = [
    ('action', 'Action'),
    ('comedy', 'Comedy'),
    ('drama', 'Drama'),]
    title = models.CharField(max_length=100)
    description = models.TextField()
    director = models.CharField(max_length=100)
    genre = models.CharField(
    max_length=10,
    choices=GENRE_CHOICES,  # 장르 선택지 설정
    )
    def clean(self):
        super().clean()
        if self.rating % Decimal('0.5') != 0:
            raise ValidationError({'rating': '평점은 0.5 단위로만 입력할 수 있습니다.'})
    
    def __str__(self):
        return self.title

class Comment(models.Model):
    movie = models.ForeignKey(Movie, related_name="comments", on_delete=models.CASCADE)
    content = models.TextField()

    def __str__(self):
        return f"Comment on {self.movie.title}"
    