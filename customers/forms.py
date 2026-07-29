from django import forms
from .models import Customer


class CustomerForm(forms.ModelForm):

    class Meta:
        model = Customer
        fields = "__all__"

        widgets = {

            "customer_code": forms.TextInput(
                attrs={"class": "form-control"}
            ),

            "first_name": forms.TextInput(
                attrs={"class": "form-control"}
            ),

            "last_name": forms.TextInput(
                attrs={"class": "form-control"}
            ),

            "phone": forms.TextInput(
                attrs={"class": "form-control"}
            ),

            "email": forms.EmailInput(
                attrs={"class": "form-control"}
            ),

            "gender": forms.Select(
                attrs={"class": "form-select"}
            ),

            "age": forms.NumberInput(
                attrs={"class": "form-control"}
            ),

            "joining_date": forms.DateInput(
                attrs={
                    "class": "form-control",
                    "type": "date",
                }
            ),

            "status": forms.Select(
                attrs={"class": "form-select"}
            ),
        }