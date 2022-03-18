from datetime import datetime,timedelta
from django.contrib.auth.hashers import make_password, check_password
from Core.models import User
from bankxyzapi.settings.base import SECRET_KEY
import jwt

def login(mail,password):

    userinfo = User.objects.filter(email=mail)
    if userinfo.exists():
        uservalues = userinfo.values().first()  
        passwordCorrect = check_password(password,uservalues.get("password"))
        if passwordCorrect:
            ## "name":uservalues.get("firstname"),"email":mail,"role":uservalues.get("role"), "exp" : datetime.now() + timedelta(seconds=600)
            accesspayload = {
                "usr": uservalues.get("id"),
                "role": uservalues.get("role"),
                "exp" : datetime.utcnow() + timedelta(seconds=3600)
                }
            
            encodedAccess = jwt.encode(accesspayload,SECRET_KEY,algorithm="HS256")
            
            refreshPayload = {
                "email": mail,
                "password": password,
                "exp" : datetime.utcnow() + timedelta(seconds=3600)
                }
            
            encodedRefresh = jwt.encode(refreshPayload,SECRET_KEY,algorithm="HS256")
            docNumber = uservalues.get("docNumber")
            tokens = [encodedAccess,encodedRefresh, docNumber]

            return tokens
        else:
            return "Password Invalid"
    else:
        return "User Not Found"
