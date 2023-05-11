import configparser
import time
import tweepy
import json

class TwitterEngagementTracker:
    def __init__(self, config_file='config.ini', output_file='engagement_scores.json'):
        # Load configuration from config_file
        self.config = configparser.ConfigParser()
        self.config.read(config_file)

        # Authenticate with Twitter API
        auth = tweepy.OAuth1UserHandler(
            self.config.get('Twitter', 'consumer_key'),
            self.config.get('Twitter', 'consumer_secret'),
            self.config.get('Twitter', 'access_token'),
            self.config.get('Twitter', 'access_token_secret')
        )
        self.api = tweepy.API(auth)
        self.interval = int(self.config.get('Twitter', 'interval'))
        self.users = self.config.get('Twitter', 'users').split(',')
        self.output_file = output_file

    def calculate_engagement_scores(self):
        engagement_scores = {}
        for user in self.users:
            tweets = self.api.user_timeline(screen_name=user, count=50, tweet_mode='extended')
            likes = sum(tweet.favorite_count for tweet in tweets)
            retweets = sum(tweet.retweet_count for tweet in tweets)
            followers = self.api.get_user(screen_name=user).followers_count
            engagement_score = (likes + retweets) / followers
            engagement_scores[user] = {'Engagement Score': engagement_score,
                                       'Total Likes': likes,
                                       'Total Retweets': retweets,
                                       'Followers': followers}
            time.sleep(1)  # Add a 1-second delay between API requests
        return engagement_scores

    def run(self):
        while True:
            engagement_scores = self.calculate_engagement_scores()
            # Append the engagement scores to the JSON file
            with open(self.output_file, mode='a+') as file:
                json.dump(engagement_scores, file)
                file.write('\n')  # Add a newline character to separate each JSON object

            # Wait for the next period before running the engagement calculation function again
            time.sleep(self.interval)
