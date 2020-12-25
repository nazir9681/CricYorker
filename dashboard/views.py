from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets
from rest_framework.views import Response
from .serializers import *
from .models import *
from rest_framework.decorators import api_view
import random
import string
import requests
from django.db import connection
from datetime import date
from datetime import timedelta
import time
from django.conf import settings 
from django.core.mail import send_mail 
from pyfcm import FCMNotification
import datetime


@api_view(['POST'])
def checkDemo(request):
    phone=request.POST['user_phone']
    if request.POST['user_phone']:

        checkData=User.objects.filter(user_phone=phone)

        if len(checkData)==0:
            return Response({"status":"Success","demo":"false"})

        else:
            check=User.objects.get(user_phone=phone)
            data=UserSerializer(check).data

            if(data['userType']=='DEMO'):
                return Response({"status":"Success","demo":"true","data":data})
            else:
                return Response({"status":"Success","demo":"false"})

    else:
        return Response({"status":"failed","msg":"Invalid Request"})

@api_view(['POST'])
def sendOtp(request):
    phone=request.POST['user_phone']
    if request.POST['user_phone']:
        phone=request.POST['user_phone']
        key = random.randint(999,9999)
        msg= str(key) + " is your CricYorker OTP. OTP is confidential. For security reasons, DO NOT share this OTP with anyone."
        print(key)
        if key:
            link = f'http://zapsms.co.in/vendorsms/pushsms.aspx?user=dpandit&password=sandeep1&msisdn={phone}&sid=WADRBE&msg={msg}&fl=0&gwid=2'
            requests.get(link)
            return Response({
                'status' : 'Success',
                'detail' : 'OTP sent successfully.',
                'user' : 'true',
                'OTP' : key
                })
        else:
            return Response({
                'status' : False,
                'detail' : 'Sending OTP error.'
                })
    else:
        return Response({"status":"failed","msg":"Invalid Request"})


@api_view(['POST'])
def socialLogin(request):
    App = AppVersion.objects.get(status = '1')
    appVersion=AppVersionSerializer(App).data

    if request.POST['user_email']:
        user_email=request.POST['user_email']
        checkemail=User.objects.filter(user_email=user_email)
        if len(checkemail)==0:
            serializer = UserSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()

                subject = "welcome to Cricyorker"
                message = "Welcome to CricYorker.com, India's biggest fantasy cricket prediction platform CricYorker launched cricyorker prime on fantasy sports user's demand. If you are tired of using many predictor, try with cricyorker prime and get best winning teams for various fantasy cricket app like Dream11. "
                email_from = settings.EMAIL_HOST_USER 
                recipient_list = [user_email, ] 
                data=send_mail( subject, message, email_from, recipient_list ) 
                return Response({"data":data})
            else:
                return Response({"Error":"Invalid details"})
            return Response({"status":"Success","msg":"Login successfully","user":"true","version":appVersion['version']+" V","package":"false","data":serializer.data})
        else:
            check=User.objects.get(user_email=user_email)
            data=UserSerializer(check).data
            if data['user_status'] == "0":
                return Response({"status":"User is Suspended"})
            else:
                checkPackage = TransactionManage.objects.filter(user_id = data['id'],paid_status='0')
                if not data['user_phone']:
                    if len(checkPackage)==0:
                        return Response({"status":"Success","msg":"Login successfully","user":"true","version":appVersion['version']+" V","package":"false","data":data})
                    else:
                        return Response({"status":"Success","msg":"Login successfully","user":"true","version":appVersion['version']+" V","package":"true","data":data})
                else:    
                    if len(checkPackage)==0:
                        return Response({"status":"Success","msg":"Login successfully","user":"false","version":appVersion['version']+" V","package":"false","data":data})
                    else:
                        return Response({"status":"Success","msg":"Login successfully","user":"false","version":appVersion['version']+" V","package":"true","data":data})
    else:
        return Response({"status":"failed","msg":"Invalid Request"})

