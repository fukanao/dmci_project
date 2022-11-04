from django.urls import path
from . import views

app_name = 'dmci_app'
urlpatterns = [
    path('', views.portal, name='portal'),
    path('main_form/', views.main_form, name='main_form'),
    path('compo_form/', views.compo_form, name='compo_form'),
    path('compo_list/', views.compo_list_data, name='compo_list_data'),
    path('confirm/', views.confirm_before_write_db, name='confirm_write_db'),
    path('list_all_data/', views.list_all_data, name='list_all_data'),
]
