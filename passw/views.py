
from django.shortcuts import HttpResponse
from django.shortcuts import render
from .models import Password
from .forms import PasswordForm


def password_view(request):
    form = PasswordForm()
    if  request.method == 'POST':
        form = PasswordForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data['username'],
            password = form.cleaned_data['password'],
            url = form.cleaned_data['url'],
            form.save()

    password_list = Password.objects.all()
    context = {}
    context["passwords"] = password_list
    context["form"] = form
    template_name = 'passw/password_list.html'
    return render(request, template_name, context)



