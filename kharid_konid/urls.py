from django.urls import path

from . import views

urlpatterns = [
    path('', views.kharid, name="kharid"),
    path('<kharid_id>/', views.show , name = "kharids")
]