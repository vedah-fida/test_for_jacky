from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import NameForm
# Create your views here.

def get_name(request):
    #if this is a POST we need to process the data form
    if request_method == "POST":
        #create a form instance and populate it with datafrom the request
        form = NameForm(request.POST)#binding data to a form
        if form.is_valid():
            #process the data in form.cleaned_data as required

            #redirect to a new URL:
            return HttpResponseRedirect('/thanks/')
        #if a GET(or any other method) we'll create a blank form
    else:
        form = NameForm()
        #name.html is the name of the html file
    return render(request,'name.html') , {'forms': form}


