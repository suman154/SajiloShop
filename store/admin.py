from django.contrib import admin
from .models import *
from django.contrib.auth.models import User



# Register your models here.
admin.site.register(Category)
admin.site.register(Customer)
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(Profile)


# Mix profile info and user info in the admin panel
class ProfileInline(admin.StackedInline):
    model = Profile
    

# Extebd user model in the admin panel
class UserAdmin(admin.ModelAdmin):
    model = User
    fields = ['username', 'email', 'first_name', 'last_name']
    inlines = [ProfileInline]

# Unregister the default user model
admin.site.unregister(User)


# Register the extended user model
admin.site.register(User, UserAdmin)



