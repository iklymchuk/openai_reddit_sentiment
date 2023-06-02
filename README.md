## Identify the sentiment of top reddit posts by subject with OpenAI

Setup: `make install`

 - **Configure a service for schedule execution:**
      1. `service.py` setup the schedule
      2. `reddit.service` update the `ExecStart` and `WorkingDirectory` with respective path

 - **Test for a single execution:**
      1. execute `main.py -t` where `-t` is the subject for quering

Result will be sent to the telegram:

![IMG_2328](https://github.com/iklymchuk/openai_reddit_sentiment/assets/5702058/c9f67582-2206-4be2-9c61-ccd5463c8f6c)
