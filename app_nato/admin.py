from django.contrib import admin

# Register your models here.
from .models import NatoMember

class NatoMemberAdmin(admin.ModelAdmin):
    list_display = ('id','name')
    search_fields = ('name','capital_city')
    list_filter = ('continent','joined_year')

admin.site.register(NatoMember, NatoMemberAdmin)