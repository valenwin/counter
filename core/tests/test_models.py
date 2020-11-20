import datetime

from django.test import TestCase

from core.models import Image


class ImageModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.image = Image.objects.create(title='Test Image',
                                         url='https://cf.ltkcdn.net/cats/images/std/264838-699x450-funny-cat-quotes.jpg')
        cls.image.slug = '/image/test-image-1605908527/'

    def test_get_absolute_url(self):
        self.assertEquals(self.image.get_absolute_url(),
                          '/image/test-image-1605908527/')

    def test_title_label(self):
        field_label = self.image._meta.get_field('title').verbose_name
        self.assertEquals(field_label, 'title')

    def test_title_max_length(self):
        max_length = self.image._meta.get_field('title').max_length
        self.assertEquals(max_length, 200)

    def test_title_data(self):
        self.assertEquals(self.image.title, 'Test Image')

    def test_url_label(self):
        field_label = self.image._meta.get_field('url').verbose_name
        self.assertEquals(field_label, 'url')

    def test_url_max_length(self):
        max_length = self.image._meta.get_field('url').max_length
        self.assertEquals(max_length, 200)

    def test_description_data(self):
        self.assertEquals(self.image.url, 'https://cf.ltkcdn.net/cats/images/std/264838-699x450-funny-cat-quotes.jpg')

    def test_created_label(self):
        field_label = self.image._meta.get_field('created').verbose_name
        self.assertEquals(field_label, 'created')

    def test_created_date(self):
        date = self.image.created.today()
        self.assertEquals(date, datetime.date.today())

    def test_slug_label(self):
        field_label = self.image._meta.get_field('slug').verbose_name
        self.assertEquals(field_label, 'slug')

    def test_slug_max_length(self):
        max_length = self.image._meta.get_field('slug').max_length
        self.assertEquals(max_length, 200)

    def test_object_title(self):
        expected_object_title = self.image.title
        self.assertEquals(expected_object_title, str(self.image))
