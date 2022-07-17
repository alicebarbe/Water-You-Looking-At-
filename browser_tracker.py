# -*- coding: utf-8 -*-
"""
Created on Sat Jul 16 09:25:54 2022

@author: Alice
"""

import time
import praw
import warnings
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from click_window import send_raspi_command, init_windows

warnings.filterwarnings("ignore")

driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))

reddit = praw.Reddit(
    client_id="nY8T3GBnoXla6VgUrRlSpA",
    client_secret="CjUzxomzY0PhMRyiP8UlzA3GuUHs1Q",
    user_agent="water_you_looking_at",
    check_for_async=False
)

current_url = "https://www.reddit.com"
driver.get(current_url)  # direct user to start url
lookup_strings = ["r/eyebleach", "r/cursedimages"]

start_time = time.time()

terminal_window, firefox_window = init_windows()
print("Start redditing")
#while time.time() - start_time < 60:
while True:
    # if website has changed
    if current_url != driver.current_url:
        current_url = driver.current_url
        print(str(current_url))
        try:
            submission = reddit.submission(url=current_url)
            for comment in submission.comments:
                if type(comment) == praw.models.reddit.comment.Comment:
                    if any(lookup in comment.body for lookup in lookup_strings):
                        print("AHHHHH")
                        send_raspi_command(terminal_window, firefox_window)
        except:  # user is not in a reddit thread yet
            print("You are not yet in a reddit thread")
        time.sleep(1)
    else:
        time.sleep(1)
