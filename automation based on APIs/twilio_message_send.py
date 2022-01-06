from twilio.rest import Client 
 
account_sid = 'ACe0c1e513897383ebc38283bcda0d2a4a' 
auth_token = '[From_TWILIO_Dashboard]' 
client = Client(account_sid, auth_token)
 
message = client.messages.create( 
                              from_='whatsapp:+14155238886',  
                              body='Your appointment is coming up on July 21 at 3PM',      
                              to='whatsapp:[YOUR_TWILIO_ASSOCIATED_NUMBER]' # ex. +919876543210 
                          )
print(message.sid)