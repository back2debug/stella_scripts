**Feature request**
Customer reports an issue with a task but it is actually a feature request	
Hi {{ticket.requester.first_name}}
(If they called the feature request "an issue")I\'m really sorry to hear about your problems with &lt;product_name&gt;&lt;task&gt;. Actually, this is a feature that we haven\'t considered adding yet. Being able to &lt;feature_request&gt; seems like an awesome thing to have. 
I have passed this idea (or enhancement request) along to our product team. Thank you for taking the time to share this with us!

workaround if necessary
We cannot accommodate every piece of feedback from every customer. But we will do our best to always ensure the best product experience possible.

**Bug report**	
Customer has reported a bug	
Hi {{ticket.requester.first_name}},
I'm really sorry to hear about your issues with &lt;product_name&gt;&lt;task&gt;. I've looked into your problem and it seems to be a bug. You're the first person to report this, so thank you! 
The issue has been escalated to our product team for prioritizing.
I understand that in this situation you won't be able to &lt;insert_task&gt;. &lt; insert workaround if available

**Convert Manager to Agent**	
Client wants to demote manager to agent status	
Hi {{ticket.requester.first_name}},
Thanks for reaching out and we are happy to assist! The Convert to Team Member button will not be displayed for a team leader if they had team members who sent out requests.
This is not a fully supported feature on Stella Connect. To complete this task, please visit our Help Center.<a href="https://stellaservice.zendesk.com/hc/en-us/articles/115005308248-Converting-Managers-to-Agents" target="_blank" rel="noreferrer">Moving a team member from Manager to Agent</a>
Thanks and let us know if you need anything else!

**Whitelisting**
Client needs whitelist	
Hi {{ticket.requester.name}},
Please whitelist the following IP and domain to ensure email deliverability to all users.
The outbound email delivery IP address is 198.2.180.76 
The outbound email domain to whitelist is admin@stellaconnect.net
Additionally, if agents have restrictions to the websites they can visit, please visit our Help Center for a complete list of domains requiring whitelisting.<a href="https://stellaservice.zendesk.com/hc/en-us/articles/235669147-Stella-Connect-Whitelist" target="_blank" rel="noreferrer">Stella Connect Whitelist</a>
Thanks and let us know if you need anything!

**Survey Rendering in Email Clients**	
Customer is questioning appearance of email in browser	
Hi {{ticket.requester.first_name}}.
Thanks for reaching out! After investigating the issue you raised we can see there are certain older email clients that do not display the Connect Request emails as expected. The wide array of email and web clients currently available limits our control over the rendering of styles. I can confirm that with &lt;client&gt; on a &lt;OS&gt; machine users will see a defaulting to &lt;default style&gt; when viewing a Connect feedback request. 

**Interaction with agents**	
Client's agent submits support ticket	
Hi {{ticket.requester.first_name}},
We recently had one of your team members contact us regarding &lt;issue&gt;. It is our standard practice to interact directly with company admins. 
Please reach out to team member regarding their issue. Let us know if we can be of additional assistance. After investigating the matter, resolution

**UTC Times explanation**
Explaining the timing of data for Stella Connect	
<p>Example:</p><p>Surveys processed after 7pm EST would be 12am UTC. Our dashboards in Connect are aligned with the UTC time zone as this supports all of our clients around the world. Unfortunately, this makes any requests sent after 8pm EST to appear to be sent the following day. We do provide these UTC unix timestamps within the response export csv.</p>

**Export delays**
Hi {{ticket.requester.first_name}},
Thank you for reaching out. We apologize for the delay experienced with the export service this morning. It is a known issue that our team is currently working to resolve.
Please feel reach out if you experience any delays in the future but we are monitoring the situation as the team determines a resolution.

**Star Rating Changes**
Hi {{ticket.requester.first_name}},
We capture the selection made in the email. Once the customer opens the survey (selecting a star) they can make adjustments to the star rating. Star rating shows the rating that was submitted and is the field used for all calculations.
Let us know if you have any other questions.

**Ticket close**
We believe your ticket has been resolved and have changed the status to “Closed.” If you feel it has not been completed, please let us know.

