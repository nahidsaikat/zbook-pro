from djchoices import DjangoChoices, ChoiceItem


class PartyType(DjangoChoices):
    Customer = ChoiceItem(1, 'Customer')
    Vendor = ChoiceItem(2, 'Vendor')


class PartyGender(DjangoChoices):
    Male = ChoiceItem(1, 'Male')
    Female = ChoiceItem(2, 'Female')
