## Instructions for capturing tweets


### Setting up Twitter API credentials
1. Go to https://apps.twitter.com/
1. Sign In, and then follow the instructions below:
1. Press "Create New App"
1. Fill in form (you can enter your website or any website in the 'website' field i.e. http://google.com)
1. Press 'Create application'
1. Press 'Manage keys ...'
1. Press 'Create access tokens'
1. Find and save four values
    - Consumer Key
    - Consumer Secret
    - Access Token Key
    - Access Token Secret

### Running the code
1. Install TwitterAPI: `pip install TwitterAPI`
1. Substitute the four values saved from 'Setting up Twitter API credentials' in `twitter.py` in

```python
access_token_key = "<ENTER ACCESS TOKEN KEY>"
access_token_secret = "<ENTER ACCESS TOKEN SECRET>"

api_key = "<ENTER CONSUMER KEY>"
api_secret = "<ENTER CONSUMER SECRET>"

```

1. Run `python capture-tweets.py <topic>` to save tweets to file called `captured-tweets.txt` related to `<topic>`.
i.e. `python capture-tweets.py Google` or `python capture-tweets.py Iran`