# Log collater for IBL

## What it does
Goes into your emails and extracts all the important parts of your logs for each week in .txt files

Will go to a **/logs** folder

## Setup

```pip install simplegmail```

### Get Gmail API credentials
- Go to https://console.cloud.google.com/
- Create a new project (or use an existing one)
- Go to APIs & Services > Credentials
- Click "Create Credentials" > OAuth client ID
  - App type: Desktop
- Download the client_secret.json file
- Place it in the same folder as the script


