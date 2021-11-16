from django.urls import path, include
from . import views





urlpatterns = [
    path('', views.home, name="home"),
    path('about/',views.about,name="about"),
    path('category/<slug:slug>/',views.category_details,name="category"),
    path('service_details/<slug:slug>/',views.service_details,name="service_details"),
    path('blogs/',views.blog_list,name="blog"),
    path("blogs/<slug:slug>/",views.blog_details,name="blog_details"),
    path("portofolio/",views.portofolio,name="portofolio"),
    path("contact",views.contact ,name="contact")


]