from twilio.rest import Client
ACCOUNT_SID = ""
AUTH_TOKEN = ""
TWILIO_NUMBER = ""
RECEIVER_NUMBER = "+9197XXXXXX80"
Client = Client(ACCOUNT_SID,AUTH_TOKEN)
message = Client.messages.create(body = "Hello I am Shyam",from_ = "Twilio_Number ",to = RECEIVER_NUMBER)
