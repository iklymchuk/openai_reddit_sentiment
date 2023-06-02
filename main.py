import os
import openai
import argparse

from utils import reddit_utils, openai_utils, telegram_utils
from dotenv import load_dotenv

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")

argParser = argparse.ArgumentParser()
argParser.add_argument("-t", "--theme", help="Theme for subreddit. Ex. stocks")
args = argParser.parse_args()


def send_posts_info():
    title_and_comments = reddit_utils.get_titles_and_comments(subreddit=args.theme)
    result = openai_utils.sentiment_from_openai(title_and_comments)
    telegram_utils.send_telegram_message(result)


if __name__ == "__main__":
    send_posts_info()
