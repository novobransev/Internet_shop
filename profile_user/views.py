from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import DetailView, UpdateView

from .forms import ProfileForm
from .models import Profile


class ProfileView(LoginRequiredMixin, DetailView):
    model = Profile
    template_name = 'profile_user/profile_user.html'

    def get_context_data(self, **kwargs):
        context = super(ProfileView, self).get_context_data(**kwargs)
        context['user_id'] = self.request.user.id
        return context


class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    model = Profile
    form_class = ProfileForm
    template_name = 'profile_user/update_profile_user.html'
    success_url = reverse_lazy('main_page')

    def get_context_data(self, **kwargs):
        context = super(ProfileUpdateView, self).get_context_data(**kwargs)
        context['user_id'] = self.request.user.id
        return context
