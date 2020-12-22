from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home',views.index,name="home"),
    path('',views.index,name="home"),
    path('contact',views.contact,name="Contact us"),
    path('about',views.about,name="About us"),
    path('submitcontact',views.submitcontact,name='submitted'),
    path('disease',views.disease,name="disease"),
    path('search',views.search,name="search")

]
