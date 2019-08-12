from djchoices import DjangoChoices, ChoiceItem


class AccountType(DjangoChoices):
    Asset = ChoiceItem(1, 'Asset')
    Liability = ChoiceItem(2, 'Liability')
    Income = ChoiceItem(3, 'Income')
    Expense = ChoiceItem(4, 'Expense')
    Equity = ChoiceItem(5, 'Equity')