@api_view(['POST','PUT'])
def addPhoneNumber(request):
    loginType = request.POST['login_type']

    App = AppVersion.objects.get(status = '1')
    appVersion=AppVersionSerializer(App).data

    if loginType=="phone":
        user_phone=request.POST['user_phone']
        userPhone=User.objects.filter(user_phone=user_phone)
        if len(userPhone)==0:
            serializer = UserSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
            
            else:
                return Response({"status":"failed","msg":"invalid Request"})
            return Response({"status":"Success","msg":"Login successfully","user":"true","version":appVersion['version']+" V","package":"false","data":serializer.data})
        else:
            check=User.objects.get(user_phone=user_phone)
            data=UserSerializer(check).data

            # if(data['userType']=='DEMO'):
                #return Response({"status":"Success","msg":"Login successfully","demo":"true","user":"false","package":"false","version":appVersion['version']+" V","data":data})
                # return demoUserApi(data['id'])
                # return Response(data['id'])
            # else:
            checkPackage = TransactionManage.objects.filter(user_id = data['id'],paid_status='0')
            if len(checkPackage)==0:
                return Response({"status":"Success","msg":"Login successfully","user":"false","package":"false","version":appVersion['version']+" V","data":data})
            else:
                return Response({"status":"Success","msg":"Login successfully","user":"false","package":"true","version":appVersion['version']+" V","data":data})
    else:
        if request.POST['user_id'] and request.POST['user_phone']:
            user_phone=request.POST['user_phone']
            userPhone=User.objects.filter(user_phone=user_phone)
            if len(userPhone)==0:
                user_id = request.POST['user_id']
                check = User.objects.get(id= user_id)
                serializer = UserSerializer(check, data=request.data)
                if serializer.is_valid():
                    serializer.save()
                else:
                    return Response({"status":"Failure","msg":"Login Failed"})
                checkPackage = TransactionManage.objects.filter(user_id = user_id,paid_status='0')
                if len(checkPackage)==0:
                    return Response({"status":"Success","msg":"Login successfully","user":"true","package":"false","version":appVersion['version']+" V","data":serializer.data})
                else:
                    return Response({"status":"Success","msg":"Login successfully","user":"true","package":"true","version":appVersion['version']+" V","data":serializer.data})
            else:
                check=User.objects.get(user_phone=user_phone)
                data=UserSerializer(check).data
                checkPackage = TransactionManage.objects.filter(user_id = data['id'],paid_status='0')
                if len(checkPackage)==0:
                    return Response({"status":"Success","msg":"Login successfully","user":"false","package":"false","version":appVersion['version']+" V","data":data})
                else:
                    return Response({"status":"Success","msg":"Login successfully","user":"false","package":"true","version":appVersion['version']+" V","data":data})
        else:
            return Response({"status":"failed","msg":"invalid Request"})


@api_view(['GET'])
def viewMatch(request):
    match = MatchManage.objects.filter(status = '1')
    matchManage=MatchManageSerializer(match,many=True).data
    

    for seriesData in matchManage:
        seriesName = Series.objects.get(id = seriesData['series_name'])
        seriesData['sname'] = SeriesSerializer(seriesName).data
        seriesData['series_name'] = seriesData['sname']['series_name']
        del(seriesData['sname'])
        

        matchTeam1 = TeamManage.objects.get(id = seriesData['match_team_1'])
        seriesData['match_team_1'] = TeamManageSerializer(matchTeam1).data
        del(seriesData['match_team_1']['status'])
        del(seriesData['match_team_1']['created_at'])
        del(seriesData['match_team_1']['updated_at'])

        matchTeam2 = TeamManage.objects.get(id = seriesData['match_team_2'])
        seriesData['match_team_2'] = TeamManageSerializer(matchTeam2).data
        del(seriesData['match_team_2']['status'])
        del(seriesData['match_team_2']['created_at'])
        del(seriesData['match_team_2']['updated_at'])

        matchType = MatchType.objects.get(id = seriesData['match_type'])
        seriesData['mtype'] = MatchTypeSerializer(matchType).data
        seriesData['match_type'] = seriesData['mtype']['match_type']
        del(seriesData['mtype'])

        matchFormat = MatchFormat.objects.get(id = seriesData['match_format'])
        seriesData['mformat'] = MatchFormatSerializer(matchFormat).data
        seriesData['match_format'] = seriesData['mformat']['match_format']
        del(seriesData['mformat'])

        matchFormat = LeagueSelection.objects.get(id = seriesData['league_selection'])
        seriesData['lselection'] = LeagueSelectionSerializer(matchFormat).data
        seriesData['league_selection'] = seriesData['lselection']['league_selection']
        del(seriesData['lselection'])

        
        x=date.fromisoformat(seriesData['match_start_date'])
        matchDate=x.strftime("%d %b %Y")

        matchTime= seriesData['match_time'][:-6] +" IST"

        seriesData['match_start_date']= matchDate +" "+ matchTime

        seriesData['match_time']=""

        del(seriesData['status'])
        del(seriesData['created_at'])
        del(seriesData['updated_at'])

    return Response({"status":"Success","data":matchManage})

