"""
class ImageFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Image

    image = factory.LazyAttribute(
            lambda _: ContentFile(
                factory.django.ImageField()._make_data(
                    {'width': 1024, 'height': 768}
                ), 'example.jpg'
            )
        )
"""