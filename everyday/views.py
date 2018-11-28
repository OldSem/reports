# -*- coding: utf-8 -*-
from django.shortcuts import render, get_object_or_404,redirect
from django.http import HttpResponse
import json
from django.db.models import Count
from django.core.serializers.json import DjangoJSONEncoder
from django.db.models import Max
from openpyxl import load_workbook
import datetime

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders



# Create your views here.
from .forms import personelForm, DTEForm, ContraForm, BTSForm,dteFilter,CarForm
from .models import DTE,Contra,BTS,Car
    





def report(request,d,m,y):



        dtes = DTE.objects.filter(created_date=datetime.date(int(y),int(m),int(d)))
        wb = load_workbook(u'z:\Отчеты отд\Ежедневные\Ежедневный Отчет Киевского Отделения_шаблон.xlsx')
        drivers = {u'Грива': 'D87', u'Снигирь': 'D88'}
        depts = {u'DTE':{'start':16,'rezult':'AQ','executor':'AZ','time':'BI','note':'BQ'},
                 u'DPRS':{'start':28,'rezult':'AQ','executor':'AZ','time':'BI','note':'BQ'},
                 u'OASS':{'start':38,'rezult':'AZ','executor':'BI','time':'BR','note':'BZ','contras':'AQ'},
                 u'ES':{'start':51,'rezult':'AZ','executor':'BI','time':'BR','note':'BZ','contras':'AQ'}}
        rp = wb.active
        rp['AN6'].value = datetime.date(int(y),int(m),int(d))
        rp['D87'].value = rp['D88'] = u''

        for i in dtes:
            row = depts[i.dept]['start']
            while rp['D'+str(row)].value!=None:
                row+=1
            rp['D'+str(row)].value = i.work
            rp['W'+str(row)].value = i.adress.ECP+'/'+i.adress.UCN
            rp['AG' + str(row)].value = i.adress.adress
            rp[depts[i.dept]['rezult'] + str(row)].value = i.rezult
            rp[depts[i.dept]['executor'] + str(row)].value=u''
            for j in i.executor.all():
                rp[depts[i.dept]['executor'] + str(row)].value+=j.Name+','
            rp[depts[i.dept]['time'] + str(row)].value = i.elapsed_time
            rp[depts[i.dept]['note'] + str(row)].value = i.note
            if i.dept in (u'Отдел Аренды',u'Энергетическая служба'):
                rp[depts[i.dept]['contras'] + str(row)].value = i.adress.dn+'/'
                if i.adress.contra!=None:
                    rp[depts[i.dept]['contras'] + str(row)].value+=i.adress.contra.name
            print row,' ',rp['B'+str(row)].value
            rp[drivers.get(i.car.driver)].value += rp['B'+str(row)].value+','
        wb.save(u'z:\Отчеты отд\Ежедневные\Ежедневный Отчет Киевского Отделения_'+rp['AN6'].value.strftime('%d-%m-%Y').decode('utf8')+u'.xlsx')

        fromaddr = "oldsem1976@gmail.com"
        toaddr = "dkulikov@it.od.ua"

        msg = MIMEMultipart()

        msg['From'] = 'Александр Семешко'
        msg['To'] = 'dkulikov'

        msg['Subject'] = "Ежедневный Отчет Киевского Отделения_"+rp['AN6'].value.strftime('%d-%m-%Y')

        filename = msg['Subject']+'.xlsx'
        attachment = open(u'z:\Отчеты отд\Ежедневные\Ежедневный Отчет Киевского Отделения_'+rp['AN6'].value.strftime('%d-%m-%Y').decode('utf8')+u'.xlsx', "rb")
        p = MIMEBase('application', 'octet-stream')
        p.set_payload((attachment).read())
        encoders.encode_base64(p)
        p.add_header('Content-Disposition', "attachment; filename= %s" % filename)

        msg.attach(p)

        s = smtplib.SMTP_SSL('smtp.gmail.com', port=465)
        s.login('oldsem1976@gmail.com', 'sem230676')
        s.sendmail(fromaddr, toaddr, msg.as_string())
        s.quit()





        return redirect('/dtes')


def frame(request):
    return render(request,'parser/frame.html')


def dte_list(request):

    dtes = DTE.objects.order_by('-created_date')[:20]

    if request.method == "POST":
        form = dteFilter(request.POST)
        if form.is_valid():

            datefilter=form.cleaned_data['datefilter']
            dtes = DTE.objects.filter(created_date=datefilter)[:30]


            return render(request, 'everyday/dtes.html', {'form': form, 'dtes': dtes})


    else:
        form = dteFilter()

    return render(request, 'everyday/dtes.html', {'form': form,'dtes': dtes})




