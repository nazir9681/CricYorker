from rest_framework import serializers
from .models import *

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class SeriesSerializer(serializers.ModelSerializer):
    series_id = serializers.IntegerField(source='id')
    class Meta:
        model = Series
        fields=['series_id','series_name','series_start_date','series_end_date','status','created_at','updated_at']

class TeamManageSerializer(serializers.ModelSerializer):
    team_id = serializers.IntegerField(source='id')
    class Meta:
        model = TeamManage
        fields=['team_id','team_name','short_name','team_manage_imageUpload','status','created_at','updated_at']

class MatchManageSerializer(serializers.ModelSerializer):
    match_id = serializers.IntegerField(source='id')
    class Meta:
        model = MatchManage
        fields=['match_id','series_name','match_team_1','match_team_2','match_start_date','match_time','match_type','match_format','total_teams','league_selection','status','created_at','updated_at']

class MatchTypeSerializer(serializers.ModelSerializer):
    match_type_id = serializers.IntegerField(source='id')
    class Meta:
        model = MatchType
        fields=['match_type_id','match_type','status','created_at','updated_at']

class MatchFormatSerializer(serializers.ModelSerializer):
    match_format_id = serializers.IntegerField(source='id')
    class Meta:
        model = MatchFormat
        fields=['match_format_id','match_format','status','created_at','updated_at']

class LeagueSelectionSerializer(serializers.ModelSerializer):
    league_selection_id = serializers.IntegerField(source='id')
    class Meta:
        model = LeagueSelection
        fields=['league_selection_id','league_selection','status','created_at','updated_at']

class PackageManageSerializer(serializers.ModelSerializer):
    package_id = serializers.IntegerField(source='id')
    class Meta:
        model = PackageManage
        fields=['package_id','package_name','package_price','discount_price','description','select_month','select_day','package_imageUpload','package_status','status','created_at','updated_at']
        # fields= '__all__'

class AddPackageMatchSerializer(serializers.ModelSerializer):
    AddPackageMatch_id = serializers.IntegerField(source='id')
    class Meta:
        model = AddPackageMatch
        fields=['AddPackageMatch_id','package_manage','add_match','status','created_at','updated_at']

class PostManageSerializer(serializers.ModelSerializer):
    PostManage_id = serializers.IntegerField(source='id')
    class Meta:
        model = PostManage
        fields=['PostManage_id','select_package','series_name','select_match','description','status','created_at','updated_at']

class TransactionManageSerializer(serializers.ModelSerializer):
    # order_id = serializers.IntegerField(source='id')
    class Meta:
        model = TransactionManage
        #fields=['order_id','user_name','transactionID','status','created_at','updated_at']
        fields= '__all__'    

class TeamCreatePostSerializer(serializers.ModelSerializer):
    TeamCreate_id = serializers.IntegerField(source='id')
    class Meta:
        model = TeamCreatePost
        fields=['TeamCreate_id','post_id','team_imageUpload','status','created_at','updated_at']

class AppVersionSerializer(serializers.ModelSerializer):
    AppVersion_id = serializers.IntegerField(source='id')
    class Meta:
        model = AppVersion
        fields=['AppVersion_id','title','description','version','url','status','created_at','updated_at']

class demoUserSerializer(serializers.ModelSerializer):
    Demo_User_id = serializers.IntegerField(source='id')
    class Meta:
        model = demoUser
        fields= ['Demo_User_id','demoUser','select_match_demo','status','created_at','updated_at']

class firebaseNotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = firebaseNotification
        fields= '__all__' 



        