@api_view(['POST'])
def viewPackage(request):
    packageActive="false"
    CDate = date.today()
    CurrentDate=datetime.datetime(CDate.year, CDate.month, CDate.day)

    Package = PackageManage.objects.filter(status = '1')
    matchPackage=PackageManageSerializer(Package,many=True).data

    App = AppVersion.objects.get(status = '1')
    appVersion=AppVersionSerializer(App).data
    
    for packageData in matchPackage:
        per = int(packageData['discount_price'])
        totalAmount = int(packageData['package_price'])
        amount= (totalAmount/100)*per
        dis_amount=totalAmount-amount
        packageData['discount_amount'] = str(int(dis_amount))
        
        if packageData['package_status'] == '0':
            packageData['package_status'] = 'None'
        
        elif packageData['package_status'] == '1':
            packageData['package_status'] = 'Trending'
            
        else:
            packageData['package_status'] = 'Big Winning'

        packageData['discount_price']=str(packageData['discount_price'])

        del(packageData['status'])
        del(packageData['created_at'])
        del(packageData['updated_at'])
    
        userID=request.POST['user_id']
        checkUserPackage = TransactionManage.objects.filter(user_id = userID,package_id=packageData['package_id'],paid_status='0')
      
        if len(checkUserPackage)==0:
            packageData['expiry_date']=''
            packageData['user_package_status']='false'

        else:
            check=TransactionManage.objects.get(user_id = userID,package_id=packageData['package_id'],paid_status='0')
            dataOrder=TransactionManageSerializer(check).data
            exDate=packageData['select_month']*30

            if packageData['select_day'] is None:
                date_1 = datetime.datetime.strptime(dataOrder['active_data'], "%Y-%m-%d")
                countDays=exDate
                end_date = date_1 + datetime.timedelta(countDays)

                

                if CurrentDate > end_date:
                    packageData['expiry_date']=''
                    packageData['user_package_status']='false'

                else:
                    days_left= (end_date - CurrentDate).days

                    packageData['expiry_date']=str(days_left) + " days "
                    packageData['user_package_status']='true'
                    packageActive='true'
                
            else:

                date_1 = datetime.datetime.strptime(dataOrder['active_data'], "%Y-%m-%d")
                
                countDays=exDate+packageData['select_day']
                end_date = date_1 + datetime.timedelta(countDays)

                if CurrentDate > end_date:
                    packageData['expiry_date']=''
                    packageData['user_package_status']='false'
                else:
                    
                    days_left= (end_date - CurrentDate).days

                    packageData['expiry_date']=str(days_left) + " days "
                    packageData['user_package_status']='true'
                    packageActive='true'
            
    return Response({"status":"Success",'packageActive':packageActive,"version":appVersion['version'],"data":matchPackage})

