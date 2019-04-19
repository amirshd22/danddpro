from django.urls import path

from . import views

urlpatterns = [
    path('', views.akhbar, name="akhbar"),
    path('<akhbar_id>/', views.show , name = "details")
]