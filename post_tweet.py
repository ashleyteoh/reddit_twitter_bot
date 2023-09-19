import os
from twitter_bot_class import TwitterBot
import pandas as pd
import time

def get_post():
    try:
        df = pd.read_csv("hot_posts.csv")
    except Exception as e:
        pj.logout()
        print(e)

    post_content = df.head(1)
    
    if post_content.loc[:, 'body'].isnull().values.any():
        body = ""
    else:
        body = (post_content.loc[:, 'body']).values[0] + "\n\n"
    
    twitter_post = post_content.loc[:, 'title'].values[0] + "\n\n" \
        + body \
        + str(post_content.loc[:, 'score'].values[0]) + " upvotes, " \
        + str(post_content.loc[:, 'num_comments'].values[0]) + " comments\n\n" \
        + post_content.loc[:, 'url'].values[0] 
    
    return twitter_post, df

if __name__ == "__main__":

    os.environ['EMAIL'] = ""
    os.environ['PASSWORD'] = ""

    try:
        pj = TwitterBot(os.environ['EMAIL'], os.environ['PASSWORD'])
        pj.login()
        post, df = get_post()
        pj.post_tweets(post)

        df = df.iloc[1:] # delete first row after posting
        df.to_csv("hot_posts.csv", index=False)
        time.sleep(4)

        pj.logout()
    except Exception as e:
        pj.logout()
        print(e)

