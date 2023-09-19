# Reddit-to-Twitter bot
A Google Chrome based twitter bot that uses Reddit API to fetch trending posts from subreddits, and post it on twitter. Also undergoes everyday tasks such as logging in, liking and searching tweets, and logging out. Made with Selenium.

## Features:
- Logging into your Twitter account
- Fetching Reddit top reddit posts to autopost
- Liking tweets of your homepage
- Searching for some keyword or hashtag
- Liking tweets of the search results
- Logging out of your account

## Examples:

All the following tasks are completely automated without any manual user input. The script launches Chrome instance and carries out the tasks provided.
### Logging in
![login gif](https://github.com/ashleyteoh/twitter-bot/assets/77535526/59b700e6-cde9-42fb-8ad7-eb53e14e254c)


#### Posting Tweets from top Reddit posts
![post tweet gif](https://github.com/ashleyteoh/twitter-bot/assets/77535526/0627e489-83f9-478e-8c7d-dcac0d0197c6)



#### Adding likes to tweets on homepage
![like homepage gif](https://github.com/ashleyteoh/twitter-bot/assets/77535526/d7930753-4265-4efe-a678-234abaea2ca6)


#### Adding likes to tweets on search results of some query
![search](https://github.com/ashleyteoh/twitter-bot/assets/77535526/0f5cae9c-be81-412f-bdec-54d8e8e30460)

## Running project locally:
1. Insert authentication keys for your twitter account under post_tweet.py
2. Run desired action file
### To post from Reddit:
 1. Get Reddit OAuth keys [here](https://github.com/reddit-archive/reddit/wiki/OAuth2), fill in reddit_bot_class.py details
 2. Run reddit_bot_class.py with desired subreddit to populate hot_posts.csv
 3. Run post_tweet.py 
