from django import forms
from datetime import datetime
from django.core.exceptions import ValidationError
from django.core.validators import URLValidator

def validate_future_date(value):
    if value < datetime.now().date():
        raise ValidationError(
            message=f'{value} is in the past.', code='past_date'
        )

class JobApplicationForm(forms.Form):
    first_name = forms.CharField(help_text='Please enter first name',
                                 widget=forms.TextInput(
                                     attrs={
                                         'autofocus': True,
                                     }
                                 ))
    last_name = forms.CharField()
    email = forms.EmailField()
    website = forms.URLField(required=False,
                             widget = forms.URLInput(
                                 attrs={
                                     'placeholder': 'https://example.com',
                                     'size': '50'
                                 }
                             ),
                             validators=[URLValidator(schemes=['http','https'])]
                             )
    
    EMPLOYMENT_TYPE = (
        (None, '----------'),
        ('full-time', 'Full-time'),
        ('part-time', 'Part-time'),
        ('contract', 'Contract')
    )
    employment_type = forms.ChoiceField(choices=EMPLOYMENT_TYPE)
    
    YEARS = range(datetime.now().year, datetime.now().year+2)
    start_date = forms.DateField(help_text='The earliest date you can start working.',
                                     widget=forms.SelectDateWidget(
                                         years=YEARS,
                                         attrs={
                                             'style': 'width: 31%; display: inline-block; margin: 0 1%'
                                         }
                                     ),
                                     validators=[validate_future_date],
                                     error_messages= {'past_date': 'Please enter a future date.'}
                                )
    
    DAYS = (
        (1, 'MON'),
        (2, 'TUE'),
        (3, 'WED'),
        (4, 'THU'),
        (5, 'FRI')
    )
    
    available_days = forms.TypedMultipleChoiceField(
        choices=DAYS,
        coerce=int,
        help_text='Select all days that you can work.',
        widget=forms.CheckboxSelectMultiple(
            attrs={
                'checked': True
                }
        ),
    )
    desired_hourly_wage = forms.DecimalField(
        widget=forms.NumberInput(
            attrs={
                'min': '10.00',
                'max': '100.00',
                'step': '.25'
            }
        )
    )
    cover_letter = forms.CharField(
        widget=forms.Textarea(
            attrs={
                'cols': '75',
                'rows': '5'
            }
        )
    )
    confirmation = forms.BooleanField(label='I certify that the information I have provided is true.')