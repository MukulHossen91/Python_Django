from django.shortcuts import render
from django.http import HttpResponseRedirect
from product.forms import RecentProduct
from .models import laptop
from django.http import HttpResponse


# Create your views here.

def cake(request):
    return render(request, 'product/product.html')

def send(request):
    return render(request, 'product/submit.html')


def details(request):
    if request.method == 'POST':
        frm = RecentProduct(request.POST)
        if frm.is_valid():
            mL = frm.cleaned_data['mobile']
            re_ml = frm.cleaned_data['re_mobile']
            lp = frm.cleaned_data['laptop']
            email = frm.cleaned_data['email']
            pas = frm.cleaned_data['password']
            ab = frm.cleaned_data['about']
            text = frm.cleaned_data['textarea']
            check = frm.cleaned_data['checkbox']
            ram = frm.cleaned_data['ram']
            ssd = frm.cleaned_data['ssd']
            you =  frm.cleaned_data['youtube_chanel']
            buy = laptop(mobile = mL, re_mobile = re_ml, laptop = lp, email = email, password = pas, about = ab, textarea = text, checkbox = check, ram = ram, ssd = ssd, youtube_chanel = you)
            buy.save()

            return HttpResponseRedirect('/pdc/successfully')
        

    else:
        frm = RecentProduct(auto_id=True, label_suffix=' - ')
        print("GET Statement")
    
    return render(request, 'product/recent.html', {'form' : frm})



def midd(request):
    print("firs Middleware")
    return HttpResponse("This is 1st middleware")



