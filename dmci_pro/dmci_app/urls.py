from django.urls import path
from . import views

app_name = 'dmci_app'
urlpatterns = [
    path('', views.portal, name='portal'),
    path('compo_form/', views.compo_form, name='compo_form'),
    path('compo_list/', views.compo_list_data, name='compo_list_data'),
]
