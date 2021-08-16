from django.shortcuts import render

# Create your views here.
def samba(request):
    return render(request,'samba.html',context={'name':'samba','age':23})

def siva(request):
    return render(request,'siva.html',context={'name':siva,'age':24})
 

