
from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "ACa96d75c8de0bf665f025ddcf4680bc38"
# Your Auth Token from twilio.com/console
auth_token  = "9cef8b60b8a8c94199da6a7981a60d0c"

client = Client(account_sid, auth_token)

message = client.messages.create(
    to="+918668504134", 
    from_="+15865719993",
    body="good morning love!drive the bike properly.")

print(message.sid)
