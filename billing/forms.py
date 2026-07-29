from django import forms
from .models import Invoice
from plans.models import Plan


class InvoiceForm(forms.ModelForm):

    class Meta:
        model = Invoice

        exclude = [
            "invoice_no",
            "package_price",
            "final_amount",
            "balance",
        ]
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields["plan"].queryset = Plan.objects.filter(status="Active")
        widgets = {
            "customer": forms.Select(attrs={"class": "form-select"}),

            "plan": forms.Select(attrs={"class": "form-select"}),

            "discount_type": forms.Select(attrs={"class": "form-select"}),

            "discount_value": forms.NumberInput(attrs={"class": "form-control"}),

            "payment_received": forms.NumberInput(attrs={"class": "form-control"}),
        }