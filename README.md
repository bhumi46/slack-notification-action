# Slack Notification Action

A GitHub Action for sending notifications to Slack based on the status of your workflows, pull requests, or commits. This action allows you to keep your team updated with real-time notifications directly in Slack.

## Features

- Send notifications to Slack when a build status changes.
- Include details like repository name, commit SHA, commit message, author, workflow name, and job name in the notification.

## Inputs

| Input Name       | Description                     | Required |
|------------------|---------------------------------|----------|
| `pr_author`      | PR Author                      | `true`   |
| `repo`           | Repository name                | `true`   |
| `commit`         | Commit SHA                     | `true`   |
| `message`        | Commit message                 | `true`   |
| `status`         | Build status                   | `true`   |
| `workflow`       | Workflow name                  | `true`   |
| `job_name`       | Job name                       | `true`   |
| `slack_mapping`  | JSON mapping of PR authors to Slack user IDs | `true`   |
| `slack_oauth_token` | Slack OAuth token          | `true`   |

## Usage

Here’s a basic example of how to use the Slack Notification Action in your GitHub workflow:

```yaml
name: Notify Slack

on:
  push:
    branches:
      - main

jobs:
  notify:
    runs-on: ubuntu-latest
    steps:
      - name: Send Slack Notification
        uses: yourusername/slack-notification-action@v1.0.0
        with:
          pr_author: ${{ github.actor }}
          repo: ${{ github.repository }}
          commit: ${{ github.sha }}
          message: ${{ github.event.head_commit.message }}
          status: 'success'
          workflow: ${{ github.workflow }}
          job_name: ${{ github.job }}
          slack_mapping: ${{ secrets.SLACK_MAPPING }}
          slack_oauth_token: ${{ secrets.SLACK_OAUTH_TOKEN }}
