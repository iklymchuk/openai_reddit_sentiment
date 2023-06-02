## Identify the sentiment of top reddit posts by subject with OpenAI

 - **Init setup:** `make install`

 - **Configure a service for schedule execution:**
      1. `service.py` setup the schedule
      2. `reddit.service` update the `ExecStart` and `WorkingDirectory` with respective path to python and service.py
      3. `sudo cp reddit.service /etc/systemd/system`
      4. `sudo systemctl enable reddit.service`
      5. `sudo systemctl restart reddit.service`
      6. `systemctl status reddit.service` check the status of the service

 - **Test for a single execution:**
      1. execute `main.py -t` where `-t` is the subject for quering

 - **Result will be sent to the telegram:**
<img width="745" alt="Screenshot 2023-06-02 at 14 22 02" src="https://github.com/iklymchuk/openai_reddit_sentiment/assets/5702058/ed1fe9c5-cd10-4934-b5fd-907fac123e5e">

