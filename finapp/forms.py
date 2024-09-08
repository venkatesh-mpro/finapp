from django import forms

class LoanHistoryForm(forms.Form):
    date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    amount_given = forms.DecimalField(max_digits=10, decimal_places=2)
