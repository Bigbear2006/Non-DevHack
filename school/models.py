from django.db import models


class News(models.Model):
    title = models.CharField(max_length=255, unique=True)
    url = models.SlugField()
    image = models.ImageField(upload_to='news_images/', blank=True)
    date = models.DateField(auto_now_add=True)
    text = models.TextField()

    def get_about_text(self):
        return str(self.text[:50]).strip()

    def __str__(self):
        return self.title


class Teacher(models.Model):
    name = models.CharField(max_length=255, unique=True)
    url = models.SlugField()
    role = models.CharField(max_length=255)
    floor = models.PositiveIntegerField()
    cabinet = models.CharField(max_length=10)
    phone = models.CharField(max_length=25)
    email = models.EmailField()

    def __str__(self):
        return self.name


class Subject(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    training_level = models.CharField(max_length=100)
    USE = models.CharField(max_length=255)

    def __str__(self):
        return self.name
