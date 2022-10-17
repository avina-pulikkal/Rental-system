from django.urls import path
from .import views


urlpatterns=[
    path('',views.index,name="index"),
    path('index/',views.index,name="index"),
    path('Register/',views.Register,name="Register"),
    path('about/',views.about,name="about"),
    path('login/',views.login,name="login"),   
    path('log/',views.log,name="log"),       
    path('home/',views.home,name="home"),
    path('portfolio/',views.portfolio,name="portfolio"),
    # path('plant/',views.plant,name="plant"),
    # path('weedviews/',views.weedviews,name="weedviews"),
]