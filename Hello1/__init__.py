# This function is not intended to be invoked directly. Instead it will be
# triggered by an orchestrator function.
# Before running this sample, please:
# - create a Durable orchestration function
# - create a Durable HTTP starter function
# - add azure-functions-durable to requirements.txt
# - run pip install -r requirements.txt

import logging
import os
from slack_bolt import App
import requests
import json


app = App(
    signing_secret = os.environ["SLACK_SIGNING_SECRET"],
    token = os.environ["SLACK_BOT_TOKEN"]
)

def send_msg(): 

    payload  = {
        "text" : "Hi hi Hello"
    }

    url = "https://hooks.slack.com/services/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"
    headers = {'Content-Type': 'application/json; charset=utf-8'}

    response = requests.post(url, data=json.dumps(payload), headers=headers)

    return f"Done!"

def main(name: str) -> str:

    # return f"Hello!"
    return send_msg()
