from django.contrib import admin
from .models import departments,Doce,Booking


# Register your models here.
admin.site.register(departments)
admin.site.register(Doce)

class BookigAdmin(admin.ModelAdmin):
    list_display = ('id', 'p_name', 'p_phone','p_email','docs_name','booking_date', 'booked_on')
admin.site.register(Booking, BookigAdmin)








