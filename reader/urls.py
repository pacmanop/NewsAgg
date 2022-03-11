from django.urls import path
from reader import views


urlpatterns = [
    path('', views.home, name="Home"),
    path('next', views.loadcontent, name="Loadcontent"),
path('1', views.cat, name="cat"),
path('2', views.con, name="con"),
    path('3', views.so, name="so"),
    path('sub',views.sub,name='sub')
]
