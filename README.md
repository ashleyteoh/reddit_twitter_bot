# Reddit-to-Twitter bot
A fully automated Twitter bot developed using Python and Selenium. This bot integrates with the Reddit API to fetch trending posts from subreddits and post them on Twitter. It includes robust error handling, session management, and dynamic interactions with Twitter's interface.

## Features:
- Automated Login: Securely logs into your Twitter account, with retry logic for handling element loading issues.
- Reddit Integration: Fetches top posts from subreddits and automatically shares them on Twitter.
- Twitter Engagement: Automatically likes tweets on your homepage, searches for specified keywords or hashtags, and interacts with search results.
- Dynamic Posting: Uses ActionChains to manage tweet length, splitting and posting content that exceeds Twitter's character limit.
- Session Management: Ensures proper login and logout procedures, with session checks before executing tasks.

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
