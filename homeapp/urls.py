from django.urls import path

from homeapp import views, adminviews, companyviews, userviews

urlpatterns = [
path('',views.home,name='home'),
path('loginview',views.loginview,name='loginview'),
path('logout_view',views.logout_view,name='logout_view'),
path('admin_home',adminviews.admin_home,name='admin_home'),
path('company_register',views.company_register,name='company_register'),
path('user_register',views.user_register,name='user_register'),
path('company_home',companyviews.company_home,name='company_home'),
path('user_home',userviews.user_home,name='user_home'),


#     admin views
path('view_company',adminviews.view_company,name='view_company'),
path('view_users',adminviews.view_users,name='view_users'),
path('viewplan',adminviews.viewplan,name='viewplan'),
path('viewpayment',adminviews.viewpayment,name='viewpayment'),
path('viewcomplaint',adminviews.viewcomplaint,name='viewcomplaint'),
path('reply_complaint/<int:id>/',adminviews.reply_complaint,name='reply_complaint'),



#     company views
path('profile_view',companyviews.profile_view,name='profile_view'),
path('upload_plans',companyviews.upload_plans,name='upload_plans'),
path('view_plans',companyviews.view_plans,name='view_plans'),
path('view_planrequests',companyviews.view_planrequests,name='view_planrequests'),
path('replytorequest/<int:id>/',companyviews.replytorequest,name='replytorequest'),
path('chatwithuser',companyviews.chatwithuser,name='chatwithuser'),
path('reviews',companyviews.reviews,name='reviews'),
path('update_plans/<int:id>/',companyviews.update_plans,name='update_plans'),



#user views
path('userprofile',userviews.userprofile,name='userprofile'),
path('viewcompany',userviews.viewcompany,name='viewcompany'),
path('viewplans',userviews.viewplans,name='viewplans'),
path('requestplans',userviews.requestplans,name='requestplans'),
path('viewrequest',userviews.viewrequest,name='viewrequest'),
path('addcomplaint',userviews.addcomplaint,name='addcomplaint'),
path('complaintview',userviews.complaintview,name='complaintview'),
path('purchaseplans',userviews.purchaseplans,name='purchaseplans'),
path('viewreqreply/<int:id>/',userviews.viewreqreply,name='viewreqreply'),




]

