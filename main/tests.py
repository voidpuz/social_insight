from django.test import TestCase
from main.models import Hashtag, Post, Comment, Reaction, User
from django.db.models import Count, F


class MainTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        user = User.objects.create_user(username='user1', password='password')
        user2 = User.objects.create_user(username='user2', password='password')
        user3 = User.objects.create_user(username='user3', password='password')
        user4 = User.objects.create_user(username='user4', password='password')
        user5 = User.objects.create_user(username='user5', password='password')
        user6 = User.objects.create_user(username='user6', password='password')
        user7 = User.objects.create_user(username='user7', password='password')
        user8 = User.objects.create_user(username='user8', password='password')
        user9 = User.objects.create_user(username='user9', password='password')

        hashtag1 = Hashtag.objects.create(name='Django')
        hashtag2 = Hashtag.objects.create(name='Python')
        hashtag3 = Hashtag.objects.create(name='C++')

        post1 = Post.objects.create(author=user, content='Hello, Django!', hashtags=[hashtag1])
        post2 = Post.objects.create(author=user2, content='Hello, Python!', hashtags=[hashtag2])
        post3 = Post.objects.create(author=user3, content='Hello, C++!', hashtags=[hashtag3])
        post4 = Post.objects.create(author=user4, content='Hello, Django!', hashtags=[hashtag1])
        post5 = Post.objects.create(author=user5, content='Hello, Python!', hashtags=[hashtag2])
        post6 = Post.objects.create(author=user6, content='Hello, C++!', hashtags=[hashtag3])
        post7 = Post.objects.create(author=user7, content='Hello, Django!', hashtags=[hashtag1])
        post8 = Post.objects.create(author=user8, content='Hello, Python!', hashtags=[hashtag2])
        post9 = Post.objects.create(author=user9, content='Hello, C++!', hashtags=[hashtag3])

        comment1 = Comment.objects.create(user=user, post=post1, content='Hello, Django!')
        comment2 = Comment.objects.create(user=user2, post=post2, content='Hello, Python!')
        comment3 = Comment.objects.create(user=user3, post=post3, content='Hello, C++!')
        comment4 = Comment.objects.create(user=user4, post=post4, content='Hello, Django!')
        comment5 = Comment.objects.create(user=user5, post=post5, content='Hello, Python!')
        comment6 = Comment.objects.create(user=user6, post=post6, content='Hello, C++!')
        comment7 = Comment.objects.create(user=user7, post=post7, content='Hello, Django!')
        comment8 = Comment.objects.create(user=user8, post=post8, content='Hello, Python!')

        reaction1 = Reaction.objects.create(user=user, post=post1, type='like')
        reaction2 = Reaction.objects.create(user=user2, post=post2, type='like')
        reaction3 = Reaction.objects.create(user=user3, post=post3, type='like')
        reaction4 = Reaction.objects.create(user=user4, post=post4, type='like')
        reaction5 = Reaction.objects.create(user=user5, post=post5, type='like')
        reaction6 = Reaction.objects.create(user=user6, post=post6, type='like')
        reaction7 = Reaction.objects.create(user=user7, post=post7, type='like')
        reaction8 = Reaction.objects.create(user=user8, post=post8, type='like')

    # Actual Tests
    def test_post_with_likes(self):
        pass
