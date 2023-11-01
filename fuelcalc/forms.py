from django import forms


class AddFuelForm(forms.Form):
    """Form for adding fuel"""

    liters = forms.IntegerField(label="Liters")
    distance = forms.IntegerField(label="Distance")
    cost = forms.IntegerField(label="Cost")


class ContactForm(forms.Form):
    subject = forms.CharField(max_length=100)
    messsage = forms.CharField(widget=forms.Textarea)
    sender = forms.EmailField()
    cc_myself = forms.BooleanField(required=False)
