from django.shortcuts import render, HttpResponse, redirect
from .models import Client, Order
from .forms import OrderForm, ClientForm
#создаем views
def clients_list(request):
    context = {}
    context["clients"] = Client.objects.all()
    return render(request, 'clients.html', context)


def client_detail(request, id):
    contex = {
        "client": Client.objects.get(id=id)
        #SELECT * FROM Client WHERE id+id:
    }
    return render(request, "client_info.html", contex)

def order_list(request):
    context = {}
    context["clients"] = Order.objects.all()
    return render(request, 'orders.html', context)

def order_detail(request, id):
    context = {
        "order": Order.objects.get(id=id)
        #SELECT * FROM Clients WHERE id+id
    }
    return render(request, "order_info.html", context)

def client_update(request, id):
    contex = {}
    client_object = Client.objects.get(id=id)
    if request.method == "POST":
        form = ClientForm(request.POST, instance=client_object)
        if form.is_valid():
            client_object = form.save()

    contex["form"] = ClientForm(instance=client_object)
    return render(request, 'client_update.html', contex)

def create_order(request):
    if request.method == "POST":
        data = request.POST
        order = Order()
        order.name = data["name"]
        order.contacts = data["contacts"]
        order.descriptions = data["description"]
        order.save()
        return HttpResponse("Форма обработана")
    return render(request, 'core/order_form.html')


def order_djangoform(request):
    context = {}
    if request.method =="POST":
        order_form = OrderForm(request.POST)
        if order_form.is_valid():
            order_form.save()
            return HttpResponse("Форма обработана")
        return HttpResponse("Данные не валидны")
    context["order_form"] = OrderForm()
    return render(request, 'order_djangoform', context)