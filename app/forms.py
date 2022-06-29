from django import forms
from django.forms import ModelForm
from .models import*

#template para crear el formulario
class ProductoForm(ModelForm):

    nombre = forms.CharField(min_length=10,max_length=20)
    precio = forms.IntegerField(min_value=400)
	
    widgets = {
      'fecha_ingreso' : forms.SelectDateWidget(years=range(2020,2023))
    }

    class Meta:
        model = Producto
        fields = ['codigo','nombre','marca','precio','stock','descripcion','tipo','imagen','created_at', 'updated_at']
        enctype="multipart/form-data"


        
