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
        user1 = User.objects.create_user(
            username='so-and-so', password='12345')
        user1.save()
        author = Blogger.objects.create(user=user1, bio='my bio')
        Blog.objects.create(title='the origin of life',
                            author=author, description="c'est la vie")

    def test_get_absolute_url(self):
        blog = Blog.objects.get(id=1)
        self.assertEqual(blog.get_absolute_url(), '/blog/1')

    def test_title_label(self):
        blog = Blog.objects.get(id=1)
        field_label = blog._meta.get_field('title').verbose_name
        self.assertEqual(field_label, 'title')

    def test_title_max_length(self):
        blog = Blog.objects.get(id=1)
        max_length = blog._meta.get_field('title').max_length
        self.assertEqual(max_length, 200)

    def test_description_label(self):
        blog = Blog.objects.get(id=1)
        field_label = blog._meta.get_field('description').verbose_name
        self.assertEqual(field_label, 'description')

    def test_description_max_length(self):
        blog = Blog.objects.get(id=1)
        max_length = blog._meta.get_field('description').max_length
        self.assertEqual(max_length, 2000)

    def test_date_label(self):
        blog = Blog.objects.get(id=1)
        field_label = blog._meta.get_field('post_date').verbose_name
        self.assertEqual(field_label, 'post date')

    def test_date(self):
        blog = Blog.objects.get(id=1)
        post_date = blog.post_date
        self.assertEqual(post_date, datetime.date.today())

    def test_object_name(self):
        blog = Blog.objects.get(id=1)
        expected_object_name = blog.title
        self.assertEqual(expected_object_name, str(blog))


class CommentModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        user1 = User.objects.create_user(
            username='so-and-so', password='12345')
        user1.save()
        user2 = User.objects.create_user(
            username='comeon', password='abc123')
        # user2.save()
        author = Blogger.objects.create(user=user1, bio='my bio')
        blog = Blog.objects.create(title='the origin of life', author=author)
        Comment.objects.create(author=user2, blog=blog,
                               description='make it work, right and fast')

    def test_description_label(self):
        comment = Comment.objects.get(id=1)
        field_label = comment._meta.get_field('description').verbose_name
        self.assertEqual(field_label, 'description')

    def test_description_max_length(self):
        comment = Comment.objects.get(id=1)
        max_length = comment._meta.get_field('description').max_length
        self.assertEqual(max_length, 1000)

    def test_author_label(self):
        comment = Comment.objects.get(id=1)
        field_label = comment._meta.get_field('description').verbose_name
        self.assertEqual(field_label, 'description')

    def test_date_label(self):
        comment = Comment.objects.get(id=1)
        field_label = comment._meta.get_field('post_date').verbose_name
        self.assertEqual(field_label, 'post date')

    def test_blog_label(self):
        comment = Comment.objects.get(id=1)
        field_label = comment._meta.get_field('blog').verbose_name
        self.assertEqual(field_label, 'blog')

    def test_object_name(self):
        comment = Comment.objects.get(id=1)
        expected_object_name = comment.description
        self.assertEqual(expected_object_name, str(comment))
