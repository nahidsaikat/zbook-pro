from django.forms import ModelForm
from .models import Customer, Vendor


class CustomerForm(ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'


class VendorForm(ModelForm):
    class Meta:
        model = Vendor
        fields = '__all__'
