from django.urls import path
from . import views
from .views import Addsub, Addstudent


urlpatterns = [
    path('', views.index, name='index'),
    path('app/', views.app, name='app'),
    path('addsub/', Addsub.as_view(), name='addsub'),
    path('sub/<int:pk>/', views.SubDetail.as_view(), name='subject'),
    path('subupdate/<int:pk>/', views.SubUpdate.as_view(), name='updatesub'),
    path('subdelete/<int:pk>/', views.SubDelete.as_view(), name='deletesub'),
    path('addstudent/', Addstudent.as_view(), name='addstudent'),
]
