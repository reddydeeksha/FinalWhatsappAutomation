import json
import requests

def reply_with_ai(myamsg):

    headers = {
        'Content-Type': 'application/json; charset=utf-8',
        'Authorization': 'Bearer ya29.c.Ko8B0Qd4CKxnCUFVlRwbQk2LbcPv43j_kK8Kn8Lqf4a2lV5b-86c5Crq0hqdxxmRB4wtSHra0iPFQN3GxVyhawmbVSTAXfxQp_76RKuUOss0yw8qw-YtSj5Z0ZrMEJv0ZiGIpBA9w4Ut5OWh9umjxmrdlnShzU0GyZTGrmDUvCY_UoVAG-xKM7pKQGKIMSHnB-o',
    }

    data = '{"queryInput":{"text":{"text":"'+myamsg+'","languageCode":"en"}},"queryParams":{"timeZone":"Asia/Calcutta"}}'

    response = requests.post(
        'https://dialogflow.clients6.google.com/v2/projects/moneyheist-dmrhrh/agent/sessions/158fe7d0-6228-2273-7c23-bd2b4a2adc3f:detectIntent',
        headers=headers, data=data)
    data = json.loads(response.text)
    return data['queryResult']['fulfillmentMessages'][0]['text']['text'][0]