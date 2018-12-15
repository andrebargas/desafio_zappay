from django.urls import include, path

from portal import views


urlpatterns = [
    path('', views.index, name='home'),
    path('past/', views.past_launches, name='home'),
    path('last/', views.last_launch, name='home'),
    path('next/', views.next_launch, name='home'),
    path('upcoming/', views.next_launches, name='home'),

]
