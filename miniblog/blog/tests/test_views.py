from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse
from blog.models import Blog, Blogger


class BlogListViewTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        number_of_blogs = 12

        for blog_id in range(number_of_blogs):
            # here str() is used while creating the user object in order
            # to differentiate the users' username otherwise a data integrity error is raised
            # alternatively only one user can be created before the loop
            user = User.objects.create_user(
                username='so-and-so'+str(blog_id), password='12345')
            user.save()
            author = Blogger.objects.create(user=user, bio='my bio')
            Blog.objects.create(title='the origin of life'+str(blog_id),
                                author=author, description="c'est la vie"+str(blog_id))

    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/blog/blogs/')
        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('blogs'))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('blogs'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/blog_list.html')

    def test_pagination_is_five(self):
        response = self.client.get(reverse('blogs'))
        self.assertEqual(response.status_code, 200)
        self.assertTrue('is_paginated' in response.context)
        self.assertTrue(response.context['is_paginated'] == True)
        self.assertEqual(len(response.context['blog_list']), 5)
