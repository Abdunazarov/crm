from django.db import models
from user.models import User

ACTIVE, HOT, WARM = 'Активная', 'Горячая', 'Теплая'
req_status = [(ACTIVE, 'Активная'), (HOT, 'Горячая'), (WARM, 'Теплая')]

NO, OK, EURO = 'Без ремонта', 'Средний ремонт', 'Евро ремонт'
req_condition = [(NO, 'Без ремонта'), (OK, 'Средний ремонт'), (EURO, 'Евро ремонт')]


class Apartment(models.Model):

    name = models.CharField(max_length=255, blank=True)
    location = models.CharField(max_length=255, blank=True)
    price = models.IntegerField(blank=True, null=True)
    rooms = models.IntegerField(blank=True, null=True)
    levels = models.IntegerField(blank=True, null=True)
    condition = models.CharField(max_length=20, choices=req_condition, default=OK)
    comments = models.TextField(blank=True, null=True)

    rieltor = models.ForeignKey(User, on_delete=models.CASCADE)

    image1 = models.ImageField(blank=True, null=True)
    image2 = models.ImageField(blank=True, null=True)
    image3 = models.ImageField(blank=True, null=True)
    image4 = models.ImageField(blank=True, null=True)
    image5 = models.ImageField(blank=True, null=True)
    image6 = models.ImageField(blank=True, null=True)
    image7 = models.ImageField(blank=True, null=True)
    image8 = models.ImageField(blank=True, null=True)
    image9 = models.ImageField(blank=True, null=True)
    image10 = models.ImageField(blank=True, null=True)
    image11 = models.ImageField(blank=True, null=True)
    image12 = models.ImageField(blank=True, null=True)
    image13 = models.ImageField(blank=True, null=True)
    image14 = models.ImageField(blank=True, null=True)


    class Meta:
        verbose_name = 'Объект'
        verbose_name_plural = 'Объекты'

    def __str__(self):
        return self.name 



    