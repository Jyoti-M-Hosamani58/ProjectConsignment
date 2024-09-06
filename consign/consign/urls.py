"""
URL configuration for consign project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from consign_app import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),

    path('',views.index,name='index'),

    path('index_menu', views.index_menu, name='index_menu'),
    path('user_menu', views.user_menu, name='user_menu'),

    path('nav', views.nav, name='nav'),
    path('feedback', views.feedback, name='feedback'),
    path('view_feedback', views.view_feedback, name='view_feedback'),

    path('userlogin', views.userlogin, name='userlogin'),
    path('admin_home', views.admin_home, name='admin_home'),
    path('user_home', views.user_home, name='user_home'),
    path('branch_home',views.branch_home,name='branch_home'),
    path('staff_home',views.staff_home,name='staff_home'),

    path('addConsignment/', views.addConsignment, name='addConsignment'),
    path('printConsignment/<int:track_id>/', views.printConsignment, name='printConsignment'),
    path('branchprintConsignment/<int:track_id>/',views.branchprintConsignment,name='branchprintConsignment'),
    path('view_consignment', views.view_consignment, name='view_consignment'),
    path('user_view_consignment', views.user_view_consignment, name='user_view_consignment'),

    path('consignment_edit/<int:pk>', views.consignment_edit, name='consignment_edit'),
    path('consignment_delete/<int:pk>', views.consignment_delete, name='consignment_delete'),
    path('invoiceConsignment/<int:pk>', views.invoiceConsignment, name='invoiceConsignment'),

    path('addTrack', views.addTrack, name='addTrack'),
    path('search_results', views.search_results, name='search_results'),

    path('user_search_results', views.user_search_results, name='user_search_results'),

    path('track_delete/<int:pk>', views.track_delete, name='track_delete'),

    path('branch', views.branch, name='branch'),
    path('view_branch', views.view_branch, name='view_branch'),

    path('edit_branch/<int:pk>', views.edit_branch, name='edit_branch'),
    path('branch_delete/<int:pk>', views.branch_delete, name='branch_delete'),

    path('driver', views.driver, name='driver'),
    path('view_driver', views.view_driver, name='view_driver'),

    path('driver_edit/<int:pk>', views.driver_edit, name='driver_edit'),
    path('driver_delete/<int:pk>', views.driver_delete, name='driver_delete'),

    path('vehicle', views.vehicle, name='vehicle'),
    path('view_vehicle', views.view_vehicle, name='view_vehicle'),

    path('vehicle_edit/<int:pk>', views.vehicle_edit, name='vehicle_edit'),
    path('vehicle_delete/<int:pk>', views.vehicle_delete, name='vehicle_delete'),

    path('branchConsignment',views.branchConsignment,name='branchConsignment'),
    path('branchprintConsignment/<int:track_id>/', views.branchprintConsignment, name='branchprintConsignment'),
    path('branchviewConsignment',views.branchviewConsignment,name='branchviewConsignment'),

    path('branchconsignment_edit/<int:pk>', views.branchconsignment_edit, name='branchconsignment_edit'),
    path('branchconsignment_delete/<int:pk>', views.branchconsignment_delete, name='branchconsignment_delete'),
    path('branchinvoiceConsignment/<int:track_id>/', views.branchinvoiceConsignment, name='branchinvoiceConsignment'),

    path('branchaddTrack', views.branchaddTrack, name='branchaddTrack'),
    path('branchsearch_results', views.branchsearch_results, name='branchsearch_results'),

    path('branchtrack_delete/<int:pk>', views.branchtrack_delete, name='branchtrack_delete'),
    path('branchMaster', views.branchMaster, name='branchMaster'),

    path('addTripSheet',views.addTripSheet,name='addTripSheet'),
    path('addTripSheetList',views.addTripSheetList,name='addTripSheetList'),
    path('saveTripSheet',views.saveTripSheet,name='saveTripSheet'),

    path('get_vehicle_numbers/', views.get_vehicle_numbers, name='get_vehicle_numbers'),
    path('get_driver_name/', views.get_driver_name, name='get_driver_name'),
    path('get_branch/', views.get_branch, name='get_branch'),
    path('get_destination/', views.get_destination, name='get_destination'),

    path('tripSheet',views.tripSheet,name='tripSheet'),
    path('tripSheetList',views.tripSheetList,name='tripSheetList'),
    path('delete-trip-sheet-data/', views.delete_trip_sheet_data, name='delete_trip_sheet_data'),

    path('editTripSheetList',views.editTripSheetList,name='editTripSheetList'),
    path('update/', views.update_view, name='update_view'),
    path('printTripSheetList/<str:vehical_no>/<str:date>/',views.printTripSheetList,name='printTripSheetList'),

    path('viewTripSheetList',views.viewTripSheetList,name='viewTripSheetList'),

    path('adminTripSheet',views.adminTripSheet,name='adminTripSheet'),
    path('adminPrintTripSheetList/<str:vehical_no>/<str:date>/<str:branch>/',views.adminPrintTripSheetList,name='adminPrintTripSheetList'),


    path('api/save-location/', views.save_location, name='save_location'),

    path('staff', views.staff, name='staff'),
    path('view_staff', views.view_staff, name='view_staff'),
    path('edit_staff/<int:pk>', views.edit_staff, name='edit_staff'),
    path('delete_staff/<int:pk>', views.delete_staff, name='delete_staff'),

    path('get_consignor_name/', views.get_consignor_name, name='get_consignor_name'),
    path('get_consignee_name/', views.get_consignee_name, name='get_consignee_name'),

    path('get_sender_details/', views.get_sender_details, name='get_sender_details'),
    path('get_rec_details/', views.get_rec_details, name='get_rec_details'),

    path('staff_home',views.staff_home,name='staff_home'),
    path('staff_nav',views.staff_nav,name='staff_nav'),

    path('staffAddTripSheet',views.staffAddTripSheet,name='staffAddTripSheet'),
    path('staffAddTripSheetList',views.staffAddTripSheetList,name='staffAddTripSheetList'),

    path('staffSaveTripSheet',views.staffSaveTripSheet,name='staffSaveTripSheet'),
    path('staffTripSheet',views.staffTripSheet,name='staffTripSheet'),

    path('staffTripSheetList',views.staffTripSheetList,name='staffTripSheetList'),
    path('staffViewTripSheetList',views.staffViewTripSheetList,name='staffViewTripSheetList'),
    path('staffprintTripSheetList/<str:vehical_no>/<str:date>/',views.staffprintTripSheetList,name='staffprintTripSheetList'),
    path('get_staff',views.get_staff,name='get_staff'),

    path('branchExpenses',views.branchExpenses,name='branchExpenses'),
    path('save-branch-expenses/', views.savebranchExpenses, name='savebranchExpenses'),
    path('branchViewExpenses',views.branchViewExpenses,name='branchViewExpenses'),

    path('adminExpenses',views.adminExpenses,name='adminExpenses'),
    path('save-admin-expenses/', views.saveadminExpenses, name='saveadminExpenses'),
    path('adminViewExpenses',views.adminViewExpenses,name='adminViewExpenses'),

    path('payment_history/', views.payment_history, name='payment_history'),
    path('fetch-details/', views.fetch_details, name='fetch_details'),
    path('fetch-consignments/', views.fetch_consignments, name='fetch_consignments'),

    path('credit/', views.credit, name='credit'),

    path('fetch_balance/', views.fetch_balance, name='fetch_balance'),
    path('submit_credit/', views.submit_credit, name='submit_credit'),

    path('credit_print/', views.credit_print, name='credit_print'),
    path('fetch_account_details/', views.fetch_account_details, name='fetch_account_details'),

    path('branchPaymenyHistory',views.branchPaymenyHistory,name='branchPaymenyHistory'),
    path('branchfetch_details',views.branchfetch_details,name='branchfetch_details'),
    path('branchcredit/', views.branchcredit, name='branchcredit'),
    path('branchsubmit_credit',views.branchsubmit_credit,name='branchsubmit_credit'),
    path('branchfetch_balance',views.branchfetch_balance,name='branchfetch_balance'),
    path('branchcredit_print',views.branchcredit_print,name='branchcredit_print'),
    path('branchfetch_account_details',views.branchfetch_account_details,name='branchfetch_account_details'),

    path('staffcredit_print',views.staffcredit_print,name='staffcredit_print'),

    path('branchConsignorView',views.branchConsignorView,name='branchConsignorView'),
    path('branchConsigneeView',views.branchConsigneeView,name='branchConsigneeView'),

    path('adminConsignorView',views.adminConsignorView,name='adminConsignorView'),
    path('adminConsigneeView',views.adminConsigneeView,name='adminConsigneeView'),

    path('adminstaff_view',views.adminstaff_view,name='adminstaff_view'),
    path('adminView_Consignment',views.adminView_Consignment,name='adminView_Consignment'),
    path('admininvoiceConsignment/<int:track_id>/',views.admininvoiceConsignment,name='admininvoiceConsignment'),

    path('staffinvoiceConsignment/<int:track_id>/',views.staffinvoiceConsignment,name='staffinvoiceConsignment'),

    path('consignment_list',views.consignment_list,name='consignment_list'),
    path('consignment/<str:sender_name>/', views.consignment_detail, name='consignment_detail'),
    path('disel_report',views.disel_report,name='disel_report'),
    path('account_report',views.account_report,name='account_report'),
    path('get_account_details',views.get_account_details,name='get_account_details'),
    path('unloaded_LR_report',views.unloaded_LR_report,name='unloaded_LR_report'),
    path('tripSheetPrem_report',views.tripSheetPrem_report,name='tripSheetPrem_report'),
    path('property_report',views.property_report,name='property_report'),
]
if settings.DEBUG:
     urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

