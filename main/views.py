from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'npm' : '2306256324',
        'name': 'Ferdinand Bonfilio Simamora',
        'class': 'KKI'
    }

    return render(request, "main.html", context)