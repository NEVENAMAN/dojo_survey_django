from django.shortcuts import render

def index(request):
    
    
    return render(request,'form.html')

def result(request):
    if request.method == "POST":
        email  = request.POST['email']
        password= request.POST['password']
        address1 = request.POST['address1']
        address2 = request.POST['address2']
        city = request.POST['city']
        state= request.POST['state']
        zip = request.POST['zip']
    context = {
        'email_from_farm' : email,
        'password_from_farm' : password,
        'address1_from_farm' : address1,
        'address2_from_farm' : address2,
        'city_from_farm' :city,
        'state_from_farm' : state,
        'zip_from_farm' : zip,
    }
    print(context)
    return render(request,'result.html',context)
