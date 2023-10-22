
from django.urls import path
from . import views
urlpatterns = [
    path('cr/', views.customer, name= 'review'),
    path('build/', views.building_form, name='registration'),
    path('adminsuccess/', views.admin_success),
    path('login/', views.login_form, name='login'),
    path('success/', views.login_success, name='success'),
    path('logout/', views.logout_form, name='logout'),
    path('cpass/', views.password_change, name='passwordchange'),
    path('withoutpass/', views.change_pass_without_oldpass, name='withoutold'),


]
