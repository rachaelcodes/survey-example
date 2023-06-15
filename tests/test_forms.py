from django.core.exceptions import ValidationError
from django.test import TestCase, SimpleTestCase

from pulse_survey.survey import forms


VALID_EMAIL = "valid@cabinetoffice.gov.uk"
INVALID_EMAIL = "invalid@example.com"
NOT_EMAIL = "not an email"

class FeedbackFormTest(TestCase):
    def test_not_email(self):
        form = forms.FeedbackForm({"email": NOT_EMAIL, "content": ""})
        form.is_valid()
        email_errors = form.errors["email"]
        self.assertTrue("Enter a valid email address" in str(email_errors))

    def test_not_cabinet_office_email(self):
        form = forms.FeedbackForm({"email": NOT_EMAIL, "content": ""})
        form.is_valid()
        email_errors = form.errors["email"]
        self.assertTrue("Invalid email domain" in str(email_errors))

    def test_valid_email(self):
        form = forms.FeedbackForm({"email": VALID_EMAIL, "content": "some feedback"})
        form.is_valid()
        no_email_errors = "email" not in form.errors
        self.assertTrue(no_email_errors)


class CabinetOfficeValidationTest(SimpleTestCase):
    def test_correct_email(self):
        result = forms.is_cabinet_office_email(VALID_EMAIL)
        self.assertTrue(result)

    def test_incorrect_email(self):
        with self.assertRaises(
            ValidationError,
            msg=f"Invalid email domain: {INVALID_EMAIL}"
        ):
            forms.is_cabinet_office_email(INVALID_EMAIL)


