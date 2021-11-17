from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import * 
from .forms import OrderForm
# Create your views here.

def home(request):
	orders = Order.objects.all()
	customers = Customer.objects.all()

	tot_customers = customers.count()
	tot_orders = orders.count()

	delivered = orders.filter(status='Delivered').count()
	pending = orders.filter(status='Pending').count()


	return render(request, 'accounts/dashboard.html', {'orders':orders, 'custs':customers, 'delivered':delivered, 'pending':pending,'tot_orders':tot_orders,'tot_customers':tot_customers})

def products(request):
	products = Product.objects.all()
	return render(request, 'accounts/products.html', {'products':products})

def customer(request, pk):
	customer = Customer.objects.get(id=pk)
	orders = customer.order_set.all()
	tot_orders = orders.count()

	context = {'customer':customer, 'orders':orders,'tot_orders':tot_orders}
	return render(request, 'accounts/customer.html', context)

def createOrder(request, pk):
	customer = Customer.objects.get(id=pk)
	form = OrderForm(instance=customer)
	if request.method =='POST':
		
		form = OrderForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('/')

	context = {'form':form}
	return render(request, 'accounts/create_order.html', context)

def updateOrder(request, pk):
	order = Order.objects.get(id=pk)
	form = OrderForm(instance=order)

	if request.method =='POST':
		
		form = OrderForm(request.POST, instance=order)
		if form.is_valid():
			form.save()
			return redirect('/')


	context = {'form':form}
	return render(request, 'accounts/create_order.html', context)

def deleteOrder(request, pk):
	order = Order.objects.get(id=pk)

	if request.method =='POST':
		order.delete()
		return redirect('/')

	context = {'item':order}
	return render(request, 'accounts/delete.html', context)