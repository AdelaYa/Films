from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth import get_user_model

from .models import Post


class BlogTests(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='testuser',
            email='test@email.com',
            password='secret'
        )
        self.post = Post.objects.create(
            title='Python prog',
            post_text='Text example',
            author=self.user
        )

    def test_string(self):
        post = Post(title='Post Python')
        self.assertEqual(str(post), post.title)

    def test_post_content(self):
        self.assertEqual(f'{self.post.title}', 'Python prog')
        self.assertEqual(f'{self.post.author}', 'testuser')
        self.assertEqual(f'{self.post.post_text}', 'Text example')

    def test_post_list_view(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Text example')
        self.assertTemplateUsed(response, 'index.html')

    def test_post_detail_view(self):
        response = self.client.get('/post/1/')
        no_response = self.client.get('/post/100/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertContains(response, 'Python prog')
        self.assertTemplateUsed(response, 'post_detail.html')

    def test_get_absolute_url(self):
        self.assertEqual(self.post.get_absolute_url(), '/post/1/')

    def test_post_create_view(self):
        response = self.client.post(reverse('post_new'),
                                    {
                                        'title': 'New Title',
                                        'post_text': 'New Text',
                                        'author': self.user,
                                    })
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'New Title')
        self.assertContains(response, 'New Text')

    def test_post_update_view(self):
        response = self.client.post(reverse('post_edit', args='1'),
                                    {
                                        'title': 'Update title',
                                        'post_text': 'Update text',
                                    })
        self.assertEqual(response.status_code, 302)

    def test_post_delete_view(self):
        response = self.client.get(reverse('post_delete', args='1'))
        self.assertEqual(response.status_code, 200)
