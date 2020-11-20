import redis as redis
from django.shortcuts import get_object_or_404
from django.views.generic import DetailView, ListView

from core.models import Image
from counter import settings

redis_connect = redis.StrictRedis(host=settings.REDIS_HOST,
                                  port=settings.REDIS_PORT,
                                  db=settings.REDIS_DB)


class ImagesListView(ListView):
    template_name = 'base.html'
    context_object_name = 'images'

    def get_queryset(self):
        return Image.objects.all()

    def get_context_data(self, *, object_list=None, **kwargs):
        """With pagination for posts list view"""
        context = super(ImagesListView, self).get_context_data(**kwargs)
        images = self.get_queryset()
        context['images'] = images
        return context


class ImageDetailView(DetailView):
    template_name = 'image.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        image = get_object_or_404(self.model, slug=self.kwargs.get('slug'))
        total_views = redis_connect.incr('image:{}:views'.format(image.id))
        redis_connect.zincrby('img_ranking', image.id, 1)
        context['image'] = image
        context['total_views'] = total_views
        return context
