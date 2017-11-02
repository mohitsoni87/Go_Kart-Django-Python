from django.shortcuts import render
def homepage(request):
    return render(request, "GO_KART/homepage.html")