**Image Sizing**
Most file types are supported and the image will be autosized to fit so you shouldn't run into any issues. 
To get the image to fit, we recommend that the image be cropped or resized to square format. 
You can upload a JPG or PNG file.
The maximum file size for the branding image upload is 20MB. This file limit is also applied to the profile photo upload
<ul>
	<li>Can be png, jpg, tiff, bmp, and several other file types.</li>
	<li>Horizontal/wide logos are best for Connect requests (as opposed to square logos)</li>
	<li>Company logos are not cropped and are shown in the same aspect ratio as uploaded.</li>
	<li>Logos should be at least 300px wide by 150px tall. We will size them down if needed as defined below.</li>
	<li>If the logo is wider than 300px, it will be sized down to 300px wide (the height will be proportionately adjusted to maintain the aspect ratio)</li>
	<li>If the logo is taller than 150px, it will be sized down to 150px tall (the height will be proportionately adjusted to maintain the aspect ratio)</li>
	<li>Logos will always size down if needed to ensure that they fit on the device and screen size of the customer.</li>
</ul>
Troubleshooting questions: 
What devices are the screenshots from?
Who are they from? customer? another employee?
Does the logo resize when you change the browser window?
Is it possible to view the survey in another browser and resize the window?
	
**Remove admin account**	
Thanks for reaching out and we are happy to help! In order to remove a company admin, you have to access their profile by selecting the green pencil on the right hand side. De-select the company admin checkbox and update. They will show up on the Manager tab. You need to select deactivate (the red circle), reassign any team members and update. The team lead will be deactivated
If the company admin profile does not have a the checkbox to remove admin rights, they are probably the main company admin. Let us know who to make the new main admin for your account.
	
**Salesforce Error: customer email missing**	
Types of errors that will and will not disable the package	
Hi {{ticket.requester.first_name}},
We were copied on an error for your Salesforce integration regarding the customer email field missing.
We have seen 3 use cases:
	<li> The email is actually missing - Please make sure you have the logic in your workflow or process builder to filter out cases or calls if the email address is null.</li><
	li>Case closed and assigned to a queue - </li>
	<li>Team member makes changes to the case after the <i>Send Stella Connect Request at</i> datetime field is set</li><

You can confirm this by looking at the case. Click on the link below and check out (or screenshot) the case history.</p><p><a href="https://stellaservice.zendesk.com/hc/en-us/articles/115004581328-Salesforce-Tracing-Errors" target="_blank" rel="noreferrer">Please see our article for tracing errors in Help Center</a>Thanks!
	
**Team Member moving around**	
<p>Team member moves from 1 Team Leader to another:</p><p>Team dashboards:</p><p>Only see requests when under you as a manager</p><p>Do not see previous requests</p><p>Deactivated agents reporting for the team leader:</p><p>You can see the team member still in the trends dashboard</p><p>You can see them on the team if the time period is when they were on that team</p><p><br></p>
	
**Zendesk: Hide ticket fields**	
There is an app in the marketplace.<a href="https://www.zendesk.com/apps/support/hide-ticket-fields/?source=app_directory" target="_blank" rel="noreferrer">https://www.zendesk.com/apps/support/hide-ticket-fields/?source=app_directory</a>
After creating the custom field on the ticket, the app will take you through setting up the restrictions to hide the field.
	
**Investigating low response or why is my team member not getting responses**	
Team Member
Team member profile active
Team member identifier is correct: employee email address or ID on profile matches what is being sent over
API status page / Invalid requests
Review errors on the left hand column Export report
Filter for team member
Review the Delivery status column: sent vs not sent / do not send 
	
**Welcome to Connect email not received**
When you create an agent or manager on Connect, they will receive a Welcome to Stella Connect email. There may be instances when your team member does not receive the email. 
Have team members check their spam folders and their inbox filtering.
Once this is completed, you can walk through the following steps:
Determine if the email address on the profile is correct. 
Update the email address if necessary. You might need to fill in profile\'s required fields (State, Profile Bio, Image) with temp content. Update and Approve customer profile Resend confirmation email.
If the email address is correct in the profile page, you can resend the confirmation from the team members profile or have the team member use this link to request password resetting.
href="" target="_blank" rel="noreferrer">
To ensure email deliverability, please whitelist the following IP and domain to all users.
The outbound email delivery IP address is
The outbound email domain to whitelist is
	
