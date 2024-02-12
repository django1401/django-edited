from django.db import models
from .orderby import OrderBy
from courses.models import Course

class OrderItem(models.Model):
    order = models.ForeignKey(OrderBy, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Course, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    price = models.PositiveIntegerField()

    def __str__(self):
        return f'product item {self.id} for Order {self.order.id}'

