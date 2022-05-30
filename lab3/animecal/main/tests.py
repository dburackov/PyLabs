from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
from .models import Anime, Comment, Genre

class BlogTests(TestCase):

    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='testuser',
            password='secret'
        )

        self.anime = Anime.objects.create(
            title='A sample title',
            description='adf',
            poster='static/main/img/vk.jpg',
            year=2022,
            episodes=12,
            status='Ongoing',
            release_day=0,
        )

        self.genre = Genre.objects.create(
            name='asdf'
        )

        self.comment = Anime.objects.create(
            author='asdfadsfasdf',
            text='comment text',
        )

    def test_string_representation(self):
        self.assertEqual(str(self.anime), self.anime.title)
        self.assertEqual(str(self.genre), self.genre.title)

    def test_get_absolute_url(self):
        self.assertEqual(self.anime.get_absolute_url(), reverse('anime', kwargs={'anime_id': self.anime.pk}))

    def test_anime_content(self):
        self.assertEqual(f'{self.anime.title}', 'A sample title')
        self.assertEqual(f'{self.anime.description}', 'adf')
        self.assertEqual(f'{self.anime.year}', 2022)
        self.assertEqual(f'{self.anime.episodes}', 12)
        self.assertEqual(f'{self.anime.release_day}', 0)

    def test_main_list_view(self):
        response = self.client.get(reverse('anime_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'main/anime_list.html')

    def test_anime_detail_view(self):
        response = self.client.get(reverse('anime', kwargs={'anime_id': self.anime.pk}) )
        self.assertEqual(response.status_code, 200)
        no_response = self.client.get('/anime/100000/')
        self.assertEqual(no_response.status_code, 404)
        self.assertTemplateUsed(response, 'main/anime.html')

    """
    def test_comment_create_view(self):
        response = self.client.comment(reverse('post_new'), {
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