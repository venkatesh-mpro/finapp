from django.shortcuts import render
from django.http import HttpResponse
from .models import Customer


def add_customer(request):
    return render(request, "addCustomer.html")


def save_customer(request):
    if request.method == "POST":
        first_name = request.POST.get("firstName")
        last_name = request.POST.get("lastName")
        email = request.POST.get("email")
        phone_number = request.POST.get("phoneNumber")
        address = request.POST.get("address")
        loan_amount = request.POST.get("loanAmount")
        paid_amount = request.POST.get("paidAmount")
        join_date = request.POST.get("joinDate")

        customer = Customer(
            first_name=first_name,
            last_name=last_name,
            phone_number=phone_number,
            address=address,
            loan_amount=loan_amount,
            paid_amount=paid_amount,
            join_date=join_date,
        )
        customer.save()

        return HttpResponse(
            """<h1 style="text-align: center;">Customer details submitted!</h1>
            <div class="button-container" style="text-align: center;">
                <button onclick="window.location.href='/home/customers/'">Customers</button>
            </div>
            """
        )

    return redirect("/")


def list_customer(request):
    customers = Customer.objects.all()
    return render(request, "customers.html", {"customers": customers})


def home_page(request):
    return render(request, "homePage.html")


def summary(request):
    return render(request, "summary.html")