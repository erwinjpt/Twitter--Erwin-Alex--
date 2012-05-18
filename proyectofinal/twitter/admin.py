from django.contrib import admin
from twitter.models import Tweet, Profile, Follow


class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'frase',)
    search_fields = ('user',)
    
class TweetAdmin(admin.ModelAdmin):
    list_display = ('user', 'contenido','activo',)
    search_fields = ('user',)
   
    
class FollowAdmin(admin.ModelAdmin):
    list_display = ('fecha', 'activo',)
    search_fields = ('activo',)


admin.site.register(Profile, ProfileAdmin)
admin.site.register(Tweet, TweetAdmin)
admin.site.register(Follow, FollowAdmin) 