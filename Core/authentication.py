from Core.models import User
from bankxyzapi.settings.base import SECRET_KEY
from Core.login import login
import jwt


def authUsr(request):

    headers = request.headers.get("authorization")
    if headers is None:
            return "No Authorization Token Given"
    else:    
        try:
            jwtHeader = headers.split()
            payload = jwt.decode(jwtHeader[1],SECRET_KEY,algorithms=["HS256"])
            user = User.objects.filter(id=payload["usr"]).values().first()
            if user.get("role")==0 and payload["role"]==0:
                return "Successfull"
            else:
                return "User Not Authorized"
        except jwt.ExpiredSignatureError:
            return "Token expired"
        except IndexError:
            return "Token not valid"

            
def authTeller(request):

    headers = request.headers.get("authorization")
    if headers is None:
            return "No Authorization Token Given"
    else:    
        try:
            jwtHeader = headers.split()
            payload = jwt.decode(jwtHeader[1],SECRET_KEY,algorithms=["HS256"])
            user = User.objects.filter(id=payload["usr"]).values().first()
            if user.get("role")==0 and payload["role"]==0:
                return "Successfull"
            elif user.get("role")==1 and payload["role"]==1:
                return "Successfull"
            else:
                return "User Not Authorized"

        except jwt.ExpiredSignatureError:
            return "Token expired"
        except IndexError:
            return "Token not valid"

            
def authServ(request): 

    headers = request.headers.get("authorization")
    if headers is None:
            return "No Authorization Token Given"
    else:    
        try:
            jwtHeader = headers.split()
            payload = jwt.decode(jwtHeader[1],SECRET_KEY,algorithms=["HS256"])
            user = User.objects.filter(id=payload["usr"]).values().first()
            if user.get("role")==0 and payload["role"]==0:
                return "Successfull"
            elif user.get("role")==1 and payload["role"]==1:
                return "Successfull"
            else:
                return "User Not Authorized"

        except jwt.ExpiredSignatureError:
            return "Token expired"
        except IndexError:
            return "Token not valid"

            
def authTick(request):

    headers = request.headers.get("authorization")
    if headers is None:
            return "No Authorization Token Given"
    else:    
        try:
            jwtHeader = headers.split()
            payload = jwt.decode(jwtHeader[1],SECRET_KEY,algorithms=["HS256"])
            user = User.objects.filter(id=payload["usr"]).values().first()
            if user.get("role")==0 and payload["role"]==0:
                return "Successfull"
            elif user.get("role")==1 and payload["role"]==1:
                return "Successfull"
            else:
                return "User Not Authorized"

        except jwt.ExpiredSignatureError:
            return "Token expired"
        except IndexError:
            return "Token not valid"

def authRefresh(request):

    headers = request.headers.get("authorization")
    if headers is None:
            return "No Authorization Token Given"
    else:    
        try:
            jwtHeader = headers.split()
            payload = jwt.decode(jwtHeader[1],SECRET_KEY,algorithms=["HS256"])
            tokens = login(payload["email"],payload["password"])
            return tokens

        except jwt.ExpiredSignatureError:
            return "Token expired"
        except IndexError:
            return "Token prefix missing"
            
            