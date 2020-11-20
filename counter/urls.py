from django.contrib import admin
from django.urls import path

from core.views import BasicView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', BasicView.as_view(), name='home_page'),

]
