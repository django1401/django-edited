from django.shortcuts import redirect
from django.views.generic import TemplateView
from ..cart import Cart

class PaymentView(TemplateView):
    template_name = 'course/cart.html'

    def post(self, request, *args, **kwargs):
        cart = Cart(request)
        cart.clear()
        return redirect(request.path_info)