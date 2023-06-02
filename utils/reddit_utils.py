import os
import praw

from dotenv import load_dotenv

load_dotenv()

reddit = praw.Reddit(
    client_id=os.getenv("REDDIT_ID"),
    client_secret=os.getenv("REDDIT_SECRET"),
    user_agent="sentiment test",
)


# we can skip 2 first posts because it always are pinned posts
def get_titles_and_comments(subreddit="stocks", limit=7, num_comments=5, skip_first=2):
    subreddit = reddit.subreddit(subreddit)
    title_and_comments = {}

    for counter, post in enumerate(subreddit.hot(limit=limit)):
        if counter < skip_first:
            continue
        counter += 1 - skip_first

        title_and_comments[counter] = ""

        submission = reddit.submission(post.id)
        title = post.title

        title_and_comments[counter] += "Title: " + title + "\n\n"
        title_and_comments[counter] += "Comments: \n\n"

        comment_counter = 0
        for comment in submission.comments:
            if not comment.body == "[deleted]":
                title_and_comments[counter] += comment.body + "\n"
                comment_counter += 1
            if comment_counter == num_comments:
                break
    return title_and_comments