**Salesforce Error:  reasons for package disabled**
The integration will be disabled (not run or re-scheduled) if any of the following are true:
Target Object Name is not defined.
Target Object Name is not valid (object doesn't exist).
Requested Datetime Field Name is not defined.
Requested Datetime Field Name is not valid (field doesn't exist on target object).
Customer Email Field Name is not defined.
Customer Email Field Name is not valid (field doesn't exist on target object).
Employee field type is set to ID and Employee ID Field Name is not defined.
Employee field type is set to ID and Employee ID Field Name is not valid (field doesn't exist on target object).
Employee field type is set to email and Employee Email Field Name is not defined.
Employee field type is set to email and Employee Email Field Name is not valid (field doesn't exist on target object).
Channel Field Name is not defined.
Channel Field Name is not valid (field doesn't exist on target object).
Language Field Name is not valid (field doesn't exist on target object).
Country Field Name is not valid (field doesn't exist on target object).
Brand Field Name is not valid (field doesn't exist on target object).
Tags Field Name is not valid (field doesn't exist on target object).
Do Not Send Field Field Name is not valid (field doesn't exist on target object).

**Incomplete Team member profile**	
Thanks for reaching out and we are happy to investigate. &lt;Team member&gt; profile is incomplete. All the fields with asterisk need to be filled out. These are missing:
	<li>profile pic</li>
	<li>profile bio</li>
You can use temp content and a company logo to move forward.<br><br>Let me know you are all set.
	
**Salesforce Error: requests too long**	
Steps for customer to take with Salesforce to resolve this issue	
You are seeing this error because the large number of cases in your production environment is causing the query to time out when the package runs. There are too many records to go through. Even though most records have a NULL value, a table scan still needs to be performed across all rows until the field is indexed. If this is not the case, let us know right away.
You will need to open a support ticket with Salesforce requesting an index for the datetime field you created along with the reasoning or justification. 
For the Salesforce ticket:
Please add an index to this datetime field on our Case object:
Field label: API label: Reasoning: We are using a managed package that depends on a datetime field that we have created. The package queries against this datetime field during a batch job and it is timing out.
	
**Salesforce: add profile after installation**	
Install for admins only and adding another profile to the package:
You are basically copying some of the settings over.
In the profile: Custom App Settings Select Stella Connect (StellaConnect__Stella_Connect) Connected App Access
Select Stella Connect Standard Tab Settings Stella Connect Configuration Default On Stella Connect Requests Default On (if you want the requests information accessible to this profile)
Custom Object Permissions Stella Connect requests Select All Basic Custom Field-Level Security Stella Connect Request Read Access All and Edit All except the 3 read only checkboxes Enabled Apex Class Access Edit and add all 3 Enabled Visualforce Page Access<br>Edit and add the 2


**Zendesk error: target disabled**	
You definitely want to review why the target was turned off so we can see if there is anything that needs to be corrected
Admin &gt; Channels &gt; API &gt; Target Failures
Select one that is for Stella Connect and scroll to the bottom
The reason will be there.
Once we discovered the root cause behind why the target was disabled, we can re-enabled it.

**Connection errors**
We can definitely help investigate your connection errors. Find certificate and supported protocols at <a href="https://www.ssllabs.com/ssltest/analyze.html?d=api.stellaconnect.net" target="_blank" rel="noreferrer" style="background-color: rgb(255, 255, 255); font-family: system-ui, -apple-system, BlinkMacSystemFont, &quot;Segoe UI&quot;, Roboto, Oxygen-Sans, Ubuntu, Cantarell, &quot;Helvetica Neue&quot;, Arial, sans-serif;">SSL server test</a>.
Here are a few considerations:
Support SNI and some applications require the SNI to be explicitly set in the communication.
Handle wildcard certificates. 
Proxy is configured to present the correct certificate.
Certificate is in right place: client profile vs. SSL-Proxy Profile

**Salesforce: Support tickets**	
When we need logs from salesforce and a ticket has to be opened with Salesforce support	
We need the following:
OrgID<
Approximate date and ID
Reproducible information if possible<
The customer to grant Salesforce Support access to their account for about a week. ( href="https://help.salesforce.com/articleView?id=granting_login_access.htm&amp;type=5" target="_blank" rel="noreferrer">https://help.salesforce.com/<wbr>articleView?id=granting_login_<wbr>access.htm&amp;type=5

**SAP ciphers**
You need to support SNI.
You have to explicitly specify SNI settings during communication
Ciphers used by previous clients:</p><p>ssl/client_ciphersuites= 982:HIGH:MEDIUM:+e3DES</p><p>the icm/HTTPS/client_sni_enabled= TRUE</p>

**Outage**	
We are currently experiencing issues within the platform. Our engineers are already aware of the situation and they are working hard on a quick solution. 
Please visit our <a href="http://status.stellaconnect.net/" target="_blank" rel="noreferrer">status page</a> and subscribe for updates.
We greatly appreciate your patience and apologize for any inconvenience caused.

**refreshing! hard refreshing! caching!**
Instructions for users to clear out cache and hard reset	
Crtl + refresh for both IE and Chrome.
Clear out history</p><p><br>You can try logging in from a private or incognito window also.
IE - Tools Private Browsing<br>Chrome - File New Incognito Window</p>

**Email digests**	
Always last 7 days (comparisons show 7 days before that)
Company shows high-level stats based on features: currently no multiple choice
Team digest shows each team member that has responses in those 7 days
Any team leader/admin can sign up for the company digest email
Any front-line team leader can sign up for team digest email for their own team
Email won\'t get sent if there are no responses in the last 7 days

**Salesforce: Resend request**	
We were copied on an error this morning for one of the survey requests.
You can resend it from the Stella Connect Requests tab.
Scroll to the SCR that was unsuccessful<br>Select it and click the resend button

**Log in issues**
Here are things to try:
Logging in from a different browser
Logging in from an incognito or private window in the browser: 
IE - Tools Private Browsing
Chrome - File New Incognito Window
There should be no error messages on the screen when you use this link.URL for company log in<
You can also try clearing out the cookies and cache on the browser.
You can hard refresh the browser: Crtl + refresh for both IE and Chrome.
If you still are having trouble:
If you have saved credentials, make the correct username and password are being sent.
Make sure you are not adding a space to the end of the username

**Automated emails from clients**
Hi {{ticket.requester.name}},
We are getting your automated responses from the &lt;type of email&gt; that Connect sends out. 
They have the subject: 
Subject: Re: You\'re missing your team\'s feedback on Stella Connect.
They are being sent to: &lt;insert who the email address being sent to&gt;
Please also update the account on Connect with a different email address to re-route these emails.  href="https://support.zendesk.com/hc/en-us/articles/226009928-How-do-I-create-a-trigger-based-on-a-ticket-subject-" target="_blank" rel="noreferrer">
You can also filter these out of the automated response flow by updating the trigger with a condition on subject text.
Thanks and let us know if you have any questions

**Salesforce Error: disabled package**	
When the package disables the integration, it will email the person who turned it on and Stella Service gets copied. If none of us are receiving the email, then Salesforce is disabling the integration.
If it is not enabled, you will need to see why it turned off and re-enable it.
To reactivate it,go to the Stella Connect Configuration tab and click Update Integration Status.
To investigate why it turned off, check to see <a href="https://help.salesforce.com/articleView?id=000170712&amp;language=en_US&amp;type=1" target="_blank" rel="noreferrer">there is anyone receiving Apex exception errors.</a> They would have received an error email. To check the jobs running for errors, they can follow Step 4 in our troubleshooting guide: href="https://stellaservice.zendesk.com/hc/en-us/articles/115004581328-Salesforce-Tracing-Errors" target="_blank" rel="noreferrer">Salesforce: Tracing Errors. 
Let us know what the errors are on the apex jobs.<br><br>Thanks and let me know if you have any questions.

**Steps to reproduce**
I\'m sorry to hear that you\'re having this experience. This is not indicative of the service we strive to provide here at Stella. We will be sure to get this worked out as quickly as we can. In order to best serve you, we will need just a few details. We recognize you said nothing is working. Can you give us more clarity and context on the issue? 
	<li>What part of Connect are you working in? </li>
	<li>What action are you trying perform? </li><li>Are you receiving any error messages?</li>

Our process is try to replicate the issue, find the root cause, and connect to walk you through steps and corrective action. We have looped in your CSM so they kept apprised of the situation and progress throughout.
We appreciate your patience and do send over any information you have and feel free to ask questions along the way. We\'re here to help.

**Re-routing to correct team**	
We're are happy to get that started for you. First, we'll tell you the support team doesn't actually handle these requests. We do have a (insert the right team or contact here) that will take care of that (or that will walk you through the process). To make sure you are taken of, I've CC'ed the (team or contact) here. I'll leave you both to discuss the project and don't hesitate to reach out if you have support needs.

**WSGC stores team member contact**	
redirects to the Store Support	
Thanks for reaching out! You can call into Williams Sonoma Store Support at 1-866-786-7343 and they will be able to assist with your request.