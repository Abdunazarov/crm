from django.contrib import admin
from .models import RequestBuy


class RequestBuyAdmin(admin.ModelAdmin):
    list_display = ("id", "buyer_full_name", "status", "get_rieltor_name", "get_date")
    # exclude = ('no_attention',)


    def get_date(self, obj):
        return obj.date.strftime("%y-%m-%d  (%H:%M)")
    get_date.admin_order_field = 'Date'
    get_date.short_description = 'Date'

    def get_rieltor_name(self, obj):
        return f"{obj.rieltor.first_name} {obj.rieltor.second_name}"
    
    get_rieltor_name.admin_order_field = 'Rieltor'
    get_rieltor_name.short_description = "Rieltor's name"


admin.site.register(RequestBuy, RequestBuyAdmin)