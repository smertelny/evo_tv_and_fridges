from django.db import models
from django.utils.translation import gettext_lazy as _
from django.shortcuts import reverse


class ProductType(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return str(_("Product type: {}".format(self.name)))

    class Meta:
        verbose_name = _("product type")
        verbose_name_plural = _("product types")


class Product(models.Model):
    name = models.CharField(
        max_length=70,
        verbose_name=_("name")
    )
    clicks = models.IntegerField(default=0)
    type = models.ForeignKey(ProductType, null=True, on_delete=models.SET_NULL)

    def get_absolute_url(self):
        return reverse('core:details', args=[str(self.id)])

    def __str__(self):
        return str(_(f"{self.__class__.__name__}: {self.name} -- {self.clicks}"))

    class Meta:
        verbose_name = _("product")
        verbose_name_plural = _("products")
        ordering = ['name']
    