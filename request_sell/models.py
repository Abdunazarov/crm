from django.db import models
from apartment.models import Apartment
from user.models import User

from datetime import timedelta
from datetime import datetime
from django.utils import timezone

ACTIVE, HOT, WARM = 'Теплый', 'Горящий', 'Завершенный'
req_status = [(ACTIVE, 'Теплый'), (HOT, 'Горящий'), (WARM, 'Завершенный')]

NO, OK, EURO = 'Без ремонта', 'Средний ремонт', 'Евро ремонт'
req_condition = [(NO, 'Без ремонта'), (OK, 'Средний ремонт'), (EURO, 'Евро ремонт')]



class RequestSell(models.Model):

    rieltor = models.ForeignKey(User, on_delete=models.CASCADE)

    apartment = models.OneToOneField(Apartment, on_delete=models.CASCADE)

    seller_full_name = models.CharField(max_length=255, blank=True, null=True)
    seller_phone_number = models.CharField(max_length=50, blank=True, null=True) 

    status = models.CharField(max_length=30, choices=req_status, default=ACTIVE)
    rooms = models.IntegerField(blank=True, null=True)
    rooms_area = models.IntegerField(blank=True, null=True)
    area = models.IntegerField(blank=True, null=True)
    levels = models.IntegerField(blank=True, null=True)
    condition = models.CharField(max_length=20, choices=req_condition, default=OK)
    location = models.CharField(max_length=150, blank=True, null=True)
    start_price = models.IntegerField(blank=True, null=True)
    end_price = models.IntegerField(blank=True, null=True)
    comments = models.TextField(blank=True, null=True)
    finished = models.BooleanField(default=False)

    no_attention = models.BooleanField(default=False)
    date = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    last_time_edited = models.DateTimeField(auto_now=True, blank=True, null=True)


    def passed_deadline(self):
        plus_seven_days_to_last_time_edited = self.last_time_edited + timedelta(minutes=1) # days=7
        self.last_time_edited = datetime.now()

        if datetime.now().date() >= plus_seven_days_to_last_time_edited.date():
            self.no_attention = True
        
        else:
            self.no_attention = False

        self.save()


    class Meta:
        verbose_name = 'Заявка на продажу'
        verbose_name_plural = 'Заявки на продажу'

    def __str__(self):
        return '#' + str(self.id) + ' - ' + self.seller_full_name 





