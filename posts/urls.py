from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='main'),
    path('thread/<slug:post_slug>', views.post_thread, name='post-thread'),
    path('thread/<slug:post_slug>/<slug:comment_slug>', views.post_thread, name='post-comment')
]
