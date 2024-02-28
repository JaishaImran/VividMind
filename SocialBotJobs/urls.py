from django.urls import path
from .views import AutomationTask, add_automation_profiles, add_device, add_proxy, add_server, add_server_via_excel_sheet, batch, insta_module_page, log, available_devices, profile, add_device_via_excel_sheet, SMSPVA, AntiCap, SignupView, add_profile_via_excel_sheet, available_proxies, available_server, index2, login_view, logout_view, tiktok_module_page
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('', login_view, name='login_view'),
    path('log', log, name='log'),
    path('batch', batch, name='batch'),
    path('index2', index2, name='index2'),
    path('SMSPVA', SMSPVA, name='SMSPVA'),
    path('add_proxy', add_proxy, name='add_proxy'),
    path('add_device', add_device, name='add_device'),
    path('add_server', add_server, name='add_server'),
    path('Anti-Captcha', AntiCap, name='AntiCap'),
    path('add_automation_profiles', add_automation_profiles, name='add_automation_profiles'),
    path('available_proxies', available_proxies, name='available_proxies'),    
    path('available_server', available_server, name='available_server'),
    path('AutomationTask', AutomationTask, name='AutomationTask'),
    path('add_device_via_excel_sheet', add_device_via_excel_sheet, name='add_device_via_excel_sheet'),
    path('add_server_via_excel_sheet', add_server_via_excel_sheet, name='add_server_via_excel_sheet'),
    path('available_devices', available_devices, name='available_devices'),
    path('profile', profile, name='profile'),
    path('login', login_view, name='login'),
    path('logout', logout_view, name='logout'),
    path('register', SignupView.as_view(), name='signup'),
    path('tiktok_module_page', tiktok_module_page, name='tiktok_module_page'),
    path('insta_module_page', insta_module_page, name='insta_module_page'),
    path('add_profile_via_excel_sheet', add_profile_via_excel_sheet, name='add_profile_via_excel_sheet'),
]