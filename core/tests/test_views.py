from django.test import TestCase
from django.urls import reverse

from core.models import Image


class ImageViewTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.image = Image.objects.create(title='Test Image',
                                         url='https://cf.ltkcdn.net/cats/images/std/264838-699x450-funny-cat-quotes.jpg')
        cls.image.slug = '/image/test-image-title-3009856/'

    def test_view_url_exists_at_desired_location(self):
        resp = self.client.get('/')
        self.assertEqual(resp.status_code, 200)

    def test_view_uses_correct_url(self):
        resp = self.client.get(reverse('core:images'))
        self.assertEqual(resp.status_code, 200)

    def test_view_url_accessible_by_name(self):
        resp = self.client.get('/image/test-image-title-3009856/')
        self.assertEqual(resp.status_code, 301)
