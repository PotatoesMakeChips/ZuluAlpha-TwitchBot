# Main imports
from datetime import datetime

# Required for CSV logging
import csv

# Requires for Discord Webhook Logging
import json
import requests
import os

def logAlert(username, alertReason, message):
    fields=[str(datetime.utcnow()),username,alertReason,message]

    # CSV logging
    with open(r'alertLog.csv', 'a') as f:
        writer = csv.writer(f)
        writer.writerow(fields)
        f.close()

    # Discord Webhook Logging
    url = os.environ['DISCORD_WEBHOOK']
    header = {"content-type": "application/json"}
    payload = {
        "username": "ZuluAlpha",
        "avatar_url": "",
        "content": str("||<@&" + os.environ['DISCORD_MOD_ROLE_ID'] + ">||"),
        "embeds": [
            {
                "author": {
                        "name" : "ZuluAlpha Twitch Bot"
                },
                "title": "Twitch Mod Alert",
                "fields": [
                    {
                        "name": "Time",
                        "value": fields[0],
                        "inline": True
                    },
                    {
                        "name": "User",
                        "value": fields[1],
                        "inline": True
                    },
                    {
                        "name": "Alert",
                        "value": fields[2],
                        "inline": False
                    },
                    {
                        "name": "Message",
                        "value": fields[3],
                        "inline": False
                    }
                ]
            }
        ]
    }
    response= requests.post(url,data=json.dumps(payload), headers=header, verify=True)
