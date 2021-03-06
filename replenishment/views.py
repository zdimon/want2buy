# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from replenishment.froms import ReplanishmentForm
from django.http import HttpResponse
from want2buy.settings import LIQPAY_PUBLIC_KEY, LIQPAY_PRIVATE_KEY
from liqpay import LiqPay
from django.shortcuts import render, redirect
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView, View
from django.views.decorators.csrf import csrf_exempt
from .models import Replanishment
from account.models import Profile
import decimal
from want2buy.settings import DOMAIN_NAME


# Create your views here.


def replenishment_page(request):
    args = {}
    if request.method == 'POST':
        form = ReplanishmentForm(request.POST)
        if form.is_valid():
            amount = request.POST['ammount']
            rep = Replanishment()
            rep.ammount = amount
            rep.user_replanishment = request.user
            rep.save()
            request.session['payment_id'] = rep.id
            return redirect('/pay', payment_id=rep.id)
        else:
            print form.errors
    else:
        args['form'] = ReplanishmentForm()

    return render(request, 'replenishment/replenishment.html', args)


class PayView(TemplateView):
    template_name = 'replenishment/liqpay.html'

    def get(self, request, *args, **kwargs):
        liqpay = LiqPay(LIQPAY_PUBLIC_KEY, LIQPAY_PRIVATE_KEY)
        amount = Replanishment.objects.get(id=request.session['payment_id']).ammount
        print request.user
        params = {
            'action': 'pay',
            'amount': amount,
            'currency': 'UAH',
            'description': 'Пополнение аккаунта',
            'order_id': request.session['payment_id'],
            'version': '3',
            'sandbox': '1',
            'server_url': 'https://%s/pay-callback/' % DOMAIN_NAME,
        }
        signature = liqpay.cnb_signature(params)
        data = liqpay.cnb_data(params)
        return render(request, self.template_name, {'signature': signature, 'data': data})


@method_decorator(csrf_exempt, name='dispatch')
class PayCallbackView(View):
    def post(self, request, *args, **kwargs):
        liqpay = LiqPay(LIQPAY_PUBLIC_KEY, LIQPAY_PRIVATE_KEY)
        data = request.POST.get('data')
        signature = request.POST.get('signature')
        sign = liqpay.str_to_sign(LIQPAY_PRIVATE_KEY + data + LIQPAY_PRIVATE_KEY)
        if sign == signature:
            print('callback is valid')
        response = liqpay.decode_data_from_str(data)
        if len(response) != 0:
            oreder_id = response['order_id']
            status = response['status']
            rep = Replanishment.objects.get(id=oreder_id)
            rep.status = status
            rep.save()
            if status == 'sandbox':
                profile = Profile.objects.get(user_id=rep.user_replanishment_id)
                profile.account = profile.account + decimal.Decimal(rep.ammount)
                profile.save()

        print('callback data', response)
        return HttpResponse()
