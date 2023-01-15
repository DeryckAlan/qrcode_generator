from django.urls import path
from . import views

app_name = 'generator'

urlpatterns = [
    path('', views.QrcodeList.as_view(), name='list'),
    path('create/', views.QrcodeCreate.as_view(), name='create'),
    path('update/<int:pk>/', views.QrcodeUpdate.as_view(), name='update'),
]
