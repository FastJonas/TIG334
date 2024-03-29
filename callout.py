from twilio.rest import Client

account_sid = "AC9ce42e4aa45fc638ad53e11d208af9l"
auth_token = "1c5608e7bce2965cde9ec59eac35880d"

twilio_number = '+15642323047'

your_number = '+46723000510'

client = Client(account_sid, auth_token)

call = client.calls.create(
    to=your_number,
    from_=twilio_number,
    url="https://call-gpt-5747-dev.twil.io/prompt"  # TwiML URL
)

print("Call SID:", call.sid)

