import requests
import json

# Jira credentials and API endpoint
jira_base_url = "https://domain.atlassian.net" # Change this
email = "email@example.com" # Change this
api_token = "api-token" # Change this
headers = {
    "Authorization": f"Basic {requests.auth._basic_auth_str(email, api_token)}",
    "Content-Type": "application/json"
}

# Automation rule creation endpoint
automation_url = f"domain.atlassian.net/rest/api/3/automation/rule" #Change this

# Define the automation rule
rule_payload = {
    "name": "SLA Breach Notification",
    "projects": {
        "useContext": False,
        "projectIds": ["10000"]  # Replace with your project ID
    },
    "triggers": [
        {
            "field": {
                "id": "customfield_10001",  # Replace with SLA field ID
                "name": "Time to resolution"
            },
            "condition": "LessThan",
            "value": "30m"
        }
    ],
    "conditions": [
        {
            "field": "priority",
            "operator": "equals",
            "value": "High"
        }
    ],
    "actions": [
        {
            "action": "sendEmail",
            "to": "assignee",
            "subject": "SLA Breach Imminent",
            "body": "The SLA for your assigned ticket is about to breach. Please prioritize resolution."
        }
    ]
}

# Send the request to create the rule
response = requests.post(automation_url, headers=headers, data=json.dumps(rule_payload))

if response.status_code == 200 or response.status_code == 201:
    print("Automation rule created successfully.")
else:
    print(f"Failed to create automation rule: {response.status_code}")
    print(response.text)
