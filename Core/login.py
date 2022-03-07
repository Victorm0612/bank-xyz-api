from datetime import datetime,timedelta
from django.contrib.auth.hashers import make_password, check_password
from Core.models import User
from bankxyzapi.settings.base import SECRET_KEY
import jwt

def login(mail,password):

    user = User.objects.filter(email=mail)
    if user.exists():
        uservalues = user.values().first()  
        passwordCorrect = check_password(password,uservalues.get("password"))
        if passwordCorrect:
            ## "name":uservalues.get("firstname"),"email":mail,"role":uservalues.get("role"), "exp" : datetime.now() + timedelta(seconds=600)
            accesspayload = {
                "usr": uservalues.get("id"),
                "role": uservalues.get("role"),
                "exp" : datetime.now() + timedelta(seconds=600)
                }
            
            encodedAccess = jwt.encode(accesspayload,SECRET_KEY,algorithm="HS256")
            
            refreshPayload = {
                "email": mail,
                "role": password,
                "exp" : datetime.now() + timedelta(seconds=1200)
                }
            
            encodedRefresh = jwt.encode(refreshPayload,SECRET_KEY,algorithm="HS256")

            tokens = [encodedAccess,encodedRefresh]

            return tokens
        else:
            return "Password Invalid"
    else:
        return "User Not Found"
