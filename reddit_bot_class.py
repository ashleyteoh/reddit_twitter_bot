import pandas as pd
import praw
import requests
import cv2
import numpy as np
import os

def get_hot_reddit_posts(sub_name):
    # Define user agent
    user_agent = "praw_scraper_7.7.1"

    # Create an instance of reddit class
    reddit = praw.Reddit(client_id="",
                        client_secret="",
                        user_agent=user_agent
    )

    subreddit = reddit.subreddit(sub_name)

    posts = []
    hot_posts = subreddit.hot(limit=10)

    # dir_path = os.path.dirname(os.path.realpath(__file__))
    # image_path = os.path.join(dir_path, "images/")

    # count = 0
    for post in hot_posts:
        # check if post has an image, download if yes
        # image_name = ""
        # if "jpg" in post.url.lower() or "png" in post.url.lower():
        #     try:
        #         resp = requests.get(post.url.lower(), stream=True).raw
        #         image = np.asarray(bytearray(resp.read()), dtype="uint8")
        #         image = cv2.imdecode(image, cv2.IMREAD_COLOR)

        #         image_name = f"{image_path}HK-{count}.png" 
        #         cv2.imwrite(image_name, image)
                    
        #     except Exception as e:
        #         print(f"Image failed. {post.url.lower()}")
        #         print(e)

        url = "https://www.reddit.com" + post.permalink
        posts.append([post.title, post.score, post.id, url, post.num_comments, post.selftext, post.created])
        # count += 1

    posts = pd.DataFrame(posts,columns=['title', 'score', 'id', 'url', 'num_comments', 'body', 'created'])

    posts.to_csv("hot_posts.csv")


if __name__ == "__main__":
    get_hot_reddit_posts("ExplainLikeImFive")