@api_view(['POST'])
def postPackageData(request):
    if request.POST['package_id']:
        package=request.POST['package_id']
        packageId =int(package)
        post = PostManage.objects.filter(status = '1')
        postManage=PostManageSerializer(post,many=True).data

        matchValue=[]
        
        for check in postManage:
            if packageId in check['select_package']:
                match = MatchManage.objects.get(id=check['select_match'])
                check['match']=MatchManageSerializer(match).data
                matchValue.append(check['match'])

        for dataTeam in matchValue:
            matchTeam1 = TeamManage.objects.get(id = dataTeam['match_team_1'])
            dataTeam['match_team_1'] = TeamManageSerializer(matchTeam1).data
            del(dataTeam['match_team_1']['status'])
            del(dataTeam['match_team_1']['created_at'])
            del(dataTeam['match_team_1']['updated_at'])

            matchTeam2 = TeamManage.objects.get(id = dataTeam['match_team_2'])
            dataTeam['match_team_2'] = TeamManageSerializer(matchTeam2).data
            del(dataTeam['match_team_2']['status'])
            del(dataTeam['match_team_2']['created_at'])
            del(dataTeam['match_team_2']['updated_at'])

            seriesName = Series.objects.get(id = dataTeam['series_name'])
            dataTeam['sname'] = SeriesSerializer(seriesName).data
            dataTeam['series_name'] = dataTeam['sname']['series_name']
            del(dataTeam['sname'])
            
            matchType = MatchType.objects.get(id = dataTeam['match_type'])
            dataTeam['mtype'] = MatchTypeSerializer(matchType).data
            dataTeam['match_type'] = dataTeam['mtype']['match_type']
            del(dataTeam['mtype'])
    
            matchFormat = MatchFormat.objects.get(id = dataTeam['match_format'])
            dataTeam['mformat'] = MatchFormatSerializer(matchFormat).data
            dataTeam['match_format'] = dataTeam['mformat']['match_format']
            del(dataTeam['mformat'])
    
            matchFormat = LeagueSelection.objects.get(id = dataTeam['league_selection'])
            dataTeam['lselection'] = LeagueSelectionSerializer(matchFormat).data
            dataTeam['league_selection'] = dataTeam['lselection']['league_selection']
            del(dataTeam['lselection'])

            x=date.fromisoformat(dataTeam['match_start_date'])
            matchDate=x.strftime("%d %b %Y")

            matchTime= dataTeam['match_time'][:-3] +" IST"

            dataTeam['match_start_date']= matchDate +" "+ matchTime

            dataTeam['match_time']=""

            del(dataTeam['status'])
            del(dataTeam['created_at'])
            del(dataTeam['updated_at'])
        
        return Response({"status":"Success","data":matchValue})

    else:
        return Response({"status":"failed","msg":"invalid Request"})


@api_view(['POST'])
def transactionApi(request):
    userID=request.POST['user_id']
    packageId=request.POST['package_id']

    userD=User.objects.get(id=userID)
    userEmailData=UserSerializer(userD).data

    checkUserExist=TransactionManage.objects.filter(user_id=userID,package_id=packageId,paid_status='0')
    if len(checkUserExist)==0:

        serializer = TransactionManageSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()

            subject = 'Your Plan is Activated'
            message = 'Congrats! You have Successfully Activated CricYorker Prime Pack. Our experts are working to provide you best teams from upcoming match. Login to CricCyorker App and view teams for upcoming matches.'
            email_from = settings.EMAIL_HOST_USER 
            recipient_list = [userEmailData['user_email'], ] 
            data=send_mail( subject, message, email_from, recipient_list ) 

            return Response({"status":"Success","msg":"Order saved"})
        else:
            return Response({"status":"failed","msg":"invalid Request"})

    else:
        updatePackageExist=TransactionManage.objects.get(user_id=userID,package_id=packageId,paid_status='0')
        updatePackageExist.paid_status= '1'
        updatePackageExist.save()

        serializer = TransactionManageSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()

            subject = 'Plan Re-Activated'
            message = 'Thanks for Re-Activating your package.'
            email_from = settings.EMAIL_HOST_USER 
            recipient_list = [userEmailData['user_email'], ] 
            data=send_mail( subject, message, email_from, recipient_list ) 

        return Response({"status":"success","msg":"Order updated"})
        # return Response({"status":"failed","msg":"Order already Exist"})

