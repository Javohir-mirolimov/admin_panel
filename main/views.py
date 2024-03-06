from django.shortcuts import render, redirect
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import *
from .serializers import *
from datetime import datetime, timedelta
from django.db.models import Count
from django.db.models.functions import ExtractDay, ExtractMonth
from django.contrib.auth import login, authenticate, logout

import calendar


""" Start Get"""
def index_view(request):


    return render(request, 'index.html')

def banner_view(request):
    context = {
        'banner': Banner.objects.all()
    }



    return render(request, 'banner.html', context)



def house_view(request):
    context = {
        'house': Recomendation.objects.all()
    }
    return render(request, 'house.html', context)

def villa_view(request):
    context = {
        'villa': Recomendation.objects.all()
    }
    return render(request, 'villa.html', context)

def apartment_view(request):
    context = {
        'apartment': Recomendation.objects.all()
    }
    return render(request, 'apartment.html', context)
def sell_house_view(request):
    context={
        'sell': Sell.objects.all()
    }


    return render(request, 'sell_house.html', context)

def presintation_view(request):
    context={
        'presintation': Presintaiton.objects.all()
    }


    return render(request, 'presintaiton.html', context)


def detail_view(request):
    context={
        'detail': Detail.objects.all()
    }
    return render(request, 'detail.html', context)

def testimonial_view(request):
    context={
        'testimonial': Testimonial.objects.all()
    }


    return render(request, 'testimonial.html', context)

def about_us(request):
    context={
        'about_us': About_us.objects.all()
    }


    return render(request, 'about_us.html', context)

def info_view(request):
    context={
        'info': Info.objects.all()
    }


    return render(request, 'info.html', context)

def contact_view(request):
    context={
        'contact': Contact.objects.all()
    }


    return render(request, 'contact.html', context)








@api_view(['GET'])
def GetBanner(request):
    banner = Banner.objects.all()
    ser = BannerSerializres(banner, many=True)
    return Response(ser.data)


@api_view(['GET'])
def GetRecomendation(request):
    recomendation = Recomendation.objects.all()
    ser = RecomendationSerializres(recomendation, many=True)
    return Response(ser.data)


@api_view(['GET'])
def GetSell(request):
    sell = Sell.objects.all()
    ser = SellSerializres(sell, many=True)
    return Response(ser.data)


@api_view(['GET'])
def GetDetail(request):
    detail = Detail.objects.all()
    ser = DetailSerializres(detail, many=True)
    return Response(ser.data)


@api_view(['GET'])
def GetPresintaiton(request):
    presintaition = Presintaiton.objects.all()
    ser = PresintaitonSerializres(presintaition, many=True)
    return Response(ser.data)


@api_view(['GET'])
def GetTestimonial(request):
    testimonial = Testimonial.objects.all()
    ser = TestimonialSerializres(hotel, many=True)
    return Response(ser.data)


@api_view(['GET'])
def GetAbout_us(request):
    about_us = About_us.objects.all()
    ser = About_usSerializres(about_us, many=True)
    return Response(ser.data)


""" End Get"""

"""" Start Crud"""


