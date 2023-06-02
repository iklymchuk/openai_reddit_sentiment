import openai
from datetime import datetime


def create_prompt(title_and_comments):
    task = "Return the sentiment based on Title and Comments as positive, negative or neutral. And if it possible indicate the company name or ticker in the format: Sentiment: {sentiment} for {ticker}'\n\n"
    return task + title_and_comments


def sentiment_from_openai(title_and_comments):
    t = datetime.now().strftime("%B %d, %Y %H:%M:%S")
    result_response = (
        "<u><b>Top reddit posts by subject for " + t + "</b></u>" + "\n\n"
    )
    for key, post in title_and_comments.items():
        prompt = create_prompt(post)
        post_title = post.split("\n")[0]

        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=prompt,
            max_tokens=256,
            temperature=0,
            top_p=1.0,
        )

        result_response += "<b>" + str(key) + ":</b> "
        result_response += (
            "<b>"
            + post_title
            + "</b>"
            + " "
            + "<code>"
            + response["choices"][0]["text"]
            + "</code>"
            + "\n"
        )

    return result_response
