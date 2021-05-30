from django.contrib import admin
from .models import Payment, Transaction
admin.site.register([Payment, Transaction])
# Register your models here.
