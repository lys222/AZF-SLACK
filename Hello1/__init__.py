# This function is not intended to be invoked directly. Instead it will be
# triggered by an orchestrator function.
# Before running this sample, please:
# - create a Durable orchestration function
# - create a Durable HTTP starter function
# - add azure-functions-durable to requirements.txt
# - run pip install -r requirements.txt

import logging
import os
# from slack_bolt import App
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError
import requests
import json

# app = App(
#     signing_secret = os.environ["SLACK_SIGNING_SECRET"],
#     token = os.environ["SLACK_BOT_TOKEN"]
# )

payload = [
{
    "color": "#f2c744",
    "blocks": [
        {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": "You have a new request:\n*<fakeLink.toEmployeeProfile.com|Fred Enriquez - New device request>*"
            }
        },
        {
            "type": "section",
            "fields": [
                {
                    "type": "mrkdwn",
                    "text": "*Type:*\nComputer (laptop)"
                },
                {
                    "type": "mrkdwn",
                    "text": "*When:*\nSubmitted Aut 10"
                },
                {
                    "type": "mrkdwn",
                    "text": "*Last Update:*\nMar 10, 2015 (3 years, 5 months)"
                },
                {
                    "type": "mrkdwn",
                    "text": "*Reason:*\nAll vowel keys aren't working."
                },
                {
                    "type": "mrkdwn",
                    "text": "*Specs:*\n\"Cheetah Pro 15\" - Fast, really fast\""
                }
            ]
        },
        {
            "type": "actions",
            "elements": [
                {
                    "type": "button",
                    "text": {
                        "type": "plain_text",
                        "emoji": True,
                        "text": "Approve"
                    },
                    "style": "primary",
                    "value": "click_me_123"
                },
                {
                    "type": "button",
                    "text": {
                        "type": "plain_text",
                        "emoji": False,
                        "text": "Deny"
                    },
                    "style": "danger",
                    "value": "click_me_123"
                }
            ]
        }
    ]
}]

#* 방법1) 웹훅으로 HTTP POST
def send_msg1(): 
    url = "https://hooks.slack.com/services/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"
    headers = {'Content-Type': 'application/json; charset=utf-8'}

    response = requests.post(url, data=json.dumps(payload), headers=headers)

    return f"Done!"

#* 방법2) Slack SDK에서 웹훅으로 메세지 전송
def send_msg2():
    token = os.environ["SLACK_BOT_TOKEN"]
    client = WebClient(token=token)

    global payload
    try :
        response = client.chat_postMessage(
            channel="C03STD086Q7",
            attachments= json.dumps(payload)
        )
    except SlackApiError as e:
        assert e.response["error"]

    return f"Done!"

def main(name: str) -> str:

    # return f"Hello!"
    # return send_msg1
    return send_msg2()


