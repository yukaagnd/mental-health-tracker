
from django.shortcuts import render
def show_main(request):
    context = {
        'npm' : '2306165704',
        'name': 'Gnade Yuka',
        'class': 'PBP B'
    }

    return render(request, "main.html", context)