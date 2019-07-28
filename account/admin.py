from django.contrib import admin
from .models import AccountSubType, Account
from .forms import AccountSubTypeForm, AccountForm


class AccountSubTypeAdmin(admin.ModelAdmin):
    form = AccountSubTypeForm
    list_display = ('name', 'type', 'order')
    list_filter = ('name', 'type')
    search_fields = ('name', 'type')
    ordering = ('type', )


class AccountAdmin(admin.ModelAdmin):
    form = AccountForm
    list_display = ('name', 'code', 'type', 'sub_type', 'depth', 'entry_date')
    list_filter = ('name', 'type', 'sub_type', 'entry_date')
    search_fields = ('name', 'type', 'sub_type', 'entry_date')
    ordering = ('entry_date', 'type', 'sub_type')


admin.site.register(AccountSubType, AccountSubTypeAdmin)
admin.site.register(Account, AccountAdmin)
