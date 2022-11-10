from django.contrib import admin
from .models import RequestSell


class RequestSellAdmin(admin.ModelAdmin):
    list_display = ("id", "seller_full_name", "apartment", "get_apartment_rieltor", "get_date")
    # exclude = ('no_attention',)


    def get_date(self, obj):
        return obj.date.strftime("%y-%m-%d  (%H:%M)")
    get_date.admin_order_field = 'Date'
    get_date.short_description = 'Date'


    def get_apartment_rieltor(self, obj):
        return f"{obj.rieltor.first_name} {obj.rieltor.second_name}"

    get_apartment_rieltor.admin_order_field = 'Rieltor'
    get_apartment_rieltor.short_description = "Rieltor's name"


admin.site.register(RequestSell, RequestSellAdmin)


