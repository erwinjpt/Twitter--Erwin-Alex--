from django.contrib import admin
from main.models import Customer, Twitt, Bio

class CustomerAdmin(admin.ModelAdmin):
    list_display = ('name_customer', 'last_name_customer',)
    
class TwittAdmin(admin.ModelAdmin):
    list_display = ('created', 'status',)
    search_fields = ('tweet_customer',)
    
class BioAdmin(admin.ModelAdmin):
    list_display = ('name_customer', 'hobbie','music',)
    search_fields = ('name_customer',)
    
admin.site.register(Customer, CustomerAdmin)
admin.site.register(Twitt, TwittAdmin)
admin.site.register(Bio, BioAdmin) 