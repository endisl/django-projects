import datetime
from django.contrib.auth.models import User
from django.test import TestCase
from blog.models import Blog, Blogger, Comment


class BloggerModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        user1 = User.objects.create_user(
            username='so-and-so', password='12345')
        user1.save()
        Blogger.objects.create(user=user1, bio='my bio')

    def test_get_absolute_url(self):
        blogger = Blogger.objects.get(id=1)
        self.assertEqual(blogger.get_absolute_url(), '/blog/blogger/1')

    def test_user_label(self):
        blogger = Blogger.objects.get(id=1)
        field_label = blogger._meta.get_field('user').verbose_name
        self.assertEqual(field_label, 'user')

    def test_bio_label(self):
        blogger = Blogger.objects.get(id=1)
        field_label = blogger._meta.get_field('bio').verbose_name
        self.assertEqual(field_label, 'bio')

    def test_bio_max_length(self):
        blogger = Blogger.objects.get(id=1)
        max_length = blogger._meta.get_field('bio').max_length
        self.assertEqual(max_length, 500)

    def test_object_name(self):
        blogger = Blogger.objects.get(id=1)
        expected_object_name = blogger.user.username
        self.assertEqual(expected_object_name, str(blogger))


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
