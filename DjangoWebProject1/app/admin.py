from django.contrib import admin
from app.models import User_Details,Leave_Status

@admin.register(User_Details)
class User_Detais_Admin(admin.ModelAdmin):
    empty_value_display = '--empty--'
    list_display = ['user','department','faculty','hod','registrar','director']
    list_filter = ('user','department','faculty','hod','registrar','director')

class Leave_Status_Admin(admin.ModelAdmin):
    list_display = ['user','type','start_date','end_date','status']
    date_hierarchy = 'start_date'
    empty_value_display = '--empty--'

#admin.site.register(User_Details,User_Detais_Admin)
admin.site.register(Leave_Status,Leave_Status_Admin)