from django.shortcuts import render,redirect
from .models import Category,Photo
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
def gallery(request):
    category= request.GET.get('category')
    if category==None:
        photo=Photo.objects.all()
    else:
        photo=Photo.objects.filter(category__Name=category)    

    categories= Category.objects.all()
    context={'categories':categories,'photos':photo}
    return render(request,'gallery.html',context)

def view_photo(request,pk):
    photo=Photo.objects.get(id=pk)
    return render(request,'photo.html',{'photo':photo})

def add(request):
    categories= Category.objects.all()
    if request.method=='POST':
        data=request.POST
        image = request.FILES.get('image')


        if data['category']!='none':
            category=Category.objects.get(id=data['category'])
        elif data['category_new']!='':
            category,created=Category.objects.get_or_create(Name=data['category_new'])   
        else:
            category= None


        photo=Photo.objects.create(
            category=category,
            description=data['description'],
            image=image,
        )         
         
        return redirect('gallery') 
    context={'categories':categories}
    return render(request,'add.html',context)

