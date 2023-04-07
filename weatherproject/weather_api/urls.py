from django.urls import path
from . import views

urlpatterns = [
    path('', views.indexx, name="homepage"),
    path('login_index', views.login_index),
    path('reg', views.reg),
    path('index', views.index, name="home"),
    path("result", views.result, name="result"),
    # path('social_links', views.social_links),
]
