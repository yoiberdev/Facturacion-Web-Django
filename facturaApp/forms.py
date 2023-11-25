from django import forms

class createNewCliente(forms.Form):
    cliente = forms.CharField(label="Nombre del cliente", max_length=200, widget=forms.TextInput(attrs={'class': 'input'}))
    dni = forms.CharField(label="Dni del cliente", widget=forms.TextInput(attrs={'class': 'input'}))
    direccion = forms.CharField(label="Direccion del cliente", widget=forms.TextInput(attrs={'class': 'input'}))
    ruc = forms.CharField(label="Ruc", widget=forms.TextInput(attrs={'class': 'input'}))
    producto = forms.CharField(label="Nombre de producto", widget=forms.TextInput(attrs={'class': 'input1'}))
    precio = forms.CharField(label="Precio de producto", widget=forms.TextInput(attrs={'class': 'input1'}))
    cantidad = forms.CharField(label="Cantidad de producto", widget=forms.TextInput(attrs={'class': 'input1'}))
    