import datetime

from django.shortcuts import render, redirect
from .models import DjangoTestCompo
from .forms import CompoForm

# Create your views here.

# 入力値オブジェクト用リスト
input_compo_object_list = []

# 入力値オブジェクト
class InputCompoObject:
    def __init__(self):
        self.product_name = ''
        self.product_text = ''
        self.unit_price = 0
        self.qty = 0
        self.total = 0

# 構成入力フォームナンバー
compo_form_num = 0

def portal(request):
    return render(request, 'portal.html')

def compo_form(request):
    form = CompoForm
    global compo_form_num
    global input_compo_object_list
    # 入力値オブジェクト作成
    compo_obj = InputCompoObject()
    # 入力値オブジェクトへインプット関数
    def input_compo_object(element_num, product_name, product_text, unit_price, qty, total):
        input_compo_object_list[element_num].product_name = product_name
        input_compo_object_list[element_num].product_text = product_text
        input_compo_object_list[element_num].unit_price = unit_price
        input_compo_object_list[element_num].qty = qty
        input_compo_object_list[element_num].total = total

    # 構成登録ページ
    if request.method == 'POST':
        form = CompoForm(request.POST)

        # プレビューページへ
        if form.is_valid() and ('button_1' in request.POST):
            # トータル金額計算
            unit_price = int(form.data['unit_price'])
            qty = int(form.data['qty'])
            total_price = unit_price * qty

            context = { 'form': form,
                        'total_price': total_price,
                        'compo_num': compo_form_num + 1,
                        }
            # オブジェクトリストへオブジェクト追加
            input_compo_object_list.append(compo_obj)

            #オブジェクトへ入力
            input_compo_object(compo_form_num, form.data['product_name'], form.data['product_text'], form.data['unit_price'], form.data['qty'], total_price)

            return render(request, 'compo_preview.html', context = context)

        # もう一つ構成登録する
        elif form.is_valid() and ('button_2' in request.POST):
            compo_form_num += 1
            context = {
                    'form': form,
                    'compo_num': compo_form_num + 1
            }
            return render(request, 'compo_form.html', context = context) 


        elif form.is_valid() and ('button_3' in request.POST):
            # DB書き込み時間取得
            created_datetime = datetime.datetime.now()
            # DB書き込み
            for input_object in input_compo_object_list:
                compo_set = DjangoTestCompo.objects.create(
                    product_name = input_object.product_name,
                    product_text = input_object.product_text,
                    unit_price = input_object.unit_price,
                    qty = input_object.qty,
                    total = input_object.total,
                    created_datetime = created_datetime,
                )
                    
            # compo object list初期化
            input_compo_object_list = []
            compo_form_num = 0

            return redirect('/compo_list/')

    context = {
            'form': form,
            'compo_num': compo_form_num + 1
            }

    return render(request, 'compo_form.html', context)


def compo_list_data(request):
    data = DjangoTestCompo.objects.all()

    context = {
            'data': data,
            }
    return render(request, 'compo_list.html', context)
