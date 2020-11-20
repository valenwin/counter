import logging
from datetime import datetime

import redis as redis
from django.shortcuts import get_object_or_404
from django.views.generic import DetailView, ListView

from core.models import Image
from counter import settings

redis_connect = redis.StrictRedis(host=settings.REDIS_HOST,
                                  port=settings.REDIS_PORT,
                                  db=settings.REDIS_DB)

logger = logging.getLogger(__name__)


class ImagesListView(ListView):
    template_name = 'base.html'
    context_object_name = 'images'

    def get_queryset(self):
        return Image.objects.all()

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ImagesListView, self).get_context_data(**kwargs)
        images = self.get_queryset()
        try:
            context['images'] = images
        except KeyError:
            logger.error('There no any image in db.')
        return context


class ImageDetailView(DetailView):
    model = Image
    context_object_name = 'images'
    template_name = 'image.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        image = get_object_or_404(self.model, slug=self.kwargs.get('slug'))
        total_views = redis_connect.incr('image:{}:views'.format(image.id))
        redis_connect.zincrby('img_ranking', image.id, 1)
        try:
            context['image'] = image
        except KeyError:
            logger.error('There no such image in db.')
        context['total_views'] = total_views
        logger.info(f'There are {total_views} on image {image}. '
                    f'Datetime: {datetime.now()}')
        return context
