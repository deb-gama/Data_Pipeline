import requests
import json
import os

from dotenv import load_dotenv
load_dotenv()


def send_slack_notification(webhook_url, message, username='DataPipelineBot', icon_emoji=':robot_face:'):
    headers = {'Content-Type': 'application/json'}
    data = {
        'text': message,
        'username': username,
        'icon_emoji': icon_emoji
    }
    response = requests.post(webhook_url, headers=headers, data=json.dumps(data))
    
    if response.status_code == 200:
        print('Notification sent successfully!')
    else:
        print(f'Failed to send notification. Status code: {response.status_code}, Response: {response.text}')

# Example usage
webhook_url = os.environ["SLACK_WEBHOOOK_URL"]
message = '''
:ghost: BOO! :ghost:
Hello from your Data Pipeline project!
I am your :slack: Bot :smile: :tada::tada::tada:
:white_check_mark: :white_check_mark: :white_check_mark:
'''
send_slack_notification(webhook_url, message)
