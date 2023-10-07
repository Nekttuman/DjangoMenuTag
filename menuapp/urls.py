from django.urls import path
from . import views

urlpatterns = [
    # main menu
    path('', views.index, name='home'),
    path('home/', views.index, name='home'),
    path('about/', views.index, name='about'),
    path('about/history/', views.index, name='history'),
    path('about/team/', views.index, name='team'),
    path('services/', views.index, name='services'),
    path('services/web/', views.index, name='web_development'),
    path('services/web/websites/', views.index, name='web_websites'),
    path('services/web/websites/technology/', views.index, name='web_websites_technologies'),
    path('services/web/web-apps/', views.index, name='web_apps'),
    path('services/web/online-stores/', views.index, name='online_stores'),
    path('services/mobile/', views.index, name='mobile_services'),
    path('products/', views.index, name='products'),
    path('contacts/', views.index, name='contacts'),

    # tableOfContents menu
    path('intro/', views.index, name='intro'),
    path('chapter1/', views.index, name='chapter1'),
    path('chapter1/p1/', views.index, name='chapter1_p1'),
    path('chapter1/p1/basics/', views.index, name='chapter1_p1_basics'),
]
