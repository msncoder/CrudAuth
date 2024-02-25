from django.shortcuts import render,HttpResponse,redirect
from .models import *
from .forms import OrderForm,CustomerForm,ProductForm,TagsForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.urls import reverse
# Create your views here.


@login_required # this decorator only allow this function for authenticated user 
def dashboard(request):
    order = Order.objects.all() # it retrive all order from database
    customer = Customer.objects.all() # it retrive all order from fatabase
    total_order = order.count() # it count how many order in Order table 
    deliver = order.filter(status='Delivered').count() # it count how many Delivered in Order table 
    pending = order.filter(status='Pending').count() # it count how many pending in Order table 
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
        fm = OrderForm(request.POST) # here's OrderForm get the value from frontend
        if fm.is_valid(): # here's the valid check which is come from frontend
            fm.save() # here's is save
            messages.success(request,"Order Created")
            # fm = OrderForm()
            # return render(request,'order_create.html',{'fm':fm})
            return redirect('/CMS/createorder/')
    else:
        fm = OrderForm() # if request is get it give only form


    context = {
        'fm':fm
    }

    return render(request,'order_create.html',context)


@login_required
def update_order(request, id): 
    if request.method == 'POST':
        order = Order.objects.get(pk=id) # it check it which is come from front end it is in database or not
        fm = OrderForm(request.POST, instance=order) # its take instance as order
        if fm.is_valid(): # it check instance is valid 
            fm.save() # then its ave
            messages.success(request, "Order Updated")
            return redirect(reverse('updateorder', args=[id])) # reverse argument take url name
            # return redirect('customer_view')
    else:
       
        order = Order.objects.get(pk=id) #it check it which is come from front end it is in database or not
        fm = OrderForm(instance=order) # it parse the instance into order form
        customer_id = order.customer_id # it collect id of customer from one to many relationship to the order table
        

    
    context = {'fm': fm,'customer_id':customer_id}
    return render(request, 'update_order.html', context)


@login_required
def delete_order(request,id): 
    order = Order.objects.get(pk=id) ##it check it which is come from front end it is in database or not
    if request.method == 'POST': 
        order.delete() # it delete the particular order which id comes in id parameter
        return redirect('/CMS/')
    context={
        'order':order 
    }
    return render(request,'order_delete.html',context)



@login_required
def customer_view(request,id):
    customers=Customer.objects.get(pk=id) # it get id from url and give particular customer of this id 
    all_orders = customers.order_set.all() # it gives all order of particular user
    order_count = all_orders.count() # it count all the order count of particular customer

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
        fm = CustomerForm(request.POST) # if form is fill
        if fm.is_valid(): # check form is valid
            fm.save() # form is save
            messages.success(request,"Customer Created")
            # fm = CustomerForm()
            # return render(request,'create_customer.html',{'fm':fm})
            return redirect("/CMS/create_customer/")
  
    else:
        fm = CustomerForm() # if request is get it give the customer form

    context = {
            'fm':fm
            }
    return render(request,'create_customer.html',context)

@login_required
def update_customer(request,id):
    if request.method == 'POST':
        cus = Customer.objects.get(pk=id) #it check it which is come from front end it is in database or not
        fm = CustomerForm(request.POST,instance=cus) # its take instance as cus
        if fm.is_valid(): # here it check it is valid or not
            fm.save() # here it save
            messages.success(request,"Update Created")
            fm = CustomerForm()
            return render(request,'update_customer.html',{'fm':fm,"cus":cus})
    else:
        cus = Customer.objects.get(pk=id) # here's match the id which is come in url to customer table
        fm = CustomerForm(instance=cus) # it pass the particular customer into form 
    context = {
            'fm':fm,
            'cus':cus
        }
    return render(request,'update_customer.html',context)



@login_required
def delete_customer(request,id):
    customer = Customer.objects.get(pk=id) #here's match the id to Customer table which is come from url 
    if request.method == 'POST': 
        customer.delete() # it delete the particular customer
        return redirect('/CMS/')
    context={
        'customer':customer 
    }
    return render(request,'customer_delete.html',context)



@login_required
def create_product(request):
    item = Product.objects.all() # it retrives all the product item from product table
    if request.method == 'POST': 
        fm = ProductForm(request.POST) # if request is post which is comes in product form
        if fm.is_valid():# heres check form is valid
            fm.save() # here save the particular form
            messages.success(request, "Product Created") # gives this message in /CMS/product. path
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
        fm = ProductForm() # if request is get it render ProductForm 

    context = {
        'fm': fm,
        'item': item
    }
    return render(request, 'product.html', context)


@login_required
def update_product(request,id): # it the id from url
    if request.method == 'POST':
        order = Product.objects.get(pk=id) # it match the id in Product table to item 
        fm = ProductForm(request.POST,instance=order) # it take the data of particular id as instance into ProductForm as Post request
        if fm.is_valid(): # it check productform isvalid
            fm.save() # it save
            messages.success(request,"Product Updated")
            fm = ProductForm()
            return render(request,'update_product.html',{'fm':fm})
    else:
        order = Product.objects.get(pk=id) # it match the id in Product table to item 
        fm = ProductForm(instance=order) # it give the data of particular id as instance into ProductForm
    context = {
            'fm':fm
        }
    return render(request,'update_product.html',context)

@login_required
def delete_product(request,id):
    product = Product.objects.get(pk=id) # it match the id in Product table to item 
    if request.method == 'POST':
        product.delete() # it delete the particular product
        return redirect('/CMS/product/')
    context={
        'product':product 
    }
    return render(request,'product_delete.html',context)




@login_required
def create_tags(request):
    if request.method == 'POST':
        fm = TagsForm(request.POST) # here it take the data into tagsform
        if fm.is_valid(): # here it check data isvalid
            fm.save() # here it save this
            messages.success(request,"Tag Created")
            return redirect("/CMS/createtag/")
            # fm = TagsForm()
            # item = Tags.objects.all()
            # return render(request,'tags.html',{
            #     'fm':fm,
            #     'item':item
            #     })
  
    else:
         item = Tags.objects.all() # it retrives all the tags item from tag table
         fm = TagsForm() # here it give the form into fm
    

    context = {
                'fm':fm,
                'item':item
                }
    return render(request,'tags.html',context)


@login_required
def update_tag(request,id):
    if request.method == 'POST':
        order = Tags.objects.get(pk=id) #it match the id to the tag object
        fm = TagsForm(request.POST,instance=order) # it take the data of particular id as instance into TagForm as Post request
        if fm.is_valid(): # here's check form is valid
            fm.save() # form is save
            messages.success(request,"Tag Updated")
            fm = TagsForm() 
            return render(request,'update_tag.html',{'fm':fm})
    else:
        order = Tags.objects.get(pk=id) # it match the id in Product table to item
        fm = TagsForm(instance=order)  # it give the data of particular id as instance into ProductForm
    context = {
            'fm':fm
        }
    return render(request,'update_tag.html',context)





@login_required
def delete_tag(request,id):
    tag = Tags.objects.get(pk=id) #it match the id to the tag object
    if request.method == 'POST': 
        tag.delete() # particular tag is delete here
        return redirect('/CMS/createtag/')
    context={
        'tag':tag 
    }
    return render(request,'delete_tag.html',context)


