from django.contrib import admin
from main.models import Tweet, UserProfile

    
class TweetAdmin(admin.ModelAdmin):
    list_display = ('name_customer', 'Que_esta_pasando','created',)
    search_fields = ('name_customer',)
   
    
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'last_name','birthday','location',)
    search_fields = ('user',)


admin.site.register(Tweet, TweetAdmin)
admin.site.register(UserProfile, UserProfileAdmin) 