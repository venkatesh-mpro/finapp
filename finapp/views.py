from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Customer
from .forms import LoanHistoryForm
from datetime import datetime, timedelta
from django.db import IntegrityError


def add_customer(request):
    return render(request, "addCustomer.html")


def save_customer(request):
    if request.method == "POST":
        name = request.POST.get("name").title()
        email = request.POST.get("email")
        phone_number = request.POST.get("phoneNumber")
        address = request.POST.get("address")
        loan_amount = request.POST.get("loanAmount")
        paid_amount = request.POST.get("paidAmount")
        join_date = request.POST.get("joinDate")

        customer = Customer(
            name=name,
            phone_number=phone_number,
            address=address,
            loan_amount=loan_amount,
            paid_amount=paid_amount,
            join_date=join_date,
        )
        try:
            customer.save()
        except IntegrityError:
            return HttpResponse('<h1 style="text-align: center;">The phone number is not unique.</h1>', status=400)
        except Exception as e:
            print(str(e))

        return HttpResponse(
            """<h1 style="text-align: center;">Customer details submitted!</h1>
            <div class="button-container" style="text-align: center;">
                <button onclick="window.location.href='/home/customers/'">Customers</button>
            </div>
            """
        )

    return redirect("/")


def list_customers(request):
    customers = Customer.objects.all()
    return render(request, "customers.html", {"customers": customers})


def view_customer(request):
    customer = Customer.objects.get(id=request.GET['id'])

    if request.method == 'POST':
        form = LoanHistoryForm(request.POST)
        if form.is_valid():
            date = form.cleaned_data['date'].strftime('%Y-%m-%d')
            amount_given = form.cleaned_data['amount_given']
            customer.loan_history[date] = str(amount_given)
            customer.save()
            return redirect('/home/customer'+f'?id={customer.id}')
    else:
        form = LoanHistoryForm()
    
    return render(request, 'customer.html', {
        'customer': customer,
        'form': form
    })


def summary(request):
    today = datetime.now().date()
    customers = []

    all_customers = Customer.objects.all()

    for customer in all_customers:
        missed_dates = []

        total_days = (today - customer.join_date).days
        expected_payment_dates = [customer.join_date + timedelta(days=i) for i in range(total_days)]

        loan_history = customer.loan_history or {}

        for date in expected_payment_dates:
            date_str = date.strftime('%Y-%m-%d')
            if date_str not in loan_history or float(loan_history[date_str]) < customer.loan_amount * 0.01:
                missed_dates.append(date)

        if missed_dates:
            customers.append({
                'name': customer.name,
                'loan_amount': customer.loan_amount,
                'missed_dates': missed_dates,
                'pending_payment': int(len(missed_dates) * (customer.loan_amount * 0.01))
            })

    context = {
        'customers': customers,
        'total': sum([i['pending_payment'] for i in customers]),
    }
    
    return render(request, 'summary.html', context)