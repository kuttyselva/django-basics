from django.shortcuts import render

# Create your views here.
def index(request):
    contextdict={'text':'helloworld','Number':123}
    return render(request,'basicapp/index.html',context=contextdict)
def other(request):
    return render(request,'basicapp/other.html')
def relative(request):
    return render(request,'basicapp/relative.html')
def base(request):
    return render(request,'basicapp/base.html')
