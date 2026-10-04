from django.urls import path
from news_portal_app.views import *

urlpatterns = [
    path('', Registration_page, name='Registration_page'),
    path('Login_page/', Login_page, name='Login_page'),
    path('logout_page/', logout_page, name='logout_page'),
    
    path('addNews/', addNews, name='addNews'),
    path('newsList/', newsList, name='newsList'),
    path('editNews/<str:id>', editNews, name='editNews'),
    path('deletenews/<str:id>', deletenews, name='deletenews'),

    path('home/', home, name='home'),
]