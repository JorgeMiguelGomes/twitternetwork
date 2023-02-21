import tweepy
import pandas as pd

# API credentials
## Set up Twitter API credentials
consumer_key = "your_consumer_key"
consumer_secret = "your_consumer_secret"
access_token = "your_access_token"
access_secret = "your_access_secret"

# Authenticate to Twitter API
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

# Create API object
api = tweepy.API(auth,wait_on_rate_limit=True)

# Set query and date interval
query = 'your_keyword(s)'
start_date = '2023-02-20'
end_date = '2023-02-21'

# Fetch tweets with the given query and date interval
tweets = tweepy.Cursor(api.search, q=query, tweet_mode="extended", since_id=start_date, until_id=end_date).items()


# Create list to store tweet data
tweet_data = []

# Loop through tweets and store all information in the list
for tweet in tweets:
    print(tweet)
    tweet_data.append(tweet._json)

# Create pandas DataFrame from tweet data
df = pd.json_normalize(tweet_data)

# Save the DataFrame to a CSV file
df.to_csv('your_csv_filename.csv', index=False)
