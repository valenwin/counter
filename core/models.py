from django.db import models
from django.urls import reverse

from core.utils import custom_slugify


class Image(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200,
                            blank=True,
                            null=True)
    url = models.URLField()
    created = models.DateField(auto_now_add=True,
                               db_index=True)

    class Meta:
        ordering = ('-created',)

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = custom_slugify(self.title)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('core:image_details', kwargs={'slug': self.slug})

    def __str__(self):
        return self.title
