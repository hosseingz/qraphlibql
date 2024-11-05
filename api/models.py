from django.db import models
from django.utils import timezone


class Author(models.Model):
    first_name = models.CharField(max_length=128)
    last_name = models.CharField(max_length=128)
    date_of_birth = models.DateField(null=True, blank=True)
    date_of_death = models.DateField('Died', null=True, blank=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    class Meta:
        ordering = ['date_of_birth']
        indexes = [
            models.Index(fields=['date_of_birth'])
        ]
    
    @property
    def age(self):
        if self.date_of_birth:
            return timezone.now().year - self.date_of_birth.year
        return None


class Genre(models.Model):
    name = models.CharField(max_length=64, unique=True)

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=128)
    author = models.ForeignKey(Author, on_delete=models.SET_NULL, null=True)
    summary = models.TextField(max_length=1024, help_text='Enter a brief description of the book')
    genre = models.ManyToManyField(Genre)
    published_date = models.DateField(null=True, blank=True)
    page_count = models.PositiveIntegerField(null=True, blank=True)

    def __str__(self):
        return f'{self.title} by {self.author}'

    class Meta:
        ordering = ['published_date']
        indexes = [
            models.Index(fields=['title']),
            models.Index(fields=['author']),
            models.Index(fields=['published_date']),
        ]
