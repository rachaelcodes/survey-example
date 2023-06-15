import re

from django import forms
from django.core.exceptions import ValidationError


def is_cabinet_office_email(email_address):
    # TODO if actual service: check if there are other valid email address forms
    if not re.fullmatch('.*@cabinetoffice.gov.uk', email_address):
        raise ValidationError(f"Invalid email domain: {email_address}", code="invalid_email_domain")
    return True
    


class FeedbackForm(forms.Form):
    template_name = "feedback.html"
    email = forms.EmailField(required=False, validators=[is_cabinet_office_email])
    content = forms.TextInput()

