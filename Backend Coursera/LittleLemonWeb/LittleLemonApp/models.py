from django.db import models

# Create your models here.
class Booking(models.Model):
    name = models.CharField(max_length=255, null=False)
    no_of_guests = models.SmallIntegerField(null=False)
    booking_date = models.DateTimeField(auto_now_add=True)

class MenuItem(models.Model):
    title = models.CharField(max_length=255, null=False)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=False)
    inventory = models.SmallIntegerField()

    def get_item(self):
        return f'{self.title} : {str(self.price)}'
