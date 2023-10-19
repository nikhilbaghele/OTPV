from twilio.rest import Client
import sms 
import math
import random
client = Client(sms.account_sid, sms.auth_token)
str = "0123456789"
leng = len(str)
otp = ""

for i in range(6):
    otp += str[math.floor(random.random()*leng)]

message = client.messages.create(
    body = "your otp is "+otp,
    from_ = sms.twilio_number,
    to = sms.target_number
)
print(message.body)

