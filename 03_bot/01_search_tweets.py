# created on Dec 24, 2020
# @author:          Bo Zhao
# @email:           zhaobo@uw.edu
# @website:         https://hgis.uw.edu
# @organization:    Department of Geography, University of Washington, Seattle
# @description:     making a web crawler to search tweets on a specific topic

from selenium import webdriver
from bs4 import BeautifulSoup
import time, datetime, json


# url = "https://twitter.com/search?l=&q=near%3A%22houston%22%20within%3A15mi%20since%3A2017-08-24%20until%3A2017-08-31&src=typd&lang=en"  #crawlling all the tweets posted near Houston during the Hurricane Harvey attacked period.
url = "https://twitter.com/search?l=&q=seattle&src=typd&lang=en"
# use a chrome browser core. https://chromedriver.chromium.org/downloads
browser = webdriver.Chrome(executable_path="assets/chromedriver.exe") # if you are a mac user, please use "assets/chromedriver"
browser.get(url)


time.sleep(8)
start = datetime.datetime.now()
while len(browser.find_elements_by_xpath('//div[contains(text(), "Back to top ↑")]')) != 1:
    time.sleep(5)
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    soup = BeautifulSoup(browser.page_source, 'html5lib')
    items = soup.find_all('li', class_="stream-item")[-20:]

    # if longer than a hour, then stop scrolling.
    if int((datetime.datetime.now() - start).seconds / 60) > 60:
        break

    for item in items:
        try:
            user_json = json.loads(item.div.attrs["data-reply-to-users-json"])
            user_id = int(user_json[0]['id_str'])
            user_name = user_json[0]['screen_name']
            screen_name = user_json[0]['name']
            status_id = int(item.attrs["data-item-id"])

            content = item.find("p").text
            created_at = item.find("small", class_="time").a.attrs["title"]
            time_integer = item.find("small", class_="time").a.span["data-time-ms"]
            reply_num = item.find("div", class_="ProfileTweet-action--reply").find("span", class_="ProfileTweet-actionCountForPresentation").text
            retweet_num = item.find("div", class_="ProfileTweet-action--retweet").find("span", class_="ProfileTweet-actionCountForPresentation").text
            favorite_num = item.find("div", class_="ProfileTweet-action--favorite").find("span", class_="ProfileTweet-actionCountForPresentation").text

            inst_url = ""
            if "www.instagram.com" in content:
                inst_url = item.p.a.attrs["title"]
        except:
            pass

        print(user_id, user_name, screen_name, status_id, content, created_at, time_integer, reply_num, retweet_num, favorite_num)

        page_json = {
            "user_id": user_id,
            "user_name": user_name,
            "screen_name": screen_name,
            "status_id": status_id,
            "content": content,
            "inst_url": inst_url,
            "created_at": created_at,
            "time_integer": time_integer,
            "reply_num": reply_num,
            "retweet_num": retweet_num,
            "favorite_num": favorite_num
        }
        # try:
        #     db.tweets.insert_one(page_json)
        # except errors.DuplicateKeyError:
        #     print('This post has already been inserted.')


browser.close()
print("finished")