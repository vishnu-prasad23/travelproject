from .import views
from django.urls import path,include

urlpatterns = [
        path('', views.demo, name='demo')
        #path('add/', views.operation, name='operation')
        # path('sub/', views.substration, name='substration'),
        # path('mul/', views.multiplication, name='multiplication'),
        # path('div/', views.division, name='division'),

]
