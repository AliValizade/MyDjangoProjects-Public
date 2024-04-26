from django.db import models
from django.conf import settings
from django.utils.translation import gettext as _


class Order(models.Model):
    customer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name=_('Customer'))
    is_paid = models.BooleanField(_('Is Paid?'), default=False)

    first_name = models.CharField(_('First Name'), max_length=100)
    last_name = models.CharField(_('Last Name'), max_length=100)
    phon_number = models.CharField(_('Phone Number'), max_length=11)
    address = models.CharField(_('Address'), max_length=700)

    order_note = models.CharField(_('Order Notes'), max_length=700, blank=True)

    datetime_created = models.DateTimeField(_('Created Date'), auto_now_add=True)
    datetime_modified = models.DateTimeField(_('Modified Date'), auto_now=True)

    def __str__(self):
        return f'Order {self.id}'

    def get_total_price(self):
        return sum(item.quantity * item.price for item in self.items.all())
    
    class Meta:
        verbose_name = _("Order")
        verbose_name_plural = _("Order")


class OrderItem(models.Model):
    order = models.ForeignKey(Order, verbose_name=_("Order"), on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey('products.Product', verbose_name=_("Product"), on_delete=models.CASCADE, related_name='order_items')
    quantity = models.PositiveIntegerField(_("Quantity"), default=1)
    price = models.PositiveIntegerField(_("Price"))

    def __str__(self):
        return f'OrderItem {self.id}: {self.product} X {self.quantity} (price: {self.price})'
    
    class Meta:
        unique_together = [['order', 'product']]
        verbose_name = _("OrderItem")
        verbose_name_plural = _("OrderItem")
