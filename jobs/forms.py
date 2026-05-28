from django import forms
from datetime import datetime

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
                             ) )
    
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
                                     )
                                )
    
    DAYS = (
        (1, 'MON'),
        (2, 'TUE'),
        (3, 'WED'),
        (4, 'THU'),
        (5, 'FRI')
    )
    
    days = forms.MultipleChoiceField(
        choices=DAYS,
        help_text='Select all days that you can work.',
        widget=forms.CheckboxSelectMultiple(
            attrs={
                'checked': True
                }
        ),
    )
    desired_hourly_wage = forms.DecimalField(
        widget=forms.TextInput(
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
    check = forms.BooleanField(label='I certify that the information I have provided is true.')