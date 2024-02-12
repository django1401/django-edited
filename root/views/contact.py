from django.shortcuts import render , redirect
from ..forms import NewsLetterForm, ContactUsForm
from django.contrib import messages

def contact(request):
    if request.method =='GET':

        return render(request,"root/contact.html")
    elif request.method == 'POST' and len(request.POST) == 2 :
        form = NewsLetterForm(request.POST)
        if form.is_valid():
            form.save()  
            messages.add_message(request,messages.SUCCESS,'your email submited')
            return redirect('root:contact')   
        else :
            messages.add_message(request,messages.ERROR,'Invalid email address')
            return redirect('root:contact')
        
    elif request.method == 'POST' and len(request.POST) > 2 :
        form = ContactUsForm(request.POST)
        if form.is_valid():
            form.save()  
            messages.add_message(request,messages.SUCCESS,'we received your message and call with you you as soon')
            return redirect('root:contact')   
        else :
            messages.add_message(request,messages.ERROR,'Invalid data')
            return redirect('root:contact')