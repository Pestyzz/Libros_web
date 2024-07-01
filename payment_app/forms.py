from django import forms

class PaymentForm(forms.Form):
    name = forms.CharField(max_length=100, label="Nombre Completo")
    email = forms.EmailField(label="Correo Electrónico")
    address = forms.CharField(max_length=255, label="Dirección")
    phone = forms.CharField(max_length=9, label="Teléfono", required=False)
    card_proprietary = forms.CharField(max_length=100, label="Propietario de la Tarjeta")
    card_number = forms.CharField(max_length=16, label="Número de Tarjeta")
    card_exp_date = forms.CharField(max_length=7, label="Fecha de Expiración (MM/AAAA)")
    card_cvv = forms.CharField(max_length=3, label="CVV")
    amount = forms.DecimalField(max_digits=10, decimal_places=2, label="Monto a Pagar", widget=forms.HiddenInput())
