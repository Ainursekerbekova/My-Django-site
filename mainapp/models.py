from django.db import models
from django.urls import reverse
from django.conf import settings


# Create your models here.
class post(models.Model):
    title=models.CharField(max_length=50)
    body=models.TextField(max_length=1000)
    img=models.FileField( blank=True)
    is_saved=models.BooleanField(default=False)
    likes=models.IntegerField(default=0)
    user=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    def get_absolute_url(self):
        return reverse('details', kwargs={'pk' : self.pk})






