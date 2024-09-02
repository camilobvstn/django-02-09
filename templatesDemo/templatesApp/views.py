from django.shortcuts import render

# Create your views here.

def renderTemplate(request):
    data={"nombre":"Camilo","apellido":"Mimiza"}
    return render(request,'templatesApp/pagina2.html',data)

