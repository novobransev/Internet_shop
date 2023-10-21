from django.contrib.auth.decorators import login_required
from django.shortcuts import render


@login_required
def main_page(request):
    return render(request, 'main/main_page.html', {'user_id': request.user.id})
