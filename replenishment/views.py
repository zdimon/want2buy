# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from replenishment.froms import ReplanishmentForm
from django.http import HttpResponse
from want2buy.settings import LIQPAY_PUBLIC_KEY, LIQPAY_PRIVATE_KEY
from liqpay import LiqPay
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView, View
from django.views.decorators.csrf import csrf_exempt


# Create your views here.

class PayView(TemplateView):
    template_name = 'replenishment/liqpay.html'

    def get(self, request, *args, **kwargs):
        liqpay = LiqPay(LIQPAY_PUBLIC_KEY, LIQPAY_PRIVATE_KEY)

        params = {
            'action': 'pay',
            'amount': '100',
            'currency': 'USD',
            'description': 'Payment for clothes',
            'order_id': 'order_id_2',
            'version': '3',
            'sandbox': '1',  # sandbox mode, set to 1 to enable it
            'server_url': 'localhost:8000/pay-callback/',  # url to callback view
        }
        signature = liqpay.cnb_signature(params)
        data = liqpay.cnb_data(params)
        return render(request, self.template_name, {'signature': signature, 'data': data})

        # args = {}
        # if request.method == 'POST':
        #     print '---------------------'+request.POST['ammount']
        #     form = ReplanishmentForm(request.POST)
        #
        #     if form.is_valid():
        #         profile = request.user.profile
        #         profile.account = profile.account + int(request.POST['ammount'])
        #         profile.save()
        #         return redirect('/')
        #     else:
        #         print form.errors
        # else:
        #     args['form'] = ReplanishmentForm()

        # return render(request, 'replenishment/replenishment.html', args)


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
        print('callback data', response)
        return HttpResponse()
