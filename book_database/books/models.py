from django.db import models
from django.utils.text import slugify

# Create your models here.
class Book(models.Model):

    name = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    book_cover = models.ImageField(upload_to="book_covers/")
    price = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.BooleanField(default=True)
    slug = models.SlugField(unique=True, blank=True, null=True)

    def save(self, *args, **kwargs):
        # Generate a slug based on the book name
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name