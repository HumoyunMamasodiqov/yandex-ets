from django.contrib import admin
from .models import Mahsulotlar
# Register your models here.


@admin.register(Mahsulotlar)
class MahsulotlarAdmin(admin.ModelAdmin):
    list_display = ['brenname', 'yetkazishvaqti', 'bepulyetkazish', 'chegirmabilan']
    search_fields = ['brenname', 'yetkazishvaqti', 'bepulyetkazish', 'chegirmabilan']
python manage.py migrate
python manage.py makemigrations 