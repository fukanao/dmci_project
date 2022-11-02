import datetime

from django.shortcuts import render, redirect
from .models import DjangoTestCompo
from .forms import CompoForm

# Create your views here.

def portal(request):
    return render(request, 'portal.html')

def compo_form(request):
    form = CompoForm
    if request.method == 'POST':
        form = CompoForm(request.POST)

        if form.is_valid() and ('button_1' in request.POST):
            context = { 'form': form, } 
            return render(request, 'compo_preview.html', context = context)

        elif form.is_valid() and ('button_3' in request.POST):
            created_datetime = datetime.datetime.now()
            compo_set = DjangoTestCompo.objects.create(
                    product_name = form.data['product_name'],
                    product_text = form.data['product_text'],
                    created_datetime = created_datetime,
                    )
            print('#30', created_datetime)


            return redirect('/compo_list/')

    context = {
            'form': form,
            }

    return render(request, 'compo_form.html', context)


def compo_list_data(request):
    data = DjangoTestCompo.objects.all()

    context = {
            'data': data,
            }
    return render(request, 'compo_list.html', context)
