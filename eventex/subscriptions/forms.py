from django import forms
from eventex.subscriptions.models import Subscription

class SubscriptionForm(forms.ModelForm):
    class Meta:
        model = Subscription
        fields = ('name', 'cpf', 'email', 'phone')