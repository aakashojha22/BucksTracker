from django.contrib import admin
from .models import TrackExpenses,Debt,SplitBill
# Register your models here.
admin.site.register(TrackExpenses)
admin.site.register(SplitBill)
admin.site.register(Debt)