from django.shortcuts import render, redirect
from django.contrib.auth.decorators import user_passes_test
from .models import *
from .forms import *
import os

## Dashboards views

@user_passes_test(lambda user: user.is_superuser)
def production_dashboard(request):
    
    return render(request, 'production/dashboard.html')



## Management views

@user_passes_test(lambda user: user.is_superuser)
def products_management_view(request):
    return render(request, 'production/products_management_view.html', {'products': Product.objects.all()})


@user_passes_test(lambda user: user.is_superuser)
def categories_management_view(request):
    return render(request, 'production/categories_management_view.html', {'categories': Product_Category.objects.all()})


##CRUD views


@user_passes_test(lambda user: user.is_superuser)
def edit_product(request, product_id):

    product = Product.objects.get(pk = product_id)

    if request.method == 'POST':

        edit_form = ProductForm(instance=product, data= request.POST)
        if edit_form.is_valid():
            product = edit_form.save()



    else:
        edit_form = ProductForm(instance=product)

    edit_form.product_id = product_id
    
    return render(request, 'production/edit_product.html', {'edit_form': edit_form})



@user_passes_test(lambda user: user.is_superuser)
def add_product(request):
    if request.method == 'POST':
        creation_form = ProductForm(request.POST)
        if creation_form.is_valid():
            product = creation_form.save()
            return redirect('edit_product', product.pk) 

    else:
        creation_form = ProductForm()

    return render(request, 'production/add_product.html', {'creation_form': creation_form})



@user_passes_test(lambda user: user.is_superuser)
def edit_item(request, item_id):
    
    item = Product_Item.objects.get(pk = item_id)
    edit_form = ProductItemForm(instance=item)
    image_form = ProductItemImageForm()
    image_form.fields['item'].initial = item

    if request.method == 'POST':
        if request.POST.get('post_type') == 'save':
            edit_form = ProductItemForm(instance=item, data= request.POST)
            if edit_form.is_valid():
                item = edit_form.save()
        
        elif request.POST.get('post_type') == 'set_as_sold':
            item.set_as_sold(10)

        elif request.POST.get('post_type') == 'set_as_preduced':
            item.set_as_preduced()

        elif request.POST.get('post_type') == 'delete_image':
            item.delete_image(request.POST.get('image_id'))

        elif request.POST.get('post_type') == 'add_image':
            image_form = ProductItemImageForm(request.POST, request.FILES)
            
            
            if image_form.is_valid():
                image_form.save()
            
            print(image_form.errors)
            
            image_form = ProductItemImageForm()
            image_form.fields['item'].initial = item



            

   
    return render(request, 'production/edit_item.html', {'edit_form': edit_form, 'item':item, "image_form": image_form})



@user_passes_test(lambda user: user.is_superuser)
def add_item(request, product_id):
    product = Product.objects.get(pk=product_id)

    if request.method == 'POST':
        creation_form = ProductItemForm(request.POST)
        if creation_form.is_valid():
            product = creation_form.save()
            return redirect('edit_item', product.pk) 

    else:
        creation_form = ProductItemForm()


    creation_form.fields['product'].initial = product

    return render(request, 'production/add_item.html', {'creation_form': creation_form})





@user_passes_test(lambda user: user.is_superuser)
def edit_category(request, category_id):

    category = Product_Category.objects.get(pk = category_id)

    if request.method == 'POST':
        edit_form = CategoryForm(instance=category, data= request.POST)
        if edit_form.is_valid():
            category = edit_form.save()

    else:
        edit_form = CategoryForm(instance=category)


    
    return render(request, 'production/edit_category.html', {'edit_form': edit_form})



@user_passes_test(lambda user: user.is_superuser)
def add_category(request):
    if request.method == 'POST':
        creation_form = CategoryForm(request.POST)
        if creation_form.is_valid():
            category = creation_form.save()
            return redirect('edit_category', category.pk) 

    else:
        creation_form = CategoryForm()

    return render(request, 'production/add_category.html', {'creation_form': creation_form})
