from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from taggit.managers import TaggableManager


#
# class PublishedManager(models.Manager):
#     def get_queryset(self):
#         return super(PublishedManager, self).get_queryset().filter(status='published')

class PMGR(models.Manager):
    def get_queryset(self):
        # obj = super(PMGR,self).get_queryset().filter(status='published')
        return super(PMGR, self).get_queryset().filter(status='published')
        # return super(PMGR, self).get_queryset().filter(status='draft')


class Post(models.Model):
    STATUS_CHOICES = (('draft', 'Draft'), ('published', 'Published'),)
    title = models.CharField(max_length=250)
    # slug = models.SlugField(max_length=250, unique_for_date='publish')

    slug = models.SlugField(max_length=250, unique='title')

    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)

    created = models.DateTimeField(auto_now_add=True)  # automatically added when object was created
    updated = models.DateTimeField(auto_now=True)  # automatically added each time saved

    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')

    objects = models.Manager()  # The default manager.
    # published = PublishedManager()  # Our custom manager.
    published = PMGR()  # Our custom manager.

    tags = TaggableManager()

    class Meta:
        ordering = ('-publish',)

    def __str__(self):
        return self.title

    # def get_absolute_url(self):
    #     return reverse('blog:post_detail',
    #                    args=[self.publish.year,
    #                          self.publish.month,
    #                          self.publish.day,
    #                          self.slug])

    def get_absolute_url(self):
        return reverse('blog:post_detail', args=[self.slug])


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')

    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ('created',)

    def __str__(self):
        return 'Comment by {} on {}'.format(self.name, self.post)
