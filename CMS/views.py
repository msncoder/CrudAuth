from django.shortcuts import render,HttpResponse,redirect
from .models import *
from .forms import OrderForm,CustomerForm,ProductForm,TagsForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.urls import reverse
# Create your views here.


@login_required
def dashboard(request):
    order = Order.objects.all() # it retrive all order from database
    customer = Customer.objects.all()
    total_order = order.count()
    deliver = order.filter(status='Delivered').count()
    pending = order.filter(status='Pending').count()
    context = {
        'order':order,
        'customer':customer,
        'total_order':total_order,
        'deliver':deliver,
        'pending':pending
    }
    return render(request,"dashboard.html",context)



@login_required
def create_order(request):
    if request.method == 'POST':
        fm = OrderForm(request.POST)
        if fm.is_valid():
            fm.save()
            messages.success(request,"Order Created")
            # fm = OrderForm()
            # return render(request,'order_create.html',{'fm':fm})
            return redirect('/CMS/createorder/')
    else:
        fm = OrderForm()


    context = {
        'fm':fm
    }

    return render(request,'order_create.html',context)


@login_required
def update_order(request, id):
    if request.method == 'POST':
        order = Order.objects.get(pk=id)
        fm = OrderForm(request.POST, instance=order)
        if fm.is_valid():
            fm.save()
            messages.success(request, "Order Updated")
            return redirect(reverse('updateorder', args=[id]))
            # return redirect('customer_view')
    else:
       
        order = Order.objects.get(pk=id)
        fm = OrderForm(instance=order)
        customer_id = order.customer_id
        

    
    context = {'fm': fm,'customer_id':customer_id}
    return render(request, 'update_order.html', context)


@login_required
def delete_order(request,id):
    order = Order.objects.get(pk=id)
    if request.method == 'POST':
        order.delete()
        return redirect('/CMS/')
    context={
        'order':order 
    }
    return render(request,'order_delete.html',context)



@login_required
def customer_view(request,id):
    customers=Customer.objects.get(pk=id)
    all_orders = customers.order_set.all()
    order_count = all_orders.count()

    context = {
        'customers':customers,
        'order':all_orders,
        'order_count':order_count,
        'pk':id
    }

    return render(request,'customer.html',context)



@login_required
def create_customer(request):
    if request.method == 'POST':
        fm = CustomerForm(request.POST)
        if fm.is_valid():
            fm.save()
            messages.success(request,"Customer Created")
            # fm = CustomerForm()
            # return render(request,'create_customer.html',{'fm':fm})
            return redirect("/CMS/create_customer/")
  
    else:
        fm = CustomerForm()

    context = {
            'fm':fm
            }
    return render(request,'create_customer.html',context)

@login_required
def update_customer(request,id):
    if request.method == 'POST':
        cus = Customer.objects.get(pk=id)
        fm = CustomerForm(request.POST,instance=cus)
        if fm.is_valid():
            fm.save()
            messages.success(request,"Update Created")
            fm = CustomerForm()
            return render(request,'update_customer.html',{'fm':fm,"cus":cus})
    else:
        cus = Customer.objects.get(pk=id)
        fm = CustomerForm(instance=cus)
    context = {
            'fm':fm,
            'cus':cus
        }
    return render(request,'update_customer.html',context)



@login_required
def delete_customer(request,id):
    customer = Customer.objects.get(pk=id)
    if request.method == 'POST':
        customer.delete()
        return redirect('/CMS/')
    context={
        'customer':customer 
    }
    return render(request,'customer_delete.html',context)



@login_required
def create_product(request):
    item = Product.objects.all()
    if request.method == 'POST':
        fm = ProductForm(request.POST)
        if fm.is_valid():
            fm.save()
            messages.success(request, "Product Created")
            return redirect("/CMS/product/")
            # item = Product.objects.all()
            # fm = ProductForm()
            # context = {
            #     'fm': fm,
            #     'item': item
            # }
            # return render(request, 'product.html', context)
    else:
        # Define 'item' for the 'else' branch as well
        fm = ProductForm()

    context = {
        'fm': fm,
        'item': item
    }
    return render(request, 'product.html', context)


@login_required
def update_product(request,id):
    if request.method == 'POST':
        order = Product.objects.get(pk=id)
        fm = ProductForm(request.POST,instance=order)
        if fm.is_valid():
            fm.save()
            messages.success(request,"Product Updated")
            fm = ProductForm()
            return render(request,'update_product.html',{'fm':fm})
    else:
        order = Product.objects.get(pk=id)
        fm = ProductForm(instance=order)
    context = {
            'fm':fm
        }
    return render(request,'update_product.html',context)

@login_required
def delete_product(request,id):
    product = Product.objects.get(pk=id)
    if request.method == 'POST':
        product.delete()
        return redirect('/CMS/product/')
    context={
        'product':product 
    }
    return render(request,'product_delete.html',context)




@login_required
def create_tags(request):
    if request.method == 'POST':
        fm = TagsForm(request.POST)
        if fm.is_valid():
            fm.save()
            messages.success(request,"Tag Created")
            return redirect("/CMS/createtag/")
            # fm = TagsForm()
            # item = Tags.objects.all()
            # return render(request,'tags.html',{
            #     'fm':fm,
            #     'item':item
            #     })
  
    else:
         item = Tags.objects.all()
         fm = TagsForm()
    

    context = {
                'fm':fm,
                'item':item
                }
    return render(request,'tags.html',context)


@login_required
def update_tag(request,id):
    if request.method == 'POST':
        order = Tags.objects.get(pk=id)
        fm = TagsForm(request.POST,instance=order)
        if fm.is_valid():
            fm.save()
            messages.success(request,"Tag Updated")
            fm = TagsForm()
            return render(request,'update_tag.html',{'fm':fm})
    else:
        order = Tags.objects.get(pk=id)
        fm = TagsForm(instance=order)
    context = {
            'fm':fm
        }
    return render(request,'update_tag.html',context)




@login_required
def delete_tag(request,id):
    tag = Tags.objects.get(pk=id)
    if request.method == 'POST':
        tag.delete()
        return redirect('/CMS/createtag/')
    context={
        'tag':tag 
    }
    return render(request,'delete_tag.html',context)


