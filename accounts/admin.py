from django.contrib import admin
from .models import User , Relation

# Register your models here.


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['id', 'full_name', 'user_name', 'email' , 'bio', 'birth_date', 'join_date']
    search_fields = ['user_name', 'email']
    list_filter = ['user_name', 'email']

#@admin.register(Relation)
#class RelationAdmin(admin.ModelAdmin):
#    list_display = ['id', 'from_user', 'to_user']
#    search_fields = ['from_user', 'to_user']
#    list_filter = ['from_user', 'to_user']