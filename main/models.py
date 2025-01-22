from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone


class User(AbstractUser):
    bio = models.TextField(blank=True, null=True)
    pic = models.ImageField(upload_to='profile_pics/', blank=True, null=True)
    followers = models.ManyToManyField('self', symmetrical=False, related_name='following')

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'

    def __str__(self):
        return self.username


class Post(models.Model):
    author = models.ForeignKey("main.User", on_delete=models.CASCADE, related_name="posts")
    content = models.TextField()
    hashtags = models.ManyToManyField("main.Hashtag", related_name="posts")
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'

    def __str__(self):
        return self.content[:20]


class Comment(models.Model):
    user = models.ForeignKey("main.User", on_delete=models.CASCADE, related_name="comments")
    post = models.ForeignKey("main.Post", on_delete=models.CASCADE, related_name="comments")
    content = models.TextField()
    parent_comment = models.ForeignKey("self", on_delete=models.CASCADE, null=True, blank=True, related_name="replies")
    created_at = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'

    def __str__(self):
        return self.content
    

class Reaction(models.Model):
    REACTION_TYPES = [
        ('like', 'Like'),
        ('love', 'Love'),
        ('haha', 'Haha'),
        ('wow', 'Wow'),
        ('sad', 'Sad'),
        ('angry', 'Angry'),
    ]
    user = models.ForeignKey("main.User", on_delete=models.CASCADE, related_name="reactions")
    post = models.ForeignKey("main.Post", on_delete=models.CASCADE, related_name="reactions", blank=True, null=True)
    comment = models.ForeignKey("main.Comment", on_delete=models.CASCADE, related_name="reactions", blank=True, null=True)
    type = models.CharField(max_length=10, choices=REACTION_TYPES)
    created_at = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Reaction'
        verbose_name_plural = 'Reactions'

    def __str__(self):
        return self.type
    

class Hashtag(models.Model):
    name = models.CharField(max_length=50, unique=True)
    created_at = models.DateTimeField(default=timezone.now)

    class Meta:
        verbose_name = 'Hashtag'
        verbose_name_plural = 'Hashtags'

    def __str__(self):
        return self.name