from django.shortcuts import render,redirect
from django.contrib import messages 
from .models import Contact
# Create your views here.
def Home(request):
    return render(request,'home.html')

def About(request):
    return render(request,'about.html')


def Contact_Form(request):
    if request.method == 'POST':
        # here is for information; 
        # full_name is name="full_name" of the template html code. but Name is variables for storing the data .
        Name = request.POST['full_name'] 
        Number = request.POST['phone_number']
        Mail = request.POST['email']
        Course = request.POST['course']
        Image = request.FILES['image']
        Message = request.POST['message']
        # aba yespachi chai ->contact = Contact(models ko variable = mathi ko variables for storing data .)
        contact = Contact(name=Name,phone_number=Number,email=Mail,course=Course,image=Image,message=Message)
        contact.save()
        messages.success(request,'your form is submitted successfully !!! ')
        return redirect('contact_info')
    else:
        return render(request,'contact.html')


def Contact_info(request):
    data = Contact.objects.all()
    context={
        'Posted_Data':data
    }
    return render(request,'contact_info.html',context)


def Delete_data(request,pk):
    data = Contact.objects.get(id=pk)
    data.delete()
    return redirect('contact_info')


def Edit_Data(request, pk):
    if request.method == 'POST' and request.FILES:
        data = Contact.objects.get(id=pk)
        data.name = request.POST['full_name']
        data.email = request.POST['email']
        data.course = request.POST['course']
        data.image = request.FILES['image']
        data.phone_number = request.POST['phone_number']
        data.message = request.POST['message']
        data.save()
        return redirect('contact_info')
    else:
        data = Contact.objects.get(id=pk)
        context = {
            'info': data
        }
        return render(request, 'edit_info.html', context)


