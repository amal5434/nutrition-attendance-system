from django import forms
from .models import Plan


class PlanForm(forms.ModelForm):

    class Meta:
        model = Plan
        fields = "__all__"

        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control"}),

            "plan_type": forms.Select(attrs={"class": "form-select"}),

            "price": forms.NumberInput(attrs={"class": "form-control"}),

            "attendance_days": forms.NumberInput(attrs={"class": "form-control"}),

            "description": forms.Textarea(attrs={
                "class": "form-control",
                "rows": 3
            }),

            "status": forms.Select(attrs={"class": "form-select"}),
        }