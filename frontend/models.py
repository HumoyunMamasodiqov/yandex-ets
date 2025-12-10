from django.db import models

class Mahsulotlar(models.Model):
    asosiyimg = models.ImageField(upload_to='asosiyimg/', blank=True, null=True)
    brenname = models.CharField(max_length=20)
    yetkazishvaqti = models.CharField(max_length=20)
    bepulyetkazish = models.BooleanField(default=False)
    chegirmabilan = models.CharField(max_length=20 , )

    def __str__(self):
        return self.brenname