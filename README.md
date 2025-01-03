# Jira-Service-Management-Setup-and-Optimization

First we select Service Management template and choose a suitable layout under the Create Project section.

Second, we costumize issue types. So, we open project settings and choose issue types.
You can use this issue type schema and apply it to multiple projects.

Next, we need to setup our workflows (either modify existing ones or create new ones).
You can add costume statuses like "Pending Approval", "Approval", etc...
The point of this step is to define conditions, validators and post functions.
### For example:
Select an existing workflow, click on "Add Transition" and connect the "In Progress" status to the "Resolved" status, and name the transition for example "Resolved"
Conditions: select the transition, open conditions tab, choose add new condition and select "User is in Group" condition, then specify the group as "Tech Support" or "Helpdesk". Save condition.
Validators: under the same transition go to validators tab, add a new validator, choose the field required validator and specify the field as the "Resolution" which must be filled before transitioning. Save Validator
Post Functions: under the same transition navigate to post functions tab, add new post function and choose "Assign to Reporter". Save the post function. This will automatically assign the issue to the original reporter after the transition.

Next, using Workflow Schemes, assign workflows to issue types.

Next, you wanna go to settings > issues > permission schemes and assign roles there. Before proceeding, you should know that each role needs to have certain permissions assigned.
### For example:

Admins should be able to modify project settings and workflows.
Helpdesk/Tech Support T1-T3 should be able to comment internally and resolve tickets.
Customers should be able to view and create tickets.

## Creating Custom Queues

Navigate to Queues in the sidebar of your project.
Click on New Queue to add it.
Now, here are some filters that I used, that could help you get started (These filters are for JQL which is Jira Query Language):

Prioritize the tickets:

priority = High AND resolution = Unresolved ORDER BY created DESC

SLA (Service-Level Agreement) tickets:

"Time to resolution" < remaining(1h)

You can name your tickets however you want and adjust columns for display. Save the queue and test this out before going live.

## Setting Up Automated Notifications and Escalations:

Go to your project settings and navigate to Automation. Now we can setup our new automation rule, which needs to be defined by trigger, condition and action:

Select create a new automation rule, and you can add the following:

Trigger: SLA Time Remaining
Condition: SLA < 30m
Action: Send Email to Assignee

This rule above will notify assignee via email if the SLA breach is imminent.

Other option is to use my python script from this repository Jauto.py.

### Prerequisites for using the python script are:

install the requests library:
pip install requests
Jira Cloud account with Admin permissions
Generation of API token from your Jira account

## Design a Knowledge Base Integration with Confluence:

To link Jira with Confluence, go to project settings > knoweledge base, and link your project to an existing Confluence page or create a new one.
What's important to define is:
Creating self-service articles with common issue resolutions
Categorization of articles. For example: Software Setup, Network Issues
Enabling self-service for users, meaning, allowing users to search knowledge base during ticket creation

### Note:

One important thing you need to know:

There are SLA responses and SLA resolutions. For example, a high priority ticket will need a response within 15 minutes but a resolution can happen for example in 1 hour. For low priority SLA response can be 1 hour, and resolution within 24h.
This all depends on the complexity of the issue provided in the ticket.