def create_banner(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        banner_img = request.FILES.get('banner_img')
        img_logo = request.FILES.get('img_logo')
        Banner.objects.create(
            title=title,
            description=description,
            banner_img=banner_img,
            img_logo=img_logo,
        )
    return redirect('banner_view_url')


def update_banner(request, pk):
    banner = Banner.objects.get(pk=pk)
    title = request.POST.get('title')
    description = request.POST.get('description')
    banner_img = request.FILES.get('banner_img')
    img_logo = request.POST.get('img_logo')
    banner.title = title
    banner.description = description
    if banner_img is not None:
        banner.banner_img = banner_img
    if img_logo is not None:
        banner.img_logo = img_logo
    banner.save()
    return redirect('banner_view_url')


def delete_banner(request, pk):
    banner = Banner.objects.get(pk=pk)
    banner.delete()
    return redirect('banner_view_url')



def create_recomendation(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        img = request.FILES.get('img')
        name = request.POST.get('name')
        price = request.POST.get('price')
        user_name = request.POST.get('user_name')
        address = request.POST.get('address')
        user_img = request.FILES.get('user_img')
        tag = request.POST.get('tag', 'default_tag')
        print(tag)
        type = request.POST.get('type', 'default_type' )
        Recomendation.objects.create(
        title=title,
        img=img,
        name= name,
        price=price,
        user_name=user_name,
        address=address,
        user_img=user_img,
        tag=tag,
        type=type,
        )
    return redirect('recomendation_view_url')


def update_recomendation(request, pk):
    recomendation = Recomendation.objects.get(pk=pk)
    title = request.POST.get('title')
    img = request.FILES.get('img')
    name = request.POST.get('name')
    price = request.POST.get('price')
    user_name = request.POST.get('user_name')
    address = request.POST.get('address')
    user_img = request.FILES.get('user_img')
    tag = request.POST.get('tag')
    type = request.POST.get('type')

    recomendation.title = title
    if img is not None:
        recomendation.img = img
    recomendation.name = name
    recomendation.price = price
    recomendation.user_name = user_name
    recomendation.address = address
    if user_img is not None:
        recomendation.user_img = img
    if tag is not None:
        recomendation.tag = tag
    if type is not None:
        recomendation.type =type
    recomendation.save()

    return redirect('recomendation_view_url')


def delete_recomendation(request, pk):
    recomendation = Recomendation.objects.get(pk=pk)
    recomendation.delete()
    return redirect('recomendation_view_url')

def create_villa(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        img = request.FILES.get('img')
        name = request.POST.get('name')
        price = request.POST.get('price')
        user_name = request.POST.get('user_name')
        address = request.POST.get('address')
        user_img = request.FILES.get('user_img')
        tag = request.POST.get('tag', 'default_tag')
        print(tag)
        type = request.POST.get('type', 'default_type' )
        Recomendation.objects.create(
        title=title,
        img=img,
        name= name,
        price=price,
        user_name=user_name,
        address=address,
        user_img=user_img,
        tag=tag,
        type=type,
        )
    return redirect('villa_view_url')


def update_villa(request, pk):
    recomendation = Recomendation.objects.get(pk=pk)
    title = request.POST.get('title')
    img = request.FILES.get('img')
    name = request.POST.get('name')
    price = request.POST.get('price')
    user_name = request.POST.get('user_name')
    address = request.POST.get('address')
    user_img = request.FILES.get('user_img')
    tag = request.POST.get('tag')
    type = request.POST.get('type')

    recomendation.title = title
    if img is not None:
        recomendation.img = img
    recomendation.name = name
    recomendation.price = price
    recomendation.user_name = user_name
    recomendation.address = address
    if user_img is not None:
        recomendation.user_img = img
    if tag is not None:
        recomendation.tag = tag
    if type is not None:
        recomendation.type =type
    recomendation.save()

    return redirect('villa_view_url')


def delete_villa(request, pk):
    recomendation = Recomendation.objects.get(pk=pk)
    recomendation.delete()
    return redirect('villa_view_url')


def create_apartment(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        img = request.FILES.get('img')
        name = request.POST.get('name')
        price = request.POST.get('price')
        user_name = request.POST.get('user_name')
        address = request.POST.get('address')
        user_img = request.FILES.get('user_img')
        tag = request.POST.get('tag', 'default_tag')
        print(tag)
        type = request.POST.get('type', 'default_type' )
        Recomendation.objects.create(
        title=title,
        img=img,
        name= name,
        price=price,
        user_name=user_name,
        address=address,
        user_img=user_img,
        tag=tag,
        type=type,
        )
    return redirect('villa_view_url')


def update_apartment(request, pk):
    recomendation = Recomendation.objects.get(pk=pk)
    title = request.POST.get('title')
    img = request.FILES.get('img')
    name = request.POST.get('name')
    price = request.POST.get('price')
    user_name = request.POST.get('user_name')
    address = request.POST.get('address')
    user_img = request.FILES.get('user_img')
    tag = request.POST.get('tag')
    type = request.POST.get('type')

    recomendation.title = title
    if img is not None:
        recomendation.img = img
    recomendation.name = name
    recomendation.price = price
    recomendation.user_name = user_name
    recomendation.address = address
    if user_img is not None:
        recomendation.user_img = img
    if tag is not None:
        recomendation.tag = tag
    if type is not None:
        recomendation.type =type
    recomendation.save()

    return redirect('villa_view_url')


def delete_apartment(request, pk):
    recomendation = Recomendation.objects.get(pk=pk)
    recomendation.delete()
    return redirect('villa_view_url')

def create_presintaiton(request):
    if request.method == "POST":
        img = request.FILES.get('img')
        Presintaiton.objects.create(
            img= img,
        )
        return redirect('presintation_view_url')


def update_presintainton(request, pk):
    presintation = Presintaiton.objects.get(pk=pk)
    img = request.FILES.get('img')

    if img is not None:
        presintation.img = img
    presintation.save()

    return redirect('presintation_view_url')


def delete_presintainton(request, pk):
    presintation = Presintaiton.objects.get(pk=pk)
    presintation.delete()
    return redirect('presintation_view_url')



def create_detail(request):
    if request.method == "POST":
        name = request.POST.get('name')
        quantity = request.POST.get('quantity')
        Detail.objects.create(
            name=name,
            quantity=quantity,
        )
        return redirect('detail_view_url')


def update_detail(request, pk):
    name = request.POST.get('name')
    quantity = request.POST.get('quantity')
    detail = Detail.objects.get(pk=pk)

    detail.name = name
    detail.quantity = quantity
    detail.save()
    return redirect('detail_view_url')

def delete_detail(request, pk):
    detail = Detail.objects.get(pk=pk)
    detail.delete()
    return redirect('detail_view_url')


def create_testimonial(request):
    if request.method == "POST":
        title = request.POST.get('title')
        img = request.FILES.get('img')
        user_title = request.POST.get('user_title')
        description = request.POST.get('description')
        user_img = request.FILES.get('user_img')
        user_job = request.POST.get('user_job')
        user_name = request.POST.get('user_name')
        reting = request.POST.get('reting')
        Testimonial.objects.create(
        title=title,
        img=img,
        user_title=user_title,
        description=description,
        user_img=user_img,
        user_job=user_job,
        user_name=user_name,
        reting=reting,
        )
    return redirect('testimonial_view_url')

def update_testimonial(request, pk):
    testimonial = Testimonial.objects.get(pk=pk)
    title = request.POST.get('title')
    img = request.FILES.get('img')
    user_title = request.POST.get('user_title')
    description = request.POST.get('description')
    user_img = request.FILES.get('user_img')
    user_job = request.POST.get('user_job')
    user_name = request.POST.get('user_name')
    reting = request.POST.get('reting')

    testimonial.title = title
    if img is not None:
        testimonial.img = img
    testimonial.user_title = user_title
    testimonial.description = description
    if user_img is not None:
        testimonial.user_img = user_img
    testimonial.user_job = user_job
    testimonial.user_name = user_name
    testimonial.reting = reting
    testimonial.save()
    return redirect('testimonial_view_url')


def delete_testimonial(request, pk):
    testimonial = Testimonial.objects.get(pk=pk)
    testimonial.delete()
    return redirect('testimonial_view_url')



def create_about_us(request):
    if request.method == "POST":
        title=request.POST.get('title')
        user_fullname=request.POST.get('user_fullname')
        img=request.FILES.get('img')
        description=request.POST.get('description')
        About_us.objects.create(
        title=title,
        user_fullname=user_fullname,
        img=img,
        description=description,
        )
    return redirect('about_us_url')


def update_about_us(request, pk):
    about_us  = About_us.objects.get(pk=pk)
    title = request.POST.get('title')
    user_fullname = request.POST.get('user_fullname')
    img = request.FILES.get('img')
    description = request.POST.get('description')


    about_us.title = title
    about_us.user_fullname =user_fullname
    if img is not None:
        about_us.img = img
    about_us.description =description
    about_us.save()
    return redirect('about_us_url')


def delete_about_us(request, pk):
    about_us = About_us.objects.get(pk=pk)
    about_us.delete()
    return redirect('about_us_url')







def create_info(request):
    if request.method == "POST":
        my_logo=request.FILES.get('my_logo')
        description=request.POST.get('description')
        facebook=request.POST.get('facebook')
        twitter=request.POST.get('twitter')
        instagram=request.POST.get('instagram')
        address=request.POST.get('address')
        phone_number=request.POST.get('phone_number')
        email=request.POST.get('email')
        Info.objects.create(
        my_logo=my_logo,
        description=description,
        facebook=facebook,
        twitter=twitter,
        instagram=instagram,
        address=address,
        phone_number=phone_number,
        email=email,
        )
    return redirect('info_view_url')

def update_info(request, pk):
    my_logo = request.FILES.get('my_logo')
    description = request.POST.get('description')
    facebook = request.POST.get('facebook')
    twitter = request.POST.get('twitter')
    instagram = request.POST.get('instagram')
    address = request.POST.get('address')
    phone_number = request.POST.get('phone_number')
    email = request.POST.get('email')


    info = Info.objects.get(pk=pk)

    if my_logo is not None:
        info.my_logo = my_logo
    info.description = description
    info.facebook = facebook
    info.twitter = twitter
    info.instagram = instagram
    info.address = address
    info.phone_number = phone_number
    info.email = email
    info.save()
    return redirect('info_view_url')


def delete_info(request, pk):
    info = Info.objects.get(pk=pk)
    info.delete()
    return redirect('info_view_url')




def create_contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        Contact.objects.create(
            name=name,
            email=email,
        )
    return redirect('contact_view_url')


def update_contact(request, pk):
    contact = Contact.objects.get(pk=pk)
    name = request.POST.get('name')
    email = request.POST.get('email')

    contact.name = name
    contact.email = email
    contact.save()
    return redirect('contact_view_url')


def delete_contact(request, pk):
    contact = Contact.objects.get(pk=pk)
    contact.delete()
    return redirect('contact_view_url')




def create_sell_house(request):
    if request.method == "POST":
        title=request.POST.get('title')
        description=request.POST.get('description')
        detail=request.POST.get('detail')
        user_img=request.FILES.get('user_img')
        user_name=request.POST.get('user_name')
        user_job=request.POST.get('user_job')
        presintation=request.POST.get('presintation')
        Sell.objects.create(
        title=title,
        description=description,
        detail=detail,
        user_img=user_img,
        user_name=user_name,
        user_job=user_job,
        presintation=presintation,
        )
    return redirect('sell_house_view_url')

def update_sell_house(request, pk):
    sell = Sell.objects.get(pk=kp)
    title = request.POST.get('title')
    description = request.POST.get('description')
    detail = request.POST.get('detail')
    user_img = request.FILES.get('user_img')
    user_name = request.POST.get('user_name')
    user_job = request.POST.get('user_job')
    presintation = request.POST.get('presintation')

    sell.title = title
    sell.description = description
    if detail is not None:
        sell.detail = detail
    if user_img is not None:
        sell.user_img = user_img
    sell.user_name = user_name
    sell.user_job = user_job
    if presintation is not None:
        sell.presintation = presintation
    sell.save()
    return redirect('sell_house_view_url')


def delete_sell_house(request, pk):
    sell = Sell.objects.get(pk=pk)
    sell.delete()
    return redirect('sell_house_view_url')






"""" End Crud"""



def home_view(request):
    all_register = Sell.objects.all().order_by('id').count()
    day = datetime.today() - timedelta(days=1)
    month = datetime.today() - timedelta(days=30)
    today = Sell.objects.filter(craeted__gte=day).count()
    months = Sell.objects.filter(craeted__gte=month).count()
    qs = Register.objects.filter(
        created__gte=month
    ).annotate(
        day=ExtractDay("created"),
        mon=ExtractMonth('created'),
    ).values(
        'day', 'mon'
    ).annotate(
        n=Count('pk')
    ).order_by('mon')
    mon_list = []
    for i in qs:
        i['mon'] = (calendar.month_abbr[i['mon']])
        if len(mon_list) >= 30:
            del mon_list[0]
            mon_list.append(i)
        else:
            mon_list.append(i)
    context = {
       "all_register":all_register,
       "today":today,
       "month":months,
        "qs": mon_list,
    }
    return render(request, 'index.html',context)


def user_month_view(request):
    all_register = User.objects.all().order_by('id').count()
    month = datetime.today() - timedelta(days=30)
    months = User.objects.filter(craeted__gte=month).count()
    context={
        'user_months': months
    }


def recomendation_month_view(request):
    all_register = Recomendation.objects.all().order_by('id').count()
    month = datetime.today() - timedelta(days=30)
    months = Recomendation.objects.filter(craeted__gte=month).count()
    context={
        'months': months
    }

def sell_month_view(request):
    all_register = Sell.objects.all().order_by('id').count()
    month = datetime.today() - timedelta(days=30)
    months = Sell.objects.filter(craeted__gte=month).count()
    context={
        'sell_months': months
    }


def register_view(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        User.objects.create_user(
            username = username,
            password = password,
        )
        return redirect("index_view_url")
    return render(request,'register.html')






def login_view(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        usr = authenticate(username=username, password=password)
        if usr is not None:
            login(request, usr)
        return redirect("index_view_url")
    return render(request,'login.html')






