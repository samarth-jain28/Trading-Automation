# package import statement
from SmartApi.smartConnect import SmartConnect #or from SmartApi.smartConnect import SmartConnect
import pyotp

api_key = 'lZuRspbx '
username = ''
pwd = ''
smartApi = SmartConnect(api_key)
token = ''
totp=pyotp.TOTP(token).now()
correlation_id = "abcde"
data = smartApi.generateSession(username, pwd)
#print(data)
authToken = data['data']['jwtToken']
refreshToken = data['data']['refreshToken']
feedToken = smartApi.getfeedToken()
#print("Feed-Token :", feedToken)
res = smartApi.getProfile(refreshToken)
print("Res:", res)