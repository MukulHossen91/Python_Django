from django.urls import path
from . import views
urlpatterns = [
    path('pd/', views.cake, name='product'),
    path('successfully/', views.send),
    path('recent/', views.details),
    path('middleware/', views.midd),
    


]