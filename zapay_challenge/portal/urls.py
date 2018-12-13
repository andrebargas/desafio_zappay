from django.urls import include, path

from portal import views


urlpatterns = [
    path('', views.index, name='home'),

]
