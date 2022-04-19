
import json
import requests


webhook_url = ''
slack_data = {'text': "Sup! We finished running automated tests! <click here> for details!"}

response = requests.post(
    webhook_url, data=json.dumps(slack_data),
    headers={'Content-Type': 'application/json'}
)
if response.status_code != 200:
    raise ValueError(
        'Request to slack returned an error %s, the response is:\n%s'
        % (response.status_code, response.text)
    )



