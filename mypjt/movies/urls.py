from django.urls import path
from . import views

app_name = 'movies'
urlpatterns = [
    path('', views.index, name='index'),
    path('movie/create/', views.create, name='create'),
    path('movie/<int:pk>/', views.detail, name='detail'),
    path('movie/<int:pk>/update/', views.update, name='update'),
    path('movie/<int:pk>/delete/', views.delete, name='delete'),
    path('movie/<int:pk>/comment/<int:comment_pk>/delete/', views.comments_delete, name='comments_delete'),
]
