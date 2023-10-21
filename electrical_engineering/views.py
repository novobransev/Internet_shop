from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.views.generic import ListView, DetailView

from rating.models import Rating
from .forms import RatingForm
from .models import Product, Ip


class ElectricalEngineeringView(LoginRequiredMixin, ListView):
    model = Product
    template_name = 'electrical_engineering/main.html'
    context_object_name = 'all_products'  # Имя переменной, которая будет передаваться в шаблон


def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')  # В REMOTE_ADDR значение ip пользователя
    return ip


class ElectricalEngineeringDetailView(LoginRequiredMixin, DetailView):
    model = Product
    template_name = 'electrical_engineering/detail_product.html'
    context_object_name = 'detail_product'  # Имя переменной, которая будет передаваться в шаблон

    def get_context_data(self, **kwargs):
        context = super(ElectricalEngineeringDetailView, self).get_context_data(**kwargs)
        form = RatingForm()
        context['form'] = form
        context['views'] = Ip.objects.count()
        return context

    def post(self, request, *args, **kwargs):

        pk = kwargs.get('pk')

        if request.method == 'POST':
            electro_product = Product.objects.get(id=pk)
            new_rating = Rating(estimation=self.request.POST.get('estimation'), user=self.request.user,
                                from_product=electro_product)
            new_rating.save()

            return redirect('main_page')

    def get(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        ip = get_client_ip(request)
        electro_product = Product.objects.get(id=pk)

        if Ip.objects.filter(ip=ip).exists():
            electro_product.views.add(Ip.objects.get(ip=ip))
        else:
            Ip.objects.create(ip=ip)
            electro_product.views.add(Ip.objects.get(ip=ip))
        return super().get(request, *args, **kwargs)

