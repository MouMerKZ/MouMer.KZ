from django.urls import path, re_path

from lol.views import *

urlpatterns = [
    path('', index, name='home'),
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),
    path('post/<int:post_id>/', show_post, name='post')
]

