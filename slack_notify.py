import os
import json
import requests

# Retrieve environment variables
slack_mapping = json.loads(os.getenv('SLACK_MAPPING'))
slack_oauth_token = os.getenv('SLACK_OAUTH_TOKEN')
pr_author = os.getenv('PR_AUTHOR')
repo = os.getenv('REPO')
commit = os.getenv('COMMIT')
message = os.getenv('MESSAGE')
status = os.getenv('STATUS')
workflow = os.getenv('WORKFLOW')
job_name = os.getenv('JOB_NAME')

# Prepare the Slack message
slack_user = slack_mapping.get(pr_author, pr_author)  # Fallback to the PR author if not mapped
slack_message = f"Notification from {repo}: {pr_author} has a commit ({commit}) with message: {message}. Status: {status} in {workflow} for job {job_name}"

# Send the message to Slack
headers = {
    'Authorization': f'Bearer {slack_oauth_token}',
    'Content-Type': 'application/json'
}
payload = {
    'channel': slack_user,
    'text': slack_message
}

response = requests.post('https://slack.com/api/chat.postMessage', headers=headers, json=payload)

if response.status_code != 200 or not response.json().get('ok'):
    raise Exception(f"Request to Slack API failed: {response.text}")
