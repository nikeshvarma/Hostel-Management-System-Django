from django.shortcuts import render
from datetime import datetime
from .models import HostelImages
from django.contrib.auth.decorators import login_required


# Create your views here.

def home(request):
    date_time = datetime.now()
    images = HostelImages.objects.all()
    return render(request, 'home/Home.html', {'datetime': date_time, 'images': images})


def base(request):
    return render(request, 'home/Home.html')


@login_required
def userhome(request):
    args = {'user': request.user}
    return render(request, 'user/User_Homepage.html', args)


def services(request):
    return render(request, 'home/service_page.html')
