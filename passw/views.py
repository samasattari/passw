
from django.shortcuts import HttpResponse
from django.shortcuts import render , redirect
from .models import Password
from .forms import PasswordForm


def password_view(request):
<<<<<<< HEAD
    form = PasswordForm()
    if  request.method == 'POST':
        form = PasswordForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data['username'],
            password = form.cleaned_data['password'],
            url = form.cleaned_data['url'],
            form.save()
=======

    # form = PasswordForm()
    if request.method == 'POST':
        form = PasswordForm(request.POST)


        if form.is_valid():
            form.save()
            
            # return redirect("")
>>>>>>> 0b50ab174f8487bfb9251c38ae057b0dab5d2f96

    password_list = Password.objects.all()
    context = {}
    context["passwords"] = password_list
    context["form"] = form
    template_name = 'passw/password_list.html'
    return render(request, template_name, context)



