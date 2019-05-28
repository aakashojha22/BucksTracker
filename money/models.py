

from django.db import models
from django.utils import timezone

from accounts.models import User

# Create your models here.
debt_type =  (
                    ('to_be_return', 'To be return'),
                    ('to_be_taken', 'To be Taken'),
                )



class TrackExpenses(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField( blank=True)
    amount = models.DecimalField(max_digits=7, decimal_places=2)
    date = models.DateField(default=timezone.now)
    user = models.ForeignKey(User,related_name='user',on_delete=models.CASCADE)
    #user = models.CharField(blank=True,max_length=253)
    def __str__(self):
        return self.title



class SplitBill(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField( blank=True)
    amount = models.DecimalField(max_digits=7, decimal_places=2)
    date = models.DateField(default=timezone.now)
    split_user = models.ForeignKey(User, related_name='split_user', on_delete=models.CASCADE)
    no_of_people = models.PositiveIntegerField()
    split_amount=models.PositiveIntegerField()
    def __str__(self):
        return self.title


class Debt(models.Model):
    debt_user = models.ForeignKey(User, related_name='debt_user', on_delete=models.CASCADE)
    description = models.TextField(blank=True)
    amount = models.DecimalField(max_digits=7, decimal_places=2)
    date = models.DateField(default=timezone.now)
    debt_to_user = models.ForeignKey(User, related_name='debt_to_user', on_delete=models.CASCADE)
    type_of_debt = models.CharField(max_length=50,choices=sorted(debt_type))

    def __str__(self):
        return str(self.debt_user)




