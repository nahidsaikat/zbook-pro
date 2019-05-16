from django.contrib import admin
from .forms import CustomerForm, VendorForm
from .models import Customer, Vendor


class CustomerAdmin(admin.ModelAdmin):
    form = CustomerForm
    list_display = ('name', 'phone', 'email', 'company_name', 'type')
    list_filter = ('name', 'type')
    search_fields = ('name', 'type')
    ordering = ('id', )


class VendorAdmin(admin.ModelAdmin):
    form = VendorForm
    list_display = ('name', 'phone', 'email', 'company_name', 'type')
    list_filter = ('name', 'type')
    search_fields = ('name', 'type')
    ordering = ('id', )


admin.site.register(Customer, CustomerAdmin)
admin.site.register(Vendor, VendorAdmin)
