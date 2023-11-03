# package import statement
from SmartApi.smartConnect import SmartConnect 
import pyotp

def connect(form):
    print ("Hello world Angle Api")
    client = form.username.data
    pin = form.pin.data
    print(pin)
    api_key = 'lZuRspbx'
    username = client
    pwd = pin
    smartApi = SmartConnect(api_key)
    token = '6R5D46XUINYLXT3XKJ6AOGVDII'
    totp=pyotp.TOTP(token).now()
    correlation_id = "abcde"
    data = smartApi.generateSession(username, pwd,totp)
    authToken = data['data']['jwtToken']
    refreshToken = data['data']['refreshToken']
    feedToken = smartApi.getfeedToken()
    res = smartApi.getProfile(refreshToken)
    print("Res:", res)
