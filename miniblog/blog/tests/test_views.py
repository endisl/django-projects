from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse
from blog.models import Blog, Blogger


class BlogListViewTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        pass

    def test_view_url_exists_at_desired_location(self):
        pass

    def test_view_url_accessible_by_name(self):
        pass

    def test_view_uses_correct_template(self):
        pass

    def test_pagination_is_five(self):
        pass
