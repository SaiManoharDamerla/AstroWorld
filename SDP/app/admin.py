from django.contrib import admin
from .models import Register, Contact, Userdetails, Feedback

# Register your models here.
admin.site.register(Register)
admin.site.register(Contact)
admin.site.register(Userdetails)
admin.site.register(Feedback)