def personel_new(request):
        if request.method == "POST":
                form = personelForm(request.POST)
                if form.is_valid():
                        personel = form.save(commit=False)

                        personel.save()

        else:
                form = personelForm()
        return render(request, 'everyday/personel_edit.html', {'form': form})


def dte_edit(request, nn):
        dte = get_object_or_404(DTE, nn=nn)
        if request.method == "POST":
                form = DTEForm(request.POST, instance=dte)
                if form.is_valid():
                        dte = form.save(commit=False)
                        dte.save()
                        form.save_m2m()
                        return redirect('dte_list')
        else:
                form = DTEForm(instance=dte)
        return render(request, 'everyday/new_dte.html', {'form': form})



def new_dte(request):

        if request.method == "POST":
                form = DTEForm(request.POST)
                if form.is_valid():
                        dte = form.save(commit=False)
                        dte.nn = max([int(i.values()[0]) for i in list(DTE.objects.values('nn'))]) + 1

                        dte.save()
                        form.save_m2m()
                        return redirect('dte_list')

        else:
                form = DTEForm()
        return render(request, 'everyday/new_dte.html', {'form': form})

def get_work(request):
        work_list = []
        starts_with = ''
        if request.method == 'GET':
                starts_with = request.GET['wk']
        print starts_with
        work_list = DTE.objects.filter(work__icontains=starts_with).values('work').annotate(nw=Count('work'))
        wl=json.dumps(list(work_list), cls=DjangoJSONEncoder)
        #work_list = [entry for entry in work_list]
        #work_list = work_list[0]



        return HttpResponse(wl, content_type='application/json')


def contra_new(request):
        if request.method == "POST":
                form = ContraForm(request.POST)

                if form.is_valid():
                        contra = form.save(commit=False)
                        contra.save()
                        form.save_m2m()
                        return redirect('contras')

        else:
                form = ContraForm()
        return render(request, 'everyday/contra.html', {'form': form})


def contra_edit(request, nn):
        contra = get_object_or_404(Contra, edrpou=nn)
        if request.method == "POST":
                form = ContraForm(request.POST, instance=contra)
                if form.is_valid():
                        contra = form.save(commit=False)
                        contra.save()
                        form.save_m2m()
                        return redirect('contras')
        else:
                form = ContraForm(instance=contra)
        return render(request, 'everyday/contra.html', {'form': form})





def contras(request):
    contras = Contra.objects.order_by('edrpou')
    return render(request, 'everyday/contras.html', {'contras': contras})


def car_edit(request, nn):
    car = get_object_or_404(Car, pk=nn)
    if request.method == "POST":
        form = CarForm(request.POST, instance=car)
        if form.is_valid():
            car = form.save(commit=False)
            car.save()
            form.save_m2m()
            return redirect('cars')
    else:
        form = CarForm(instance=contra)
    return render(request, 'everyday/entity.html', {'form': form,'entity':u'Автомобиля'})


def car_new(request):
    if request.method == "POST":
        form = CarForm(request.POST)

        if form.is_valid():
            car = form.save(commit=False)
            car.save()
            form.save_m2m()
            return redirect('cars')

    else:
        form = CarForm()
    return render(request, 'everyday/entity.html', {'form': form,'entity':u'Автомобиля'})

def cars(request):
    cars = Car.objects.order_by('dn')
    return render(request, 'everyday/cars.html', {'cars': cars})



def bts_new(request):
            if request.method == "POST":
                    form = BTSForm(request.POST)

                    if form.is_valid():
                            bts = form.save(commit=False)
                            bts.save()
                            form.save_m2m()
                            return redirect('btss')

            else:
                    form = BTSForm()
            return render(request, 'everyday/BTS.html', {'form': form})


def bts_edit(request, nn):
        bts = get_object_or_404(BTS, ECP=nn)
        if request.method == "POST":
                form = BTSForm(request.POST, instance=bts)
                if form.is_valid():
                        bts = form.save(commit=False)
                        bts.save()
                        form.save_m2m()
                        return redirect('BTSs')
        else:
                form = BTSForm(instance=bts)
        return render(request, 'everyday/BTS.html', {'form': form})


def btss(request):
        btss = BTS.objects.order_by('ECP')
        return render(request, 'everyday/BTSs.html', {'btss': btss})


