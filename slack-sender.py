from dotenv import load_dotenv
import os
from datetime import datetime

load_dotenv()

print(os.environ.get('SLACK_ID'))

import requests

headers = {
    'Content-type': 'application/json',
}

json_data = {
    'text': 'Hello, World!',
}

response = requests.post(f'https://hooks.slack.com/services/T0838R6359U/B083FGRMHJ6/{os.environ.get("SLACK_ID")}',
                         headers=headers, 
                         json=json_data)

print(response)
