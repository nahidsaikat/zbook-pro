from django.views.generic.edit import CreateView
from .forms import AccountForm


class AccountCreateView(CreateView):
    form_class = AccountForm
    template_name = 'account/add.html'
