from django import forms
from .models import TrackExpenses,Debt,SplitBill



class AddExpensesForm(forms.ModelForm):

    class Meta():
        model = TrackExpenses
        fields=('title','description','amount')



class SplitBillForm(forms.ModelForm):

    class Meta():
        model = SplitBill
        fields=('title','description','amount','no_of_people')



class AddDebtForm(forms.ModelForm):

    class Meta():
        model = Debt
        fields=('debt_to_user','type_of_debt','description','amount')
