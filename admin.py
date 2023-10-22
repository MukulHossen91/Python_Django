from django.contrib import admin
from .models import laptop

# Register your models here.
class laptopAdmin(admin.ModelAdmin):
    list_display =('mobile', 're_mobile', 'laptop', 'email', 'password', 'about', 'textarea', 'checkbox', 'ram', 'ssd', 'youtube_chanel' )

admin.site.register(laptop, laptopAdmin)




