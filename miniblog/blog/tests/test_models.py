import datetime
from django.contrib.auth.models import User
from django.test import TestCase
from blog.models import Blog, Blogger, Comment


class BloggerModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        pass

    def test_get_absolute_url(self):
        pass

    def test_user_label(self):
        pass

    def test_bio_label(self):
        pass

    def test_bio_max_length(self):
        pass

    def test_object_name(self):
        pass


class BlogModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        pass

    def test_get_absolute_url(self):
        pass

    def test_title_label(self):
        pass

    def test_title_max_length(self):
        pass

    def test_description_label(self):
        pass

    def test_description_max_length(self):
        pass

    def test_date_label(self):
        pass

    def test_date(self):
        pass

    def test_object_name(self):
        pass


class CommentModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        pass

    def test_description_label(self):
        pass

    def test_description_max_length(self):
        pass

    def test_author_label(self):
        pass

    def test_date_label(self):
        pass

    def test_blog_label(self):
        pass

    def test_object_name(self):
        pass
