from django.contrib import admin
from .models import *
from django.forms import CheckboxSelectMultiple
from django.contrib.auth.models import Group
from django.http import HttpResponse
from django.urls import path
from pyfcm import FCMNotification
from .serializers import *


admin.site.site_header = 'CricYorker'
admin.site.unregister(Group)

class InlineTeamPlayer(admin.TabularInline):
    model = TeamPlayer
    extra = 0

# class InlineAddPackageMatch(admin.TabularInline):
#     model = AddPackageMatch
#     field = ('package_manage','add_match','status','created_at','updated_at')

#     extra = 0
class InlineTeamCreatePost(admin.TabularInline):
    model = TeamCreatePost

    extra = 0

def make_activate_user(modeladmin,request,queryset):
    queryset.update(user_status='1')
make_activate_user.short_description = "Marks as Live user"

def make_inactivate_user(modeladmin,request,queryset):
    queryset.update(user_status='0')
make_inactivate_user.short_description = "Marks as Suspend user"

def send_notification(modeladmin,request,queryset):
    
    titlePush = queryset.values_list('title')
    desPush = queryset.values_list('description')
    # titlePush="hello"
    # desPush= "cricyorker"
    # return HttpResponse(titlePush)

     # users = models.NewEventNotification.objects.all().filter(is_notify=1)
    # serializer = NewEventNotificationSerializer(users, many=True)
    tokens = ['f8T97RkxtMg:APA91bEQ4rGn48Oo-vB5oODQy32V8MNrJPVUZjPEytNpp08ZfyMSTMIrXkrSGIHT0BW6cEXpKo9_NkmA0VoSt0Lnx8GWR_ez0w_cYpCw8foNjsTZkeiZWVaGGw7wSyK8HeCQ1lCrAJtb']
    # for user in serializer.data:
    #     tokens.append(user['user_token'])
    if tokens:

        push_service = FCMNotification(api_key='AAAAyLSRPqg:APA91bHnHmo2wN8ItP-PqQHvZNOligRl9IZcut_ikyU1DIGWpHFk7DLdWYWB5uQXBaOYyXKIx8KPh_h1LOEHxBaGZuMm6CTNNeKUAjYkMlq89G7d2wjSJseWGABemknG0oD6GIWTUVMJ')
        message_title = titlePush
        # message_body = data
        message_body = desPush

        result = push_service.notify_multiple_devices(
            registration_ids=tokens, message_title=message_title, message_body=message_body)

    return HttpResponse(result)

send_notification.short_description = "Send Notifications"


class UserAdmin(admin.ModelAdmin):
    list_display = ('id','user_name','user_phone','user_email','userType','user_status')
    list_display_links = ('user_name',)
    list_editable = ('user_status',)
    actions = [make_activate_user,make_inactivate_user]
    search_fields = ('id', 'user_name', 'user_email', )
    list_filter = ['created_at']
    list_per_page = 10
admin.site.register(User,UserAdmin)

# class UserProxyAdmin(admin.ModelAdmin):
#     list_display = ('id','user_name','user_phone','user_email')
#     list_display_links = ('user_name',)
# admin.site.register(UserProxy,UserProxyAdmin)

class PackageManageAdmin(admin.ModelAdmin):
    # inlines = [InlineAddPackageMatch]
    list_display = ('id','package_name','package_price','package_imageUpload','select_month','package_status','status')
    list_editable = ('package_status','status',)
    search_fields = ('id', 'package_name', 'package_price', )
    # list_filter = ['created_at']
    formfield_overrides = {
        models.ManyToManyField: {'widget': CheckboxSelectMultiple},
    }
admin.site.register(PackageManage,PackageManageAdmin)

class SeriesAdmin(admin.ModelAdmin):
    list_display = ('id','series_name','series_start_date','series_end_date','status')
    list_editable = ('status',)
    search_fields = ('id', 'package_name', 'package_price', )
    list_filter = ['created_at']
admin.site.register(Series,SeriesAdmin)

class TeamManageAdmin(admin.ModelAdmin):
    inlines = [InlineTeamPlayer]
    list_display = ('id','team_name','team_manage_imageUpload','short_name','status')
    list_editable = ('status',)
    search_fields = ('id', 'team_name', 'short_name', )
    list_filter = ['created_at']
admin.site.register(TeamManage,TeamManageAdmin)

class MatchManageAdmin(admin.ModelAdmin):
    list_display = ('id','team_1','team_2','short_name','match_start_date','status')
    list_editable = ('status',)
    search_fields = ('id', )
    list_filter = ['created_at']

    def team_1(self, instance):
        return instance.match_team_1.team_name
    
    def team_2(self, instance):
        return instance.match_team_2.team_name

    def short_name(self, instance):
        a= instance.match_team_1.short_name
        b= instance.match_team_2.short_name

        shrt_name= a + " vs " + b
        return shrt_name

admin.site.register(MatchManage,MatchManageAdmin)



# class MatchTypeAdmin(admin.ModelAdmin):
#     list_display = ('id','match_type','status')
#     list_editable = ('status',)
#     search_fields = ('id', )
#     list_filter = ['match_type','created_at']
# admin.site.register(MatchType,MatchTypeAdmin)

# class MatchFormatAdmin(admin.ModelAdmin):
#     list_display = ('id','match_format','status')
#     list_editable = ('status',)
#     search_fields = ('id', )
#     list_filter = ['match_format','created_at']
# admin.site.register(MatchFormat,MatchFormatAdmin)

# class LeagueSelectionAdmin(admin.ModelAdmin):
#     list_display = ('id','league_selection','status')
#     list_editable = ('status',)
#     search_fields = ('id', )
#     list_filter = ['league_selection','created_at']
# admin.site.register(LeagueSelection,LeagueSelectionAdmin)


# class AddPackageMatchAdmin(admin.ModelAdmin):
#     list_display = ('id','status')
#     list_editable = ('status',)
#     search_fields = ('id', )
#     list_filter = ['created_at']
# admin.site.register(AddPackageMatch,AddPackageMatchAdmin)

class PostManageAdmin(admin.ModelAdmin):
    inlines = [InlineTeamCreatePost]
    list_display = ('id','description','select_match','created_at','status')
    list_editable = ('status',)
    search_fields = ('id', )
    list_filter = ['created_at']

    def select_match(self, instance):
        return instance.MatchManage
admin.site.register(PostManage,PostManageAdmin)

class TransactionManageAdmin(admin.ModelAdmin):
    list_display = ('id','user_id','order_id','created_at','status')
    list_editable = ('status',)
    search_fields = ('id', )
    list_filter = ['created_at']
admin.site.register(TransactionManage,TransactionManageAdmin)

class AppVersionAdmin(admin.ModelAdmin):
    list_display = ('id','title','version','url','status')
    list_editable = ('status',)
    search_fields = ('id', )
    list_filter = ['created_at']
admin.site.register(AppVersion,AppVersionAdmin)


class demoUserAdmin(admin.ModelAdmin):
    list_display = ('id','demoUser','status')
    list_editable = ('status',)
    search_fields = ('id', )
    list_filter = ['created_at']

    def demoUser(self, instance):
        return instance.User

admin.site.register(demoUser,demoUserAdmin)



class firebaseNotificationAdmin(admin.ModelAdmin):
    list_display = ('id','title')
    actions = [send_notification]
admin.site.register(firebaseNotification,firebaseNotificationAdmin)



