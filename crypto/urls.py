from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('prices/', views.prices, name='prices'),
    path('list/', views.news_list, name='list_news'),
    path('detail/<source_id>', views.news_detail, name='news_detail'),
]