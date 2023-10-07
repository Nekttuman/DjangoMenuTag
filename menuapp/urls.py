from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='home'),  # Главная страница
    path('home/', views.index, name='home'),  # Главная страница
    path('about/', views.index, name='about'),  # Страница "О нас"
    path('about/history/', views.index, name='history'),  # Страница "О нас"
    path('about/team/', views.index, name='history'),  # Страница "О нас"
    path('services/', views.index, name='services'),  # Страница "Услуги"
    path('services/web/', views.index, name='web_development'),  # Страница "Веб-разработка"
    path('services/web/websites/', views.index, name='web_websites'),  # Страница "Веб-сайты"
    path('services/web/websites/technology/', views.index, name='web_websites_technologies'),  # Страница "Веб-сайты"
    path('services/web/web-apps/', views.index, name='web_apps'),  # Страница "Веб-приложения"
    path('services/web/online-stores/', views.index, name='online_stores'),  # Страница "Интернет-магазины"
    path('services/mobile/', views.index, name='mobile_services'),  # Страница "Мобильные приложения"
    path('products/', views.index, name='products'),  # Страница "Продукты"
    path('contacts/', views.index, name='contacts'),  # Страница "Контакты"
    # Другие URL-шаблоны вашего приложения, если есть

    path('intro/', views.index, name='intro'),  # Страница "Продукты"
    path('chapter1/', views.index, name='chapter1'),  # Страница "Контакты"
    path('chapter1/p1/', views.index, name='chapter1_p1'),  # Страница "Контакты"
    path('chapter1/p1/basics/', views.index, name='chapter1_p1_basics'),  # Страница "Контакты"
]