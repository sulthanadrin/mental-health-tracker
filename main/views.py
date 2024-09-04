from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'npm' : '2306201306',
        'name': 'Sulthan Adrin Pasha Siregar',
        'class': 'PBP C'
    }

    return render(request, "main.html", context)
