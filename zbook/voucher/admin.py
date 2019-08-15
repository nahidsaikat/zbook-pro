from django.contrib import admin
from .models import VoucherSubType, Voucher, Ledger
from .forms import VoucherSubTypeForm, VoucherForm, LedgerForm


class VoucherSubTypeAdmin(admin.ModelAdmin):
    form = VoucherSubTypeForm
    list_display = ('name', 'type', 'prefix', 'debit_account', 'credit_account')
    list_filter = ('name', 'type', 'debit_account', 'credit_account')
    search_fields = ('name', 'type', 'debit_account', 'credit_account')
    ordering = ('type', 'name')


class VoucherAdmin(admin.ModelAdmin):
    form = VoucherForm
    list_display = ('voucher_date', 'voucher_number', 'type', 'sub_type', 'amount')
    list_filter = ('type', 'sub_type', 'voucher_date')
    search_fields = ('voucher_number', 'type', 'sub_type', 'voucher_date')
    ordering = ('voucher_date', 'type', 'sub_type')


class LedgerAdmin(admin.ModelAdmin):
    form = LedgerForm
    list_display = ('voucher', 'account', 'amount', 'entry_date')
    list_filter = ('voucher', 'account')
    search_fields = ('voucher', 'account', 'entry_date')
    ordering = ('entry_date', 'voucher')


admin.site.register(VoucherSubType, VoucherSubTypeAdmin)
admin.site.register(Voucher, VoucherAdmin)
admin.site.register(Ledger, LedgerAdmin)
