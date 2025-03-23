from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('digital-distribution.html/', views.digital_distribution, name='digital_distribution'),
    path('login.html/', views.login, name='login'),
    path('music-distribute.html/', views.music_distribute, name='music_distribute'),
    path('music-publishing.html/', views.music_publishing, name='music_publishing'),
    path('rights-management.html/', views.rights_management, name='rights_management'),
    path('sell.html/', views.sell, name='sell'),
    path('service.html/', views.service, name='service'),
    path('sign-up.htm/l', views.sign_up, name='sign_up'),
    path('logout/', views.logout, name='logout'),
    path('stores.html/', views.stores, name='stores'),
    path('support.html/', views.support, name='support'),
    path('youtube-monetization.htm/l', views.youtube_monetization, name='youtube_monetization'),
    path('admin/user-list/', views.user_list, name='user_list'),
    
]