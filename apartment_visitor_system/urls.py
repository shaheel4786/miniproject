
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('base/', views.BASE, name='base'),
    path('', views.LOGIN, name='login'),
    path('doLogin', views.doLogin, name='doLogin'),
    path('doLogout', views.doLogout, name='logout'),

    #profile path
    path('Profile', views.PROFILE, name='profile'),
    path('Profile/update', views.PROFILE_UPDATE, name='profile_update'),

    
    path('Index', views.INDEX, name='index'),
    path('Visitor', views.ADD_VISITOR, name='add_visitor'),
    path('ManageVisitor', views.MANAGE_VISITOR, name='manage_visitor'),
    path('UpdateVisitor/<str:id>', views.UPDATE_VISITOR, name='update_visitor'),

    path('Visitorpass', views.CREATE_VISITOR_PASS, name='create_visitor_pass'),
    path('ManageVisitorPass', views.MANAGE_VISITOR_PASS, name='manage_visitor_pass'),
    path('DeleteVisitorPass/<str:id>', views.DELETE_VISITOR_PASS, name='delete_visitor_pass'),
    path('ViewVisitorPass/<str:id>', views.VIEW_VISITOR_PASS, name='view_visitor_pass'),
    path('SearchPass', views.Search_Pass, name='search_pass'),
    path('BetweenDateReportPass', views.Between_Date_Report_Pass, name='between_date_report_pass'),
    
    path('UpdateVisitorRemark/Update', views.UPDATE_VISITOR_REMARK, name='update_visitor_remark'),
    path('DeleteVisitor/<str:id>', views.DELETE_VISITOR, name='delete_visitor'),
    path('BetweenDateReport', views.Between_Date_Report, name='between_date_report'),
    path('Search', views.Search, name='search'),
    path('Password', views.CHANGE_PASSWORD, name='change_password'),
   



]+static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
