from django.urls import include, path
from rest_framework import routers 
from django.conf import settings 
from django.conf.urls.static import static
from . import views
app_name= 'dashboard'

urlpatterns = [
    path('sendOtp',views.sendOtp,name="sendOTP"),
    path('socialLogin',views.socialLogin,name="socialLogin"),
    path('addPhoneNumber',views.addPhoneNumber,name="addPhoneNumber"),
    path('viewMatch',views.viewMatch,name="viewMatch"),
    path('viewPackage',views.viewPackage,name="viewPackage"),
    path('postPackageData',views.postPackageData,name="postPackageData"),
    # path('postData',views.postData,name="postData"),
    path('transactionApi',views.transactionApi,name="transactionApi"),
    path('postDataApi',views.postDataApi,name="postDataApi"),
    path('sendMail',views.sendMail,name="sendMail"),
    path('updateProfile',views.updateProfile,name="updateProfile"),
    path('demoUserApi',views.demoUserApi,name="demoUserApi"),
    path('checkDemo',views.checkDemo,name="checkDemo"),
    path('sendNotification',views.sendNotification,name="sendNotification"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)