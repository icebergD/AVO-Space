from django.contrib import admin

from .models import Account, Merch, Donate

admin.site.register(Account)
admin.site.register(Merch)
admin.site.register(Donate)
