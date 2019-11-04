from django.urls import path
from . import views

urlpatterns = [
        path('',       views.index,            name = 'index'),
        path('hot/',    views.hot,              name = 'hot'),
        path('tag/',    views.tagged,           name = 'tagged'),
        path('question/',   views.question,     name = 'question'),
        path('login/',  views.login,            name = 'login'),
        path('signup/', views.signup,           name = 'signup'),
        path('ask/',    views.ask,              name = 'ask'),
    ]