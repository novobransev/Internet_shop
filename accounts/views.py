from django.contrib.auth.views import PasswordResetView
from django.contrib.auth.models import User
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView

from .forms import UserRegisterForm


class ValidatePasswordResetView(PasswordResetView):

    def form_valid(self, form):
        email = form.cleaned_data['email']  # Получение значения поля email из формы
        # Дальнейшая проверка или действия на основе значения email
        # Пример проверки и вывода значения на консоль:

        if email in User.objects.values_list('email', flat=True):
            return super().form_valid(form)
        else:
            return render(self.request, 'registration/password_reset_form.html',
                          {'error': 'Вы ввели неправильный адрес почты'})


class SignUpView(CreateView):
    form_class = UserRegisterForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'
