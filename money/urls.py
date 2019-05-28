
from django.urls import path
from . import views


app_name='money'

urlpatterns = [
    #path('track_expenses', views.TrackExpenses.as_view(), name='track_expenses'),
    path('track_expenses', views.track_expenses, name='track_expenses'),
    path('add_expenses', views.add_expenses, name='add_expenses'),
    path('split_bill_list', views.split_bill_list, name='split_bill_list'),
    path('add_split_bill', views.add_split_bill, name='add_split_bill'),

    path('debt_list', views.debt_list, name='debt_list'),
    path('add_debt', views.add_debt, name='add_debt'),

]

