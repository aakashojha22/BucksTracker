from django.shortcuts import render,redirect
from .models import TrackExpenses,Debt,SplitBill
from .forms import AddExpensesForm,AddDebtForm,SplitBillForm
from django.contrib.auth.decorators import login_required


# Create your views here.

@login_required
def track_expenses(request):
    data=TrackExpenses.objects.order_by('-date')
    data_dict={'expenses':data}

    return render(request,'money/trackexpenses_list.html',context=data_dict)

@login_required
def add_expenses(request):
    form = AddExpensesForm()
    if request.method == "POST":
        form = AddExpensesForm(request.POST)
        if form.is_valid():

            request_detail = form.save(commit=False)
            request_detail.user=request.user
            request_detail.save()
            return redirect('money:track_expenses')
    return render(request, 'money/add_expenses_form.html', {'form': form})

"""~~~~~~~~~~~~~~~~~~~~~~~~~~~spilt bill~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"""


@login_required
def split_bill_list(request):
    data=SplitBill.objects.order_by('-date')
    data_dict={'bill':data}

    return render(request,'money/split_bill_list.html',context=data_dict)

@login_required
def add_split_bill(request):
    form = SplitBillForm()
    if request.method == "POST":
        form = SplitBillForm(request.POST)
        if form.is_valid():

            request_detail = form.save(commit=False)
            request_detail.split_user=request.user
            no_of_people = form.cleaned_data['no_of_people']
            amount = form.cleaned_data['amount']
            request_detail.split_amount=amount/no_of_people
            request_detail.save()
            return redirect('money:split_bill_list')
    return render(request, 'money/split_bill_form.html', {'form': form})



"""~~~~~~~~~~~~~~~~~~~add debt~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"""


@login_required
def debt_list(request):
    data=Debt.objects.order_by('-date')
    data_dict={'debt':data}

    return render(request,'money/debt_list.html',context=data_dict)

@login_required
def add_debt(request):
    form = AddDebtForm()
    if request.method == "POST":
        form = AddDebtForm(request.POST)
        if form.is_valid():

            request_detail = form.save(commit=False)
            request_detail.debt_user=request.user
            request_detail.save()
            return redirect('money:debt_list')
    return render(request, 'money/add_debt_form.html', {'form': form})

