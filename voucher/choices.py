from djchoices import DjangoChoices, ChoiceItem


class VoucherType(DjangoChoices):
    Receive = ChoiceItem(1, 'Receive')
    Payment = ChoiceItem(2, 'Payment')
    Expense = ChoiceItem(3, 'Expense')
    Sale = ChoiceItem(4, 'Sale')
    Purchase = ChoiceItem(5, 'Purchase')
    SaleDelivery = ChoiceItem(6, 'SaleDelivery')
    PurchaseDelivery = ChoiceItem(7, 'PurchaseDelivery')
