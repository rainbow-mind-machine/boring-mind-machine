# Creating a Google App

The brief summary of what we cover here:

We need to create an application (something that will consume the API
endpoints), and we need to grant the application access to at least one Google
account.

### Set Up API and Create App

The first thing you must do is enable the APIs that you need.
This may include the Drive, Calendar, or other APIs.
You do this in the [Google Cloud Platform (GCP) console](https://console.cloud.google.com/).

Go to the [enable APIs](https://console.developers.google.com/flows/enableapi)
page and select a project from the drop down menu.  If you do not already have
a project, go to the [GCP console](https://console.cloud.google.com/) to create
a new one before visiting the enable APIs link above.

### Creating App Credentials

Now you will need to create OAuth credentials for your application. You can do this
on the API Credentials page. To get there, click the three-stack menu (a.k.a. the 
"hamburger" menu) and scroll down to the Products section and click "APIs and Services".
Now click the "Credentials" option on the left side.

Now create your credentials. Create "OAuth Client ID" credentials.
Use application type "Other".

When you create the credentials, you will be given a client ID and a client secret.
Copy these into a password manager or other location.


### Getting the App Credentials

Once you've created the credentials, you can either copy-and-paste the
client ID and client secret, or you can download them as a JSON file.

To copy-and-paste, find the OAuth client credentials you created in the
prior step and click the pencil icon on the right side. This will take
you to a page with the client ID and client secret.

To download as a JSON file, download credentials using the download button
(down-arrow icon) on the right side. This JSON file contains all credential
information (client ID and client secret).

Rename it `client_secret.json`.

### End Result

In the end you will have a JSON file with your OAuth application credentials
in it, and these will be used to authenticate with the user. The Google
OAuth process will load the keys from `client_secret.json`, and will
open a login link for the user to authenticate with their Google account.

The Google OAuth process also takes care of recieving the callback URL
and the token contained in it, so the bot account keys are also stored in
a JSON file.

No environment variables need to be set, the only thing that needs to be set
is the name of the JSON file containing the OAuth application's API credentials
(should be `client_secret.json`).

Once you have `client_secret.json` in the current directory, you're set to go.

