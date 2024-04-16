from django.db import models
from django.db.models import Model, CharField, DateTimeField, ForeignKey, CASCADE, DecimalField, TextField, \
    SmallIntegerField, SlugField, ImageField, PositiveIntegerField
from django.utils.text import slugify


class BaseModel(models.Model):
    created_at = DateTimeField(auto_now_add=True)
    updated_at = DateTimeField(auto_now=True)

    class Meta:
        abstract = True


# Create your models here.
class Category(BaseModel):
    name = CharField(max_length=255)
    slug = SlugField(max_length=255, null=True, blank=True)

    def __str__(self):
        return f'{self.name}'

    def _get_unique_slug(self):
        slug = slugify(self.name)
        unique_slug = slug
        num = 1
        while Product.objects.filter(slug=unique_slug).exists():
            unique_slug = f'{slug}-{num}'
            num += 1
        return unique_slug

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        self.slug = self._get_unique_slug()
        if force_update is True:
            self.slug = slugify(self.name)
        return super().save(force_insert, force_update, using, update_fields)


class Product(BaseModel):
    name = CharField(max_length=255)
    category = ForeignKey('apps.Category', CASCADE)
    price = DecimalField(max_digits=10, decimal_places=2)
    description = TextField()
    quantity = SmallIntegerField(default=1)
    discount = SmallIntegerField(default=0)
    slug = SlugField(max_length=255, null=True, blank=True)

    def _get_unique_slug(self):
        slug = slugify(self.name)
        unique_slug = slug
        num = 1
        while Product.objects.filter(slug=unique_slug).exists():
            unique_slug = f'{slug}-{num}'
            num += 1
        return unique_slug

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        self.slug = self._get_unique_slug()
        if force_update is True:
            self.slug = slugify(self.name)
        return super().save(force_insert, force_update, using, update_fields)

    def __str__(self):
        return f'{self.name}'

    @property
    def discount_price(self):
        return self.price * self.discount / 100

    @property
    def sell_price(self):
        return self.price - self.discount_price


class ProductImages(Model):
    image = ImageField(upload_to='products/')
    product = ForeignKey('apps.Product', CASCADE, related_name='images')

    def __str__(self):
        return self.product.name


class Order(BaseModel):
    name = CharField(max_length=255)
    phone_number = CharField(max_length=20)
    product = ForeignKey('apps.Product', CASCADE, related_name='order')

    class Meta:
        verbose_name = 'buyurtma'
        verbose_name_plural = 'buyurtmalar'

