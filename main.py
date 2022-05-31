# from pydoc_data.topics import topics
# from typing import List
import requests
# from urllib.request import urlopen
from configparser import ConfigParser
import json
import requests

WEB_HOOK_LIST = [f"https://hooks.slack.com/services/TFF0B1TDG/{}/{}",f"https://hooks.slack.com/services/TFF0B1TDG/{}/{}",f"https://hooks.slack.com/services/TFF0B1TDG/{}/{}",f"https://hooks.slack.com/services/TFF0B1TDG/{}/{}",f"https://hooks.slack.com/services/TFF0B1TDG/{}/{}",f"https://hooks.slack.com/services/TFF0B1TDG/{}/{}",f"https://hooks.slack.com/services/TFF0B1TDG/{}/{}"]


# Read config file
config = ConfigParser()

config.read('config.ini')

def notify_channel(web_hook):
    text={'text': "\n Hello! :wave: It's time for the: <https://form.typeform.com/to/mDeJ1mNM|*instructor monthly survey*> \n Please, help us to improve. :muscle: It's only 3 minutes and completely anonymous.\n  "}
    requests.post(web_hook, data=json.dumps(text))       


if __name__ == "__main__":
  for web_hook in WEB_HOOK_ADMIN:
    notify_channel(web_hook)     
