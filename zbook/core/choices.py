from djchoices import DjangoChoices, ChoiceItem


class LocationType(DjangoChoices):
    Country = ChoiceItem(1, 'Country')
    State = ChoiceItem(2, 'State')
    Division = ChoiceItem(3, 'Division')
    District = ChoiceItem(4, 'District')
    SubDistrict = ChoiceItem(5, 'SubDistrict')
