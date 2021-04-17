from django.db import models

# Create your models here.

choices=[
    ('py','Python'),
    ('cs','CSS'),
    ('pe','Personal'),
    ('wd','Web Development'),
]

class Entry(models.Model):
    time = models.DateField(auto_now=True, verbose_name="Date Entered")
    title = models.CharField(max_length=100, verbose_name="Title")
    cat = models.CharField(max_length=50,choices=choices, verbose_name="Category")
    blogslug = models.SlugField( verbose_name="Slug",null=True)
    blog = models.TextField(max_length=2000, verbose_name="Main Text")
    image = models.ImageField(upload_to='blog_photos/', verbose_name="Blog Page Image",null=True)

    def __str__(self):
        return self.title
