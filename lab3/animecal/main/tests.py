from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse


class BlogTests(TestCase):

    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='testuser',
            email='test@email.com',
            password='secret'
        )
        """
        self.post = Blog.objects.create(
            title='A good title',
            content='Nice body content',
            author=self.user,
        )
        """
    """
    def test_string_representation(self):
        post = Blog(title='A sample title')
        self.assertEqual(str(post), post.title)
    """
    def test_get_absolute_url(self):
        self.assertEqual(self.post.get_absolute_url(), '/post/1/')

    def test_post_content(self):
        self.assertEqual(f'{self.post.title}', 'A good title')
        self.assertEqual(f'{self.post.author}', 'testuser')
        self.assertEqual(f'{self.post.content}', 'Nice body content')

    def test_post_list_view(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Nice body content')
        self.assertTemplateUsed(response, 'home.html')
def test_post_detail_view(self):
        response = self.client.get('/post/5/')
        self.assertEqual(response.status_code, 200)
        no_response = self.client.get('/post/100000/')
        # print(no_response.status_code)
        self.assertEqual(no_response.status_code, 404)
        self.assertContains(response, 'A good title')
        self.assertTemplateUsed(response, 'blog/post_detail.html')

"""
def test_post_create_view(self):
        response = self.client.post('/account/login/', {'username': 'testuser', 'password': 'secret'})

        response = self.client.post(reverse('post_new'), {
            'title': 'New title',
            'content': 'New text',
            'categories': 'Spam',
        })
        self.assertEqual(response.status_code, 200)
    
    def test_post_update_view(self):
        response = self.client.post('/account/login/', {'username': 'testuser', 'password': 'secret'})
        # print(response)
        for post in Blog.objects.all():
            p = post
        response = self.client.post(reverse('post_edit', args='7'), json.dumps({
            'title': 'Updated title',
            'content': 'Updated text',
        }), content_type='application/json')
        self.assertEqual(response.status_code, 200)
        
    def test_post_delete_view(self):
        response = self.client.post('/account/login/', {'username': 'testuser', 'password': 'secret'})
        self.assertEqual(response.status_code, 302)
        response = self.client.post(reverse('post_delete', args='4'))
        self.assertEqual(response.status_code, 302)
        
        """