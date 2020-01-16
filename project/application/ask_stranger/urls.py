from django.urls import path
from . import views

app_name = 'ask_stranger'
urlpatterns = [
        path('index/<int:page>/', views.index, name = 'index'),
        path('',                 views.index, name = 'index'),

        path('hot/',             views.hot,   name = 'hot'),


        path('tag/<str:tag>/<int:page>/', views.tagged, name = 'tagged'),
        path('tag/<str:tag>/', views.tagged, name = 'tagged'),
        path('tag/', views.tagged, name = 'tagged'),

        path('question/<int:question_id>/',    views.question,     name = 'question'),
        path('login/',  views.login,          name = 'login'),
        path('signup/', views.signup,         name = 'signup'),
        path('ask/',    views.ask,            name = 'ask'),
    ]
