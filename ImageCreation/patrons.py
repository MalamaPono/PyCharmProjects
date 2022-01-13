# This project uses Pillow and the Patreon API to automate Image Creation.
# It uses the Patreon API key to get names of your supporters that you can then create an imasge with
# by listing those names in order on an image or something.

# All this info and how to work with API's is inside the Patreon API documentation. The API documentation
# is your best friend whenever working with API's.
import patreon
from image import create_credits

access_token = "enter your access token here"
api_client = patreon.API(access_token)
campaign_response = api_client.fetch_campaign()
campaign_id = campaign_response.data()[0].id()

all_pledges = []
cursor = None
# the cursor tells us how to get to each new page so we can loop through every page of patrons and get
# all their data in one list. When cursor is none, it retrieves the first page.

print('Fetching Patron Info...')
while True:
    # gets 25 patreon supporters on certain page
    pledges_response = api_client.fetch_page_of_pledges(campaign_id, 25,cursor=cursor,fields={'pledge':['total_historical_amount_cents','declined_since']})
    cursor = api_client.extract_cursor(pledges_response)
    all_pledges += pledges_response.data()
    # adds the pledges response list to the back of the  all_pledges list

    # cursor will be set to none when there are no more pages to retrieve
    if cursor == None:
        break

pledges_info = []

for pledge in all_pledges:
    declined = pledge.attribute('declined_since')
    reward_tier = 0

    if pledge.relationships()['reward']['data']:
        reward_tier = pledge.relationship('reward').attribute('amount_cents')

    if not declined and reward_tier >= 500:
          pledges_info.append({'full_name':pledge.relationship('patron').attribute('full_name'),
                               'total_historical_amount_cents': pledge.attribute('total_historical_amount_cents')
                               })

sorted_pledges = sorted(pledges_info,key=lambda item:item['total_historical_amount_cents'],reverse=True)

sorted_names = [pledge['full_name'] for pledge in sorted_pledges]

# makes the image
create_credits(sorted_names)