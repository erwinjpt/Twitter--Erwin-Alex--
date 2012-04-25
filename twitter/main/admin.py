from django.contrib import admin
from main.models import Customer, Tweet, Bio

class CustomerAdmin(admin.ModelAdmin):
    list_display = ('name_customer', 'last_name_customer',)
    
class TweetAdmin(admin.ModelAdmin):
    list_display = ('created', 'Que_esta_pasando',)
    search_fields = ('name_customer',)
   
    
class BioAdmin(admin.ModelAdmin):
    list_display = ('name_customer', 'hobbie','music',)
    search_fields = ('name_customer',)
    
admin.site.register(Customer, CustomerAdmin)
admin.site.register(Tweet, TweetAdmin)
admin.site.register(Bio, BioAdmin) 