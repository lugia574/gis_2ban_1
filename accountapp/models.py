from django.db import models

# Create your models here.
class HelloWorld(models.Model):
    text = models.CharField(max_length=255, null= False) # 문자열 데이터를 여기다가 박을꺼야
