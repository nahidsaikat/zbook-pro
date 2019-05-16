from django.forms import ModelForm
from .models import AccountSubType, Account


class AccountSubTypeForm(ModelForm):
    class Meta:
        model = AccountSubType
        fields = '__all__'


class AccountForm(ModelForm):
    class Meta:
        model = Account
        fields = '__all__'
        exclude = ('depth', )
