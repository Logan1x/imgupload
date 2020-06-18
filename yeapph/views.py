from django.shortcuts import render
from .models import User

# Create your views here.
def index(request):
    # p = users[len(users)-1].pic
    # print(p.url)
    return render(request,"index.html")


def uploadImage(request):
    print("request handling...")
    p  = request.FILES['image']
    q  = request.POST['texttitle']
    user = User(pic = p, titletext = q)
    user.save()
    users = User.objects.all()
    return render(request,"show.html", {'users':users})