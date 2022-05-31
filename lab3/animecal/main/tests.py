from django.contrib.auth import get_user_model
from django.db.models.fields import json
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
            description='some description',
            poster='static/main/img/vk.jpg',
            year=2022,
            episodes=12,
            status='Ongoing',
            release_day=0,
        )

        self.genre = Genre.objects.create(
            name='genre'
        )

        self.comment = Comment.objects.create(
            anime_id=self.anime,
            author='author',
            text='comment text',
        )

    def test_string_representation(self):
        self.assertEqual(str(self.anime), self.anime.title)
        self.assertEqual(str(self.genre), self.genre.name)

    def test_get_absolute_url(self):
        self.assertEqual(self.anime.get_absolute_url(), reverse('anime', kwargs={'pk': self.anime.pk}))

    def test_anime_content(self):
        self.assertEqual(f'{self.anime.title}', 'A sample title')
        self.assertEqual(f'{self.anime.description}', 'some description')
        self.assertEqual(f'{self.anime.year}', '2022')
        self.assertEqual(f'{self.anime.episodes}', '12')
        self.assertEqual(f'{self.anime.release_day}', '0')

    def test_main_list_view(self):
        response = self.client.get(reverse('anime_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'main/anime_list.html')

    def test_anons_list_view(self):
        response = self.client.get(reverse('anons'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'main/anons.html')

    def test_ongoing_list_view(self):
        response = self.client.get(reverse('ongoing'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'main/ongoing.html')

    def test_anime_detail_view(self):
        response = self.client.get(reverse('anime', kwargs={'pk': self.anime.pk}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'main/anime.html')

    def test_anime_create_view(self):
        response = self.client.post(reverse('create'), {
            'title': 'New title',
            'description': 'New description',
            'poster': 'static/main/img/vk.jpg',
            'year': 2022,
            'episodes': 12,
            'status': 'Ongoing',
            'release_day': 0,
        })
        self.assertEqual(response.status_code, 302)

    def test_anime_edit_view(self):
        response = self.client.post(reverse('edit', args=f'{self.anime.id}'), {
            'title': 'Updated title',
        })
        self.assertEqual(response.status_code, 302)
        
    def test_anime_delete_view(self):
        response = self.client.post(reverse('delete', args=f'{self.anime.id}'))
        self.assertEqual(response.status_code, 302)