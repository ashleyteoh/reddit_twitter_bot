# Reddit-to-Twitter bot
A fully automated Twitter bot built using Selenium and the Reddit API. The bot fetches trending posts from specified subreddits and posts them directly to Twitter via a Google Chrome instance.

## Features:
- Automated Login: Securely logs into your Twitter account.
- Reddit Integration: Fetches top posts from subreddits and automatically shares them on Twitter.
- Twitter Engagement: Likes tweets on your homepage and searches for specified keywords or hashtags, liking relevant tweets.
- Session Management: Logs out of your Twitter account after completing tasks.

## Examples:

All the following tasks are completely automated without any manual user input. The script launches Chrome instance and carries out the tasks provided.
### Logging in
![login gif](https://github.com/ashleyteoh/reddit_twitter_bot/blob/master/gifs/login.gif)


#### Posting Tweets from top Reddit posts
![post tweet gif](https://github.com/ashleyteoh/reddit_twitter_bot/blob/master/gifs/post_tweet.gif)



#### Adding likes to tweets on homepage
![like homepage gif](https://github.com/ashleyteoh/reddit_twitter_bot/blob/master/gifs/like_home.gif)


#### Adding likes to tweets on search results of some query
![search](https://github.com/ashleyteoh/reddit_twitter_bot/blob/master/gifs/search.gif)

## Running project locally:
1. Insert authentication keys for your twitter account under post_tweet.py
2. Run desired action file
### To post from Reddit:
 1. Get Reddit OAuth keys [here](https://github.com/reddit-archive/reddit/wiki/OAuth2), fill in reddit_bot_class.py details
 2. Run reddit_bot_class.py with desired subreddit to populate hot_posts.csv
 3. Run post_tweet.py 
