import os
from decouple import config
from twilio.rest import Client
from otpauth.models import Custumer

# Set environment variables for your credentials
# Read more at http://twil.io/secure
def phone_otp_verify(token, otp):
    print("in otp_verify")
    client = Client(config('account_sid'), config('auth_token'))

    # Send OTP using Twilio
    custumer_obj = Custumer.objects.get(uuid = token)
    recipient_number =  custumer_obj.custumer_phone_number # Recipient's phone number
    otp_code = otp  # The OTP code
    recipient_number = '+91' + recipient_number
    print(recipient_number,otp_code)
    message_body = f'Your OTP code is: {otp_code}'

    message = client.messages.create(
        body=message_body,
        from_=config('verified_number'),  # Your Twilio phone number
        to='+919838741277'
    )

    print(f'Message SID: {message.sid}')