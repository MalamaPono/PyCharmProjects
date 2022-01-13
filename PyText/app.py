from twilio.rest import Client
import config

client = Client(config.account_sid,config.auth_token)

call = client.messages.create(
    to="8087455820",
    from_="5702588656",
    body="damn she fine"
)

