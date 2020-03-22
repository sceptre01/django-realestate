from django.shortcuts import render, redirect
from .models import Contact
from django.contrib import messages

# Create your views here.
def contact(request):
    if request.method == 'POST':
        property_id = request.POST['property_id']
        property = request.POST['property']
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']
        user_id = request.POST['user_id']
        agent_email = request.POST['agent_email']

        if request.user.is_authenticated:
            user_id = request.user.property_id
            has_contacted = Contact.objects.all().filter(property_id=property_id, user_id=user_id)
            if has_contacted:
                messages.error(request, 'You have aleardy made an inquiry for this property')
                return redirect('/properties/'+property_id)


        contact = Contact(property=property, property_id=property_id, name=name, email=email, phone=phone, message=message, user_id=user_id)
    
        contact.save()

        messages.success(request, 'Your request has been submitted, an agent will get back to you soon')

        return redirect('/properties/'+property_id)