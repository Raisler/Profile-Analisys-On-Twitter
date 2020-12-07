import pandas as pd
import tweepy

# You need to create a python archive with the keys and tokens of twitter developer account.
from keys_project import consumer_key, consumer_secret, access_token, access_token_secret

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

username = 'elonmusk'
count = 500     # 03/12/2020 22:20 Brazil
try:     
 
 tweets = tweepy.Cursor(api.user_timeline,id=username).items(count)
 
 tweets_list = [[tweet.created_at,tweet.text] for tweet in tweets]
 
 tweets_df = pd.DataFrame(tweets_list)
 tweets_df.to_csv('collect1.csv')
except BaseException as e:
      print('failed on_status,',str(e))
      time.sleep(3)