@api_view(['POST'])
def postDataApi(request):

    matchId=request.POST['match_id']

    matchData = MatchManage.objects.get(id = matchId)
    matchTeamData = MatchManageSerializer(matchData).data

    seriesData = Series.objects.get(id = matchTeamData['series_name'])
    sTeamData = SeriesSerializer(seriesData).data
    matchTeamData['series_name']=sTeamData['series_name']

    teamData = TeamManage.objects.get(id = matchTeamData['match_team_1'])
    mTeamData = TeamManageSerializer(teamData).data
    matchTeamData['match_team_1']=mTeamData['team_name']

    teamData1 = TeamManage.objects.get(id = matchTeamData['match_team_2'])
    mTeamData1 = TeamManageSerializer(teamData1).data
    matchTeamData['match_team_2']=mTeamData1['team_name']
    del(matchTeamData['match_type'])
    del(matchTeamData['match_format'])
    del(matchTeamData['league_selection'])
    del(matchTeamData['status'])
    del(matchTeamData['created_at'])
    del(matchTeamData['updated_at'])

    x=date.fromisoformat(matchTeamData['match_start_date'])
    matchDate=x.strftime("%d %b %Y")

    matchTime= matchTeamData['match_time'][:-3] +" IST"

    matchTeamData['match_start_date']= matchDate +", "+ matchTime

    matchTeamData['match_time']=""


    post=PostManage.objects.get(select_match=matchId)
    postData = PostManageSerializer(post).data


    date_string = postData['created_at'][:-22]
    date_string_time_before = postData['created_at'][:-16]
    date_string_time = date_string_time_before[11:]

    y=date.fromisoformat(date_string)
    date_string=y.strftime("%d %b %Y")

    matchTeamData['created_at']=date_string +", "+ date_string_time + " IST"
    matchTeamData['description']=postData['description']
    

    tPost=TeamCreatePost.objects.filter(post_id=postData['PostManage_id'])
    teamPost = TeamCreatePostSerializer(tPost,many=True).data

    matchTeamData['screen_shot_images']=[]
    i=0
    for sShot in teamPost:
        i=i+1
        matchTeamData['screen_shot_images'].append({"screen_shot":sShot['team_imageUpload'],"count":str(i)})
        
    return Response({"status":"Success","data":matchTeamData})

@api_view(['POST'])
def sendMail(request):
    userEmail=request.POST['email']
    subject = 'welcome to Cricyorker'
    message = 'Hi thank you for registering in cricyorker.'
    email_from = settings.EMAIL_HOST_USER 
    recipient_list = [userEmail, ] 
    data=send_mail( subject, message, email_from, recipient_list ) 
    return Response({"data":data})


@api_view(['POST'])
def sendNotification(request):
    
    # users = models.NewEventNotification.objects.all().filter(is_notify=1)
    # serializer = NewEventNotificationSerializer(users, many=True)
    tokens = ['f8T97RkxtMg:APA91bEQ4rGn48Oo-vB5oODQy32V8MNrJPVUZjPEytNpp08ZfyMSTMIrXkrSGIHT0BW6cEXpKo9_NkmA0VoSt0Lnx8GWR_ez0w_cYpCw8foNjsTZkeiZWVaGGw7wSyK8HeCQ1lCrAJtb']
    # for user in serializer.data:
    #     tokens.append(user['user_token'])
    if tokens:

        push_service = FCMNotification(api_key='AAAAyLSRPqg:APA91bHnHmo2wN8ItP-PqQHvZNOligRl9IZcut_ikyU1DIGWpHFk7DLdWYWB5uQXBaOYyXKIx8KPh_h1LOEHxBaGZuMm6CTNNeKUAjYkMlq89G7d2wjSJseWGABemknG0oD6GIWTUVMJ')
        message_title = "New Event"
        # message_body = data
        message_body = "Welcome To CricYorker"

        result = push_service.notify_multiple_devices(
            registration_ids=tokens, message_title=message_title, message_body=message_body)

    return Response(result)

