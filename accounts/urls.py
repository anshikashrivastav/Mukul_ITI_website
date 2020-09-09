from django.conf.urls import url
from django.urls import path

from . import views

urlpatterns=[
#juststart and stop
url(r'^$',views.home),
#url(r'^signup/$',views.signup),
path('register/',views.RegisterPage,name="register"),
path('login/',views.LogPage,name="login"),
path('staff/',views.staffPage,name="staff"),
path('about/',views.AboutPage,name="about"),
]