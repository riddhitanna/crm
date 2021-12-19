from django.forms import ModelForm 
from .models import * 
from django.contrib.auth import get_user_model

class OrderForm(ModelForm):
	class Meta:
		model = Order
		fields = '__all__'

class CustomerForm(ModelForm):
	class Meta:
		model = Customer
		fields = '__all__'

class ProductForm(ModelForm):
	class Meta:
		model = Product
		fields = '__all__'

