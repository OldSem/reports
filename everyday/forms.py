# -*- coding: utf-8 -*-
from django import forms
from django.utils import timezone
from .models import personel,Contra,BTS,DTE



class ContraForm(forms.ModelForm):
    class Meta:
        model = Contra
        fields = ('edrpou','name','address')
        labels = {'edrpou':u'ЕДПРОУ','name':u'Название','address':u'Адресс'}
        values = {"save": u'Добавить'}

class BTSForm(forms.ModelForm):
    class Meta:
        model = BTS
        fields = ('ECP','UCN','adress','dn','contra')
        labels = {'ECP':u'ЕСР','UCN':u'УЧН','adress':u'Адресс','dn':u'Номер договора','contra':u'Контрагент'}
        values = {"save": u'Добавить'}


class personelForm(forms.ModelForm):

     class Meta:
         model = personel
         fields = ('Name', 'Position',)



DEPT_CHOICES = (('DTE',u'ДТЕ'),('DPRS',u'ДПРС'),('OASS',u'Отдел Аренды'),('ES',u'Энергетическая Служба'))

class DTEForm(forms.ModelForm):

    #executor = forms.ModelMultipleChoiceField(label=u'Исполнитель',widget=forms.CheckboxSelectMultiple, queryset=personel.objects.all())
    class Meta:

        model = DTE

        fields = ('created_date','dept','work','adress','rezult','executor','elapsed_time','note','car')
        labels = {'created_date':u'Дата','dept':u'Отдел','work':u'Вид работ','adress':u'Адресс объекта','rezult':u'Результат','executor':u'Исполнитель','elapsed_time':u'Затраченное время','note':u'Примечание','car':u'Автомобиль',}
        values = {"save":u'Добавить','rezult':u'выполнено'}
        widgets = {
            'executor': forms.CheckboxSelectMultiple(),
            'dept':forms.Select(choices=DEPT_CHOICES),
            'created_date':forms.SelectDateWidget()
        }

class dteFilter(forms.Form):
    datefilter = forms.DateField(widget=forms.SelectDateWidget(),initial=timezone.now())