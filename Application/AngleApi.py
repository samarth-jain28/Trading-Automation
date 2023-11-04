# package import statement
from SmartApi.smartConnect import SmartConnect 
import pyotp

def connect(form):
    ## fetching data from client 
    client = form.username.data
    pin = form.pin.data
    totp = form.totp.data
 
    ## send client id pin and totp to broker 
    api_key = 'lZuRspbx'
    username = form.username.data
    pwd = form.pin.data
    smartApi = SmartConnect(api_key)
    token = form.totp.data
    try:
        totp=pyotp.TOTP(token).now()
    except:
        return "Invalid TOTP"
    correlation_id = "abcde"
    data = smartApi.generateSession(username, pwd,totp)

    ## checking response for input 
    if data['status']==False :
        return data['message']
    else:
        authToken = data['data']['jwtToken']
        refreshToken = data['data']['refreshToken']
        feedToken = smartApi.getfeedToken()
        res = smartApi.getProfile(refreshToken)
        return res

