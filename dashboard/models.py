from django.db import models
from django import forms
from djrichtextfield.models import RichTextField
import uuid

STATUS_CHOICES = [
    ('0', 'Suspended'),
    ('1', 'Live'),
]
PACKAGE_STATUS_CHOICES = [
    ('1', 'Trending'),
    ('2', 'Big Winning'),
    ('0', 'None'),
]

STATUS = [
    ('1', 'ACTIVE'),
    ('0', 'INACIVE'),
]

USERTYPE = [
    ('DEMO', 'DEMO'),
    ('REAL', 'REAL USER'),
]

TEAM = [
    ('1', '1 TEAM'),
    ('2', '2 TEAMS'),
    ('3', '3 TEAMS'),
    ('4', '4 TEAMS'),
    ('5', '5 TEAMS'),
    ('6', '6 TEAMS'),
    ('7', '7 TEAMS'),
    ('8', '8 TEAMS'),
    ('9', '9 TEAMS'),
    ('10', '10 TEAMS'),
    ('11', '11 TEAMS'),
]


INT_CHOICES= [tuple([x,x]) for x in range(1,12)]
DAYS_CHOICES= [tuple([x,x]) for x in range(1,31)]



class User(models.Model):
    user_name = models.CharField(max_length=100, null=True, blank=True)
    user_email = models.EmailField(max_length=100, null=True, blank=True,unique=True)
    user_phone = models.CharField(max_length=50,null=True, blank=True,unique=True)
    userType = models.CharField(max_length=15, choices=USERTYPE, default='REAL')
    isVerified = models.BooleanField(blank=False, default=False)
    counter = models.IntegerField(default=0, blank=False)
    user_social_id = models.CharField(max_length=100, null=True, blank=True)
    user_status = models.CharField(max_length=1, choices=STATUS_CHOICES, default='1')
    user_image = models.CharField(max_length=300, null=True, blank=True)
    user_imageUpload = models.ImageField('upload/images/',null=True, blank=True)
    login_type = models.CharField(max_length=80, null=True, blank=True)
    fcm_id = models.CharField(max_length=300, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        ids = self.id
        if self.user_name is None:
             return str(ids)
        else:
            return self.user_name + "-" + str(ids)

# class UserProxy(User):

#     class Meta:
#         proxy = True

# class Visitor(models.Model):
#     pupil = models.OneToOneField(User, on_delete=models.CASCADE,related_name='session')
#     session_key = models.CharField(null=False, max_length=40)

class PackageManage(models.Model):
    class Meta:
        verbose_name_plural = "Package"
        
    package_name = models.CharField(max_length=60)
    package_price = models.CharField(max_length=60)
    discount_price = models.IntegerField(verbose_name = "Discount Percentage")
    # package_description = models.TextField(max_length=60, null=True, blank=True)
    description = RichTextField(null=True, blank=True)
    select_month= models.IntegerField(choices=INT_CHOICES)
    select_day = models.IntegerField(choices=DAYS_CHOICES, null=True, blank=True)
    package_imageUpload = models.ImageField('upload/images/',null=True, blank=True)
    package_status = models.CharField(max_length=1, choices=PACKAGE_STATUS_CHOICES, default='0')
    status = models.CharField(max_length=1, choices=STATUS, default='1')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.package_name

class Series(models.Model):
    class Meta:
        verbose_name_plural = "Series"

    series_name = models.CharField(max_length=60, null=True, blank=True)
    series_start_date = models.DateField(null=True, blank=True)
    series_end_date = models.DateField(null=True, blank=True)
    status = models.CharField(max_length=1, choices=STATUS, default='1')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.series_name

class TeamManage(models.Model):
    class Meta:
        verbose_name_plural = "Team Manage"

    team_name = models.CharField(max_length=60, null=True, blank=True)
    short_name = models.CharField(max_length=60, null=True, blank=True)
    team_manage_imageUpload = models.ImageField('upload/images/',null=True, blank=True)
    status = models.CharField(max_length=1, choices=STATUS, default='1')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.team_name

class MatchType(models.Model):
    match_type = models.CharField(max_length=60, null=True, blank=True)
    status = models.CharField(max_length=1, choices=STATUS, default='1')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.match_type

class MatchFormat(models.Model):
    match_format = models.CharField(max_length=60, null=True, blank=True)
    status = models.CharField(max_length=1, choices=STATUS, default='1')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.match_format

class LeagueSelection(models.Model):
    league_selection = models.CharField(max_length=60, null=True, blank=True)
    status = models.CharField(max_length=1, choices=STATUS, default='1')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.league_selection

class MatchManage(models.Model):
    class Meta:
        verbose_name_plural = "Match Manage"

    series_name = models.ForeignKey(Series, on_delete=models.CASCADE,related_name='seriesname')
    match_type = models.ForeignKey(MatchType, on_delete=models.CASCADE,related_name='matchtype')
    match_format = models.ForeignKey(MatchFormat, on_delete=models.CASCADE,related_name='matchformat')
    league_selection = models.ForeignKey(LeagueSelection, on_delete=models.CASCADE,related_name='leagueselection')
    total_teams = models.CharField(max_length=60,choices=TEAM)
    match_team_1 = models.ForeignKey(TeamManage, on_delete=models.CASCADE,related_name='teammanage')
    match_team_2 = models.ForeignKey(TeamManage, on_delete=models.CASCADE,related_name='teammanages')
    match_start_date = models.DateField()
    match_time = models.TimeField()
    status = models.CharField(max_length=1, choices=STATUS, default='1')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        self.series_name.empty_label = "Select"
        ids = self.id
        t1 = self.match_team_1.team_name
        t2 = self.match_team_2.team_name
        teams = t1 + " vs " + t2 + "-" + str(ids) 
        return teams 
        
    # def __str__(self):
    #     return self.series_name

    # def __init__(self,*args,**kwargs):
    #     self.fields['series_name'].empty_label = "Select"

class TeamPlayer(models.Model):
    class Meta:
        verbose_name_plural = "Players"

    player_name = models.CharField(max_length=60, null=True, blank=True)
    player_imageUpload = models.ImageField('upload/images/',null=True, blank=True)
    player_team = models.ForeignKey(TeamManage, on_delete=models.CASCADE,related_name='playerteam')
    status = models.CharField(max_length=1, choices=STATUS, default='1')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.player_name


    
class AddPackageMatch(models.Model):
    class Meta:
        verbose_name_plural = "Add Match"

    package_manage=models.ForeignKey(PackageManage, on_delete=models.CASCADE,related_name='packagmanage')
    add_match=models.ManyToManyField(MatchManage,blank=True)
    status = models.CharField(max_length=1, choices=STATUS, default='1')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class PostManage(models.Model):
    class Meta:
        verbose_name_plural = "Post Manage"

    select_package=models.ManyToManyField(PackageManage)
    series_name = models.ForeignKey(Series, on_delete=models.CASCADE,related_name='seriesnames')
    select_match=models.ForeignKey(MatchManage, on_delete=models.CASCADE,related_name='addmatchs')
    description = RichTextField(null=True, blank=True)
    status = models.CharField(max_length=1, choices=STATUS, default='1')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        ids = self.select_match.id
        t1 = self.select_match.match_team_1.team_name
        t2 = self.select_match.match_team_2.team_name
        teams = t1 + " vs " + t2 + "-" + str(ids) 
        return teams 



class TransactionManage(models.Model):
    class Meta:
        verbose_name_plural = "Order Manage"

    user_id=models.ForeignKey(User, on_delete=models.CASCADE,related_name='username')
    order_id= models.UUIDField(default=uuid.uuid4, unique=True, db_index=True, editable=False)
    package_id=models.ForeignKey(PackageManage, on_delete=models.CASCADE,related_name='packagename')
    active_data=models.DateField(null=True, blank=True)
    transactionID=models.CharField(max_length=100, null=True, blank=True, editable=False)
    status = models.CharField(max_length=1, choices=STATUS, default='1')
    paid_status = models.CharField(max_length=1, choices=STATUS, default='0', editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        orderId=self.order_id
        return str(orderId)
    

class TeamCreatePost(models.Model):
    class Meta:
        verbose_name_plural = "Team Create"

    post_id=models.ForeignKey(PostManage, on_delete=models.CASCADE,related_name='postmanage')
    team_imageUpload = models.ImageField('upload/images/',default='pexels-ave-calvar-martinez-4852353_ZZZxG7O.jpg')
    status = models.CharField(max_length=1, choices=STATUS, default='1')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class AppVersion(models.Model):
    title=models.CharField(max_length=100, null=True, blank=True)
    description=models.TextField(null=True, blank=True)
    version=models.CharField(max_length=100, null=True, blank=True)
    url=models.URLField(max_length=100, null=True, blank=True)
    status = models.CharField(max_length=1, choices=STATUS, default='1')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.title

class firebaseNotification(models.Model):
    title=models.CharField(max_length=100, null=True, blank=True)
    description=models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.title

class demoUser(models.Model):
    demoUser=models.ForeignKey(User, on_delete=models.CASCADE,related_name='demousername')
    select_match_demo=models.ManyToManyField(PostManage)
    status = models.CharField(max_length=1, choices=STATUS, default='1')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.demoUser.user_name



    


