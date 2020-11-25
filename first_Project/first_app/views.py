from django.shortcuts import render
from django.http import HttpResponse
from first_app.models import Topic,Webpage,AccessRecord
from first_app import forms
# Create your views here.


def index(request):
    webpages_list = AccessRecord.objects.order_by('date')
    date_dict={'access_records':webpages_list}
    # my_dict = {'insert_me':"Hello i am from views.py !"}
    return render(request,'first_app/index.html',context=date_dict)
def form_name_view(request):
    form = forms.Formname()
    if request.method == 'POST':
        form = forms.Formname(request.POST)

        if form.is_valid():
            print("VALIDATION SUCCEED")
            print("NAME: "+form.cleaned_data['name'])
            print("Email: "+form.cleaned_data['email'])
            print("text: "+form.cleaned_data['text'])

    return render(request,'first_app/forms.html',{'form':form})
