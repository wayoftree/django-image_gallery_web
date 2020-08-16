from django.shortcuts import render
from .models import *
# Create your views here.
def main(request):
    cats = Category.objects.all()
    images = Image.objects.all() 
    act_cat = None
    data = {'image' : images, 'cats' : cats, 'act_cat' : act_cat}
    return render(request,'main.html', data)
    

def cats_by_image(request,cid):
    cats = Category.objects.all()
    cat = Category.objects.get(pk=cid)
    images = Image.objects.filter(cat=cat)
    data = {'image' : images, 'cats' : cats}
    return render(request,'main.html', data)

def search(request):
    cats = Category.objects.all()
    image = Image.objects.all()
    query = request.GET.get("q")
    if query is not None:
        images = image.filter(title__icontains=query)
    data = {'image' : images, 'cats' : cats}
    return render(request,'main.html', data)    