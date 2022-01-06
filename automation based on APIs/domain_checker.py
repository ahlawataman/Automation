import requests
import argparse
import time

from twilio.rest import Client 

# set up cli domain argument
parser = argparse.ArgumentParser(description="Check domain for availability.")
parser.add_argument('domain', type=str, help="Domain name to be checked")
args = parser.parse_args()

# godaddy API credentials for authorization
api_key = "3mM44UbhLsi6Eh_JxtXDKoQ2NtcNGoVP7tCyn"
api_secret = "5f9du6Fy7u7hCFwNQvDmH1"
req_headers = {
    "Authorization": f"sso-key {api_key}:{api_secret}",
    "accept" : "application/json"
}

# twilio API credentials
account_sid = 'ACe0c1e513897383ebc38283bcda0d2a4a' 
auth_token = '[From_TWILIO_Dashboard]' 
client = Client(account_sid, auth_token)
to_whatsapp_number = "[to_whatsapp_number_associated_with_twilio_account]" # ex. +919876543210

def send_message(check_domain, to_whatsapp_number):
    domain_purchase_url = f"https://in.godaddy.com/domainsearch/find?domainToCheck={check_domain}"
    message = client.messages.create(
        from_='whatsapp:+14155238886',
        to=f'whatsapp:{to_whatsapp_number}',
        body=f'Your domain {check_domain} is now available for purchase. {domain_purchase_url}' 
    )
    print(f"Message was sent to {to_whatsapp_number}, message_id is {message.sid}")

# assemble the request url with the given domain    
def get_url(check_domain):
    return f"https://api.ote-godaddy.com/v1/domains/available?domain={check_domain}"

def check_availability(check_domain, to_whatsapp_number):
    url = get_url(check_domain)
    req = requests.get(url, headers=req_headers)

    # if the request was unsuccessful, notify the user and stop
    if req.status_code != 200:
        print(f"Could not get availability state of domain {check_domain} - Status Code {req.status_code}")
        return

    # check if the domain is available
    response = req.json()
    if response["available"] == True:
        print(f"Domain {check_domain} is available for purchase.")
        # send whatsapp message if domain is free
        send_message(check_domain, to_whatsapp_number)

    else:
        print(f"{time.strftime('%Y-%m-%d %H-%M')} - Domain {check_domain} is not available.")

check_availability(args.domain, to_whatsapp_number)