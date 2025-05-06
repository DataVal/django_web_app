from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from .forms import ReservationForm
# Create your views here.

# Isso é uma fucntion view 
def heeloo(request):
    return HttpResponse("Helooooooooo")

# Isso é uma class based view
class helotwo(View):
    def get(self, request):
        return HttpResponse("outro hello")
    
def home(request):
    form = ReservationForm()

    if request.method == "POST":
        form = ReservationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("Sucess")
        
    return render(request, "index.html", {"form": form})