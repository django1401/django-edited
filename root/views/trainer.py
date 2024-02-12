from django.shortcuts import render , redirect
from courses.models import Trainer
from ..forms import NewsLetterForm
from django.contrib import messages


def trainer(request):
    if request.method =='GET':
        trainer = Trainer.objects.filter(status=True)
        context = {
            'trainer':trainer,
        }
        return render(request,"root/trainers.html",context=context)
    elif request.method == 'POST':
        form = NewsLetterForm(request.POST)
        if form.is_valid():
            form.save()  
            messages.add_message(request,messages.SUCCESS,'your email submited')
            return redirect('root:trainer')   
        else :
            messages.add_message(request,messages.ERROR,'Invalid email address')
            return redirect('root:trainer')