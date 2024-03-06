from django.urls import path
from .views import *


urlpatterns =[
    path('index_view', index_view , name='index_view_url'),
    path('banner/', banner_view , name='banner_view_url'),
    path('recomendation/', house_view , name='recomendation_view_url'),
    path('villa/', villa_view , name='villa_view_url'),
    path('apartment/', apartment_view , name='apartment_view_url'),
    path('sell_house/', sell_house_view , name='sell_house_view_url'),
    path('presintation/', presintation_view , name='presintation_view_url'),
    path('detail/', detail_view , name='detail_view_url'),
    path('testimonial/', testimonial_view , name='testimonial_view_url'),
    path('info_view/', info_view , name='info_view_url'),
    path('about_us/', about_us , name='about_us_url'),
    path('contact_view/', contact_view , name='contact_view_url'),


    path('GetBanner/', GetBanner),
    path('GetRecomendation/', GetRecomendation),
    path('GetSell/', GetSell),
    path('GetDetail/' ,GetDetail),
    path('GetPresintaiton/' ,GetPresintaiton),
    path('GetTestimonial/',GetTestimonial),
    path('GetAbout_us/',GetAbout_us),



    path('create-banner/', create_banner, name="banner_create_url"),
    path('edit-banner/<int:pk>/', update_banner, name="banner_update_url"),
    path('delete-banner/<int:pk>/', delete_banner , name="banner_delete_url"),

    path('create-recomendation/', create_recomendation, name="create_recomendation_url"),
    path('update-recomendation/<int:pk>/', update_recomendation, name="update_recomendation_url"),
    path('delete_recomendation/<int:pk>/', delete_recomendation, name="delete_recomendation_url"),

    path('create-recomendation/', create_villa, name="create_villa_url"),
    path('update-recomendation/<int:pk>/', update_villa, name="update_villa_url"),
    path('delete_recomendation/<int:pk>/', delete_villa , name="delete_villa_url"),

    path('create-recomendation/', create_apartment, name="create_apartment_url"),
    path('update-recomendation/<int:pk>/', update_apartment, name="update_apartment_url"),
    path('delete_recomendation/<int:pk>/', delete_apartment, name="delete_apartment_url"),

    path('create-presintaiton/', create_presintaiton, name="create_presintaiton_url"),
    path('update-presintainton/<int:pk>/', update_presintainton, name="update_presintainton_url"),
    path('delete-presintainton/<int:pk>/', delete_presintainton, name="delete_presintainton_url"),

    path('create-detail/', create_detail, name="create_detail_url"),
    path('update-detail/<int:pk>/', update_detail, name="update_detail_url"),
    path('delete-detail/<int:pk>/', delete_detail, name="delete_detail_url"),

    path('create-testimonial/', create_testimonial, name="create_testimonial_url"),
    path('update-testimonial/<int:pk>/', update_testimonial, name="update_testimonial_url"),
    path('delete-testimonial/<int:pk>/', delete_testimonial, name="delete_testimonial_url"),

    path('create-about-us/', create_about_us, name="create_about_us_url"),
    path('update-about-us/<int:pk>/', update_about_us, name="update_about_us_url"),
    path('delete-about-us/<int:pk>/', delete_about_us, name="delete_about_us_url"),

    path('create-info/', create_info, name="create_info_url"),
    path('update-info/<int:pk>/', update_info, name="update_info_url"),
    path('delete-info/<int:pk>/', delete_info, name="delete_info_url"),

    path('create-contact/', create_contact, name="create_contact_url"),
    path('update-contact/<int:pk>/', update_contact, name="update_contact_url"),
    path('delete-contact/<int:pk>/', delete_contact, name="delete_contact_url"),

    path('create-sell-house/', create_sell_house, name="create_sell_house_url"),
    path('update-sell-house/<int:pk>/', update_sell_house, name="update_sell_house_url"),
    path('delete-sell-house/<int:pk>/', delete_sell_house, name="delete_sell_house_url"),

    path('month-view/', user_month_view, name="month_view_url"),
    path('recomendation-month-view/', recomendation_month_view, name="recomendation_month_view_url"),

    path('login_view/', login_view, name="login_view_url"),
    path('', register_view, name="register_view_url"),
]