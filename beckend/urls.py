
from django.contrib import admin
from django.urls import path , include
urlpatterns = [
    path('salom/', admin.site.urls),
    path('', include('frontend.urls') )
]
