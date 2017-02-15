# -*- coding: utf-8 -*-

from django.forms import ModelForm
from django import forms
from .models import Page1
from .models import EntDbSpr
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, ButtonHolder, Submit, Button
from django.forms.models import inlineformset_factory
from crispy_forms.layout import Fieldset
from django.forms.formsets import BaseFormSet



class Page1Form(forms.ModelForm):

   class Meta:
       model = Page1
       fields=['kod_okpo','kod_unn','kod_gvk','wateruser_name','wateruser_level_name','postal_address','email_address','territory_level','kod_soato']

       widgets = {'kod_unn': forms.TextInput(
           attrs={'id': 'kod_unn', 'required': True, 'placeholder': 'Введите код УНП (9-ти значнный)',
                  'title': 'Введите код УНП (9-ти значный)',
                  'pattern': '[0-9]{9}',
                  }
       ),
           'kod_okpo': forms.TextInput(
               attrs={'id': 'kod_okpo', 'required': True, 'placeholder': 'Введите код ОКПО (12-ти значный)',
                      'title': 'Введите код ОКПО  10 - 12-ти значный',
                      'pattern':'[0-9]{10,11,12}',
                       }
           ),
           'kod_gvk': forms.TextInput(
               attrs={'maxlenght': '35', 'size': '45', 'id': 'kod_gvk', 'required': True,
                      'placeholder': 'Введите код ГВК',
                      'title': 'Введите код ГВК  (6-7-ти значный код)',
                      'pattern': '[0-9]{5,6}',
                      }
           ),
           'wateruser_name': forms.Textarea(
               attrs={'id': 'wateruser_name', 'required': True,
                      'placeholder': 'Введите полное наименование юридического лица',
                      'title': 'Введите полное наименование юридического лица',
                      'rows':'2',
                      'cols':'10',
                      }
           ),
           'wateruser_level_name': forms.Textarea(
               attrs={'id': 'wateruser_level_name', 'required': True,
                      'placeholder': 'Введите полное наименование обособленного подразделения юридического лица',
                      'title': 'Введите полное наименование обособленного подразделения юридического лица',
                      'rows': '2',
                      'cols': '10',
                      }
           ),
           'postal_address': forms.Textarea(
               attrs={'id': 'postal_address', 'required': True,
                      'placeholder': 'Введите почтовый адрес (фактический)',
                      'title': 'Введите почтовый адрес (фактический)',
                      'rows': '2',
                      'cols': '10',
                      }
           ),
                 'email_address': forms.EmailInput(
           attrs={'id': 'email_address', 'required': True,
                  'placeholder': 'Введите электронный адрес (e-mail)',
                  'title': 'Введите электронный адрес (e-mail)',
                  'error_messages':{'invalid': 'Mail invalido'} }
       ),
           'territory_level': forms.TextInput(
               attrs={'id': 'territory_level', 'required': True,
                      'placeholder': 'Введите территорию нахождения структурного подразделения',
                      'title': 'Введите территорию нахождения структурного подразделения',
                      }
           ),
           'kod_soato': forms.Select(
               attrs={'id': 'kod_soato', 'required': True,'label':'',
                      'placeholder': 'Введите',
                      'title': 'Введите код СОАТО, который соответствует территории нахождения водопользователя',
                      }

           )
       }

   def __init__(self, *args, **kwargs):
       super(Page1Form, self).__init__(*args, **kwargs)
       self.helper = FormHelper()
       self.helper.form_id = 'id-exampleForm'
       self.helper.field_class = 'col-lg-12'
       self.helper.form_class = 'blueForms'
       self.helper.form_method = 'POST'
       self.helper.form_action = ''
       self.helper.html5_required=True
       self.helper.add_input(Submit('submit', 'Принять введенные данные и перейти к Разделу 1 "Водопотребление"'))


class ObjectsListFormHelperFind(FormHelper):
    model = EntDbSpr
    form_show_errors = False
    form_error_title = False
    help_text_inline = True
    html5_required = True
    form_tag = True
    form_class = 'form-inline'
    layout = Layout('gup','npr','oku',ButtonHolder(
        Submit('submit', u'Осуществить запрос ', css_class='btn-primary ',),

    ))