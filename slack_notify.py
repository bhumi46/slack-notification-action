import os
import sys
import requests
import json

# Capture environment variables
PR_AUTHOR = os.getenv('PR_AUTHOR')
REPO = os.getenv('REPO')
COMMIT = os.getenv('COMMIT')
MESSAGE = os.getenv('MESSAGE')
STATUS = os.getenv('STATUS')
WORKFLOW = os.getenv('WORKFLOW')
JOB_NAME = os.getenv('JOB_NAME')

# Get Slack mapping and token from environment (GitHub secrets)
SLACK_MAPPING = os.getenv('SLACK_MAPPING')
SLACK_OAUTH_TOKEN = os.getenv('SLACK_OAUTH_TOKEN')

# Debugging information
print("Start Slack notification debug...")
print(f"PR Author: {PR_AUTHOR}")
print(f"Repository: {REPO}")
print(f"Commit SHA: {COMMIT}")
print(f"Commit Message: {MESSAGE}")
print(f"Build Status: {STATUS}")
print(f"Workflow: {WORKFLOW}")
print(f"Job Name: {JOB_NAME}")

# Get the Slack user ID from the mapping
slack_mapping = json.loads(SLACK_MAPPING)
slack_author = slack_mapping.get(PR_AUTHOR)

if not slack_author:
    print(f"Slack mapping not found for {PR_AUTHOR}; exiting")
    sys.exit(1)

# Create the message with additional fields
slack_message = f"""
Build Status: *{STATUS}*
Repository: *{REPO}*
Commit: *{COMMIT}*
Message: *{MESSAGE}*
Author: *{PR_AUTHOR}*
Workflow: *{WORKFLOW}*
Job: *{JOB_NAME}*
"""

print(f"Sending Slack notification to: @{slack_author}")

response = requests.post(
    "https://slack.com/api/chat.postMessage",
    headers={
        "Authorization": f"Bearer {SLACK_OAUTH_TOKEN}",
        "Content-type": "application/json"
    },
    json={
        "channel": f"@{slack_author}",
        "text": slack_message
    }
)

if response.status_code == 200 and response.json().get('ok'):
    print("Slack notification sent successfully!")
else:
    print(f"Failed to send Slack notification. Response: {response.text}")
    sys.exit(1)
