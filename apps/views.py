from django.shortcuts import render
from apps .models import *


# Create your views here.

def index(req):
    return render(req,'index.html')

def projects(req):
    data = {"product": Product.objects.all(), "category": Category.objects.all()}
    return render(req, 'projects.html', data)


def about(req):
    return render(req, 'about.html')


def project(req, pro_id):
    return render(req, 'project.html', {
        'products': Product.objects.get(pk=pro_id),
        'category': Category.objects.all()
    })


def categoryList(req, cat_id):
    data = {
            "product": Product.objects.filter(category=cat_id),
            "category": Category.objects.all()
            }
    return render(req, 'projects.html', data)
