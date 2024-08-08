from django.shortcuts import render, redirect
from django.contrib.auth.decorators import user_passes_test
from .models import *
from .forms import *
import os
from django_filters.views import FilterView
from .filters import ItemFilter


## Dashboards views

@user_passes_test(lambda user: user.is_superuser)
def production_dashboard(request):
    
    data = {
        'products' : Product.objects.all(),
        'categories': Product_Category.objects.all(),
        'items': Product_Item.objects.all(),
    }
    return render(request, 'production/dashboard.html',data)




## Management views

@user_passes_test(lambda user: user.is_superuser)
def products_management_view(request):
    return render(request, 'production/products_management_view.html', {'products': Product.objects.all()})


@user_passes_test(lambda user: user.is_superuser)
def categories_management_view(request):
    return render(request, 'production/categories_management_view.html', {'categories': Product_Category.objects.all()})


@user_passes_test(lambda user: user.is_superuser)
def items_management_view(request):
    return render(request, 'production/items_management_view.html', {'items': Product_Item.objects.all()})


class ItemListView(FilterView):
    model = Product_Item
    filterset_class = ItemFilter
    template_name = 'production/items_management_view.html'


##CRUD views




@user_passes_test(lambda user: user.is_superuser)
def edit_product(request, product_id):

    product = Product.objects.get(pk = product_id)

    if request.method == 'POST':

        edit_form = ProductForm(request.POST, request.FILES, instance=product)
        if edit_form.is_valid():
            product = edit_form.save()
            


    else:
        edit_form = ProductForm(instance=product)

    edit_form.product_id = product_id
    
    return render(request, 'production/edit_product.html', {'edit_form': edit_form, 'product':product})



@user_passes_test(lambda user: user.is_superuser)
def add_product(request):
    if request.method == 'POST':
        creation_form = ProductForm(request.POST, request.FILES)
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
        creation_form = ProductItemForm(request.POST, request.FILES)
        if creation_form.is_valid():
            product = creation_form.save()
            return redirect('edit_item', product.pk) 

    else:
        creation_form = ProductItemForm()


    creation_form.fields['product'].initial = product

    return render(request, 'production/add_item.html', {'creation_form': creation_form, 'product': product})





@user_passes_test(lambda user: user.is_superuser)
def edit_category(request, category_id):

    category = Product_Category.objects.get(pk = category_id)

    if request.method == 'POST':
        edit_form = CategoryForm(request.POST, request.FILES, instance=category)
        if edit_form.is_valid():
            category = edit_form.save()

    else:
        edit_form = CategoryForm(instance=category)


    
    return render(request, 'production/edit_category.html', {'edit_form': edit_form, 'category':category})



@user_passes_test(lambda user: user.is_superuser)
def add_category(request):
    if request.method == 'POST':
        creation_form = CategoryForm(request.POST, request.FILES)
        if creation_form.is_valid():
            category = creation_form.save()
            return redirect('edit_category', category.pk) 

    else:
        creation_form = CategoryForm()

    return render(request, 'production/add_category.html', {'creation_form': creation_form})


# Client views


def view_product(request, product_id):
    return render(request, 'production/view_product.html', {'product': Product.objects.get(pk = product_id)})



def view_item(request, item_id):
    return render(request, 'production/view_item.html', {'item': Product_Item.objects.get(pk = item_id)})

def view_categories(request):
    return render(request, 'production/view_categories.html', {'categories': Product_Category.objects.all()})



def view_category(request, category_id):
    return render(request, 'production/view_category.html', {'category': Product_Category.objects.get(pk = category_id)})

