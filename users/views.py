from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import render, redirect
from django.contrib.auth.forms import PasswordChangeForm
from .forms import *


@user_passes_test(lambda user:user.is_superuser)
def users_management_view(request):
    return render(request, 'accounts/users_view.html', {'users': User.objects.all(),})


@user_passes_test(lambda user:user.is_superuser)
def edit_user(request, user_id):



    if request.method == 'POST':
        if request.POST.get('type') == 'details':
            details_form = CustomUserEditForm(request.POST, instance=User.objects.get(pk=user_id))
            if details_form.is_valid():
                details_form.save()

            password_form = CustomSetPasswordForm(User.objects.get(pk=user_id))

        elif request.POST.get('type') == 'password':
            password_form = CustomSetPasswordForm(data = request.POST, user = User.objects.get(pk=user_id))
            if password_form.is_valid():
                password_form.save() 
            
            details_form = CustomUserEditForm(instance=User.objects.get(pk=user_id))
        
        else:
            password_form = CustomSetPasswordForm(User.objects.get(pk=user_id))
            details_form = CustomUserEditForm(instance=User.objects.get(pk=user_id))

            

    else:
        details_form = CustomUserEditForm(instance=User.objects.get(pk=user_id))
        password_form = CustomSetPasswordForm(User.objects.get(pk=user_id))

    return render(request, 'accounts/user_view.html', {'details_form':details_form, 'password_form': password_form}) 



@user_passes_test(lambda user:user.is_superuser)
def add_user(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('user_view', user.pk) 
    else:
        form = CustomUserCreationForm()
    return render(request, 'accounts/add_user.html', {'form': form})



@user_passes_test(lambda user: not user.is_anonymous)
def profile(request):
    if request.method == 'POST':
        password_form = PasswordChangeForm(user = request.user)
        if password_form.is_valid():
            password_form.save()
            return redirect('profile') 
    else:
        password_form = PasswordChangeForm(user = request.user)


    return render(request, 'accounts/profile.html', {'password_form': password_form}) 
