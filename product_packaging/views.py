from django.shortcuts import render, redirect
from django.contrib.auth.decorators import user_passes_test
from .models import *
from .forms import *


@user_passes_test(lambda user: user.is_superuser)
def edit_packaging_group(request, group_id):

    group = Packaging_Group.objects.get(pk = group_id)

    if request.method == 'POST':

        edit_form = PackagingGroupForm(instance=group, data= request.POST)
        if edit_form.is_valid():
            group = edit_form.save()

    else:
        edit_form = PackagingGroupForm(instance=group)

    
    return render(request, 'packaging/edit_packaging_group.html', {'edit_form': edit_form})



@user_passes_test(lambda user: user.is_superuser)
def add_packaging_group(request):
    if request.method == 'POST':
        creation_form = PackagingGroupForm(request.POST)
        if creation_form.is_valid():
            group = creation_form.save()
            return redirect('edit_packaging_group', group.pk) 

    else:
        creation_form = PackagingGroupForm()

    return render(request, 'packaging/add_packaging_group.html', {'creation_form': creation_form})



@user_passes_test(lambda user: user.is_superuser)
def edit_package_s2i(request, package_id):

    package = Package_S2I.objects.get(pk = package_id)
    edit_form = PackageS2IForm(instance=package)

    if request.method == 'POST':
        if request.POST.get('submit_type') == 'save':
            if edit_form.is_valid():
                package = edit_form.save()
        
        elif request.POST.get('submit_type') == 'set_as_send':
            package.set_as_send()
            


    
    return render(request, 'packaging/edit_package_s2i.html', {'edit_form': edit_form})



@user_passes_test(lambda user: user.is_superuser)
def add_package_s2i(request):
    if request.method == 'POST':
        creation_form = PackageS2IForm(request.POST)
        if creation_form.is_valid():
            package = creation_form.save()
            return redirect('edit_package_s2i', package.pk) 

    else:
        creation_form = PackageS2IForm()

    return render(request, 'packaging/add_package_s2i.html', {'creation_form': creation_form})



def products_view(request):
    return render(request, 'packaging/add_package_s2i.html', {'creation_form': creation_form})