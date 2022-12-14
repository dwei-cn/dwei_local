# tutorial: https://medium.com/@sharan.aadarsh/sending-notification-to-slack-using-python-8b71d4f622f3
# slack incoming webhooks: https://gm-fin.slack.com/services/B03RR589VUK

import json
import sys
import random
import requests
import yaml

if __name__ == '__main__':
    with open('../credentials/credentials.yml', 'r') as file:
        slack_incoming_webhook_url = yaml.safe_load(file)['slack_python']['webhook']

    with open('msg_builder.json', 'r') as myfile:
        data=myfile.read()

    slack_data = json.loads(data)

    byte_length = str(sys.getsizeof(slack_data))
    headers = {'Content-Type': "application/json", 'Content-Length': byte_length}
    response = requests.post(slack_incoming_webhook_url, data=json.dumps(slack_data), headers=headers)

    if response.status_code != 200:
        raise Exception(response.status_code, response.text)