@api_view(['POST'])
def updateProfile(request):
    if request.POST['user_id']:

        UserId=request.POST['user_id']
        userData=User.objects.get(id=UserId)
        serializer=UserSerializer(userData, data = request.data)
        if serializer.is_valid():
            serializer.save()
            data=UserSerializer(userData).data
            del(data['isVerified'])
            del(data['counter'])
            del(data['user_social_id'])
            del(data['user_status'])
            del(data['user_image'])
            del(data['user_imageUpload'])
            del(data['login_type'])
            del(data['fcm_id'])
            del(data['created_at'])
            del(data['updated_at'])
        return Response({"status":"Success","msg":"profile updated successfully","data":data})

    else:
        return Response({"status":"failed","msg":"invalid Request"})


#for demo user function in addmobile API
@api_view(['POST'])
def demoUserApi(request):
    if request.POST['user_id']:
        user_Id=request.POST['user_id']
        checkdata=demoUser.objects.filter(demoUser=user_Id)
        if len(checkdata)==0:
            return Response({"status":"Failure","msg":"no data avialable","data":""})

        else:
            checks=demoUser.objects.get(demoUser=id,status = '1')

            demoData=demoUserSerializer(checks).data
            match=demoData['select_match_demo']

            summary=[]
            matchValue=[]
            for val in match:
                post = PostManage.objects.get(id=val,status = '1')
                postManage=PostManageSerializer(post).data
        
                match = MatchManage.objects.get(id=postManage['select_match'])
                check=MatchManageSerializer(match).data
                matchValue.append(check)

            
            for dataTeam in matchValue:
                matchTeam1 = TeamManage.objects.get(id = dataTeam['match_team_1'])
                dataTeam['match_team_1'] = TeamManageSerializer(matchTeam1).data
                del(dataTeam['match_team_1']['status'])
                del(dataTeam['match_team_1']['created_at'])
                del(dataTeam['match_team_1']['updated_at'])

                matchTeam2 = TeamManage.objects.get(id = dataTeam['match_team_2'])
                dataTeam['match_team_2'] = TeamManageSerializer(matchTeam2).data
                del(dataTeam['match_team_2']['status'])
                del(dataTeam['match_team_2']['created_at'])
                del(dataTeam['match_team_2']['updated_at'])

                seriesName = Series.objects.get(id = dataTeam['series_name'])
                dataTeam['sname'] = SeriesSerializer(seriesName).data
                dataTeam['series_name'] = dataTeam['sname']['series_name']
                del(dataTeam['sname'])
                
                matchType = MatchType.objects.get(id = dataTeam['match_type'])
                dataTeam['mtype'] = MatchTypeSerializer(matchType).data
                dataTeam['match_type'] = dataTeam['mtype']['match_type']
                del(dataTeam['mtype'])
        
                matchFormat = MatchFormat.objects.get(id = dataTeam['match_format'])
                dataTeam['mformat'] = MatchFormatSerializer(matchFormat).data
                dataTeam['match_format'] = dataTeam['mformat']['match_format']
                del(dataTeam['mformat'])
        
                matchFormat = LeagueSelection.objects.get(id = dataTeam['league_selection'])
                dataTeam['lselection'] = LeagueSelectionSerializer(matchFormat).data
                dataTeam['league_selection'] = dataTeam['lselection']['league_selection']
                del(dataTeam['lselection'])

                x=date.fromisoformat(dataTeam['match_start_date'])
                matchDate=x.strftime("%d %b %Y")

                matchTime= dataTeam['match_time'][:-3] +" IST"

                dataTeam['match_start_date']= matchDate +" "+ matchTime

                dataTeam['match_time']=""

                del(dataTeam['status'])
                del(dataTeam['created_at'])
                del(dataTeam['updated_at'])
            
        return Response({"status":"Success","data":matchValue})
    
    else:
        return Response({"status":"failed","msg":"invalid Request"})
    



    