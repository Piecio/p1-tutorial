from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


# Create your models here.
class PublishedManager(models.Manager):
    def get_queryset(self):
        return super(PublishedManager,self).get_queryset().filter(status='published')

class Post(models.Model):
    STATUS_CHOICES = (
        ('draft',"Roboczy"),
        ('published','Opublikowany'),
    )
    title=models.CharField(max_length=250)
    slug=models.SlugField(max_length=80, unique_for_date='publish',help_text="A short label, generally used in URLs.")
    author=models.ForeignKey(User,related_name='blog_posts',on_delete=models.DO_NOTHING)
    short_description=models.TextField(max_length=450)
    body=models.TextField()
    publish=models.DateTimeField(default=timezone.now)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)
    status=models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')
    objects = models.Manager() # Menedżer domyślny.
    published = PublishedManager() # Menedżer niestandardowy.

    class Meta:
     ordering = ('-publish',)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:post_detail',
                       args=[self.publish.year,
                             self.publish.strftime('%m'),
                             self.publish.strftime('%d'),
                             self.slug])




