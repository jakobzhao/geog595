# created on April 14, 2021
# @author:          Bo Zhao
# @email:           zhaobo@uw.edu
# @website:         https://hgis.uw.edu
# @organization:    Department of Geography, University of Washington, Seattle
# @description:     A demo of collecting data from YouTube.

from selenium import webdriver
from bs4 import BeautifulSoup
import time, datetime, csv


url = "https://www.youtube.com/results?search_query=standing+rock"

# this is where you store the chromedrive. Download a chromedriver from https://chromedriver.chromium.org/downloads. Please make sure you download the right version.
bot = webdriver.Chrome(executable_path="C:\\workspace\chromedriver.exe") # if you are a mac user, please use "assets/chromedriver"
bot.get(url)

# start = datetime.datetime.now()
# time_limit = 60
i = 0

video_urls = []

f = open("assets/videos.csv", "w", newline='', encoding="utf-8") # mode a, r, w
fieldnames = ['username', 'user_url', 'title', 'view_num', 'created_at', 'video_url', 'shortdesc', 'collected_at']
writer = csv.DictWriter(f, fieldnames=fieldnames)
writer.writeheader()
# Read the Xpath tutorial if you are not familiar with XPath.
# "//" operator indicates Selects nodes in the document from the current node that match the selection no matter where they are.
while i < 3:

    soup = BeautifulSoup(bot.page_source, 'html.parser')
    videos = soup.find_all('ytd-video-renderer', class_="style-scope ytd-item-section-renderer")[-20:] # only process the newly-acquired tweets.
    # if int((datetime.datetime.now() - start).seconds) >= time_limit: # if longer than a minute, then stop scrolling.
    #     break
    for video in videos:
        try:
            video_url = video.find("a", class_="yt-simple-endpoint inline-block style-scope ytd-thumbnail").attrs["href"]
            user_url = video.find("a", class_="yt-simple-endpoint style-scope yt-formatted-string").attrs["href"]
            username = video.find("a", class_="yt-simple-endpoint style-scope yt-formatted-string").text
            title = video.find("yt-formatted-string", class_="style-scope ytd-video-renderer").text
            view_num = video.find_all("span", class_="style-scope ytd-video-meta-block")[0].text.replace(" views", "")
            created_at = video.find_all("span", class_="style-scope ytd-video-meta-block")[0].text.replace(" ago", "")
            shortdesc = video.find("yt-formatted-string", id="description-text").text
            collected_at = datetime.datetime.now()
            row = {'video_url': video_url,
                    'user_url': user_url,
                    'username': username,
                    'title': title,
                    'view_num': view_num,
                    'created_at': created_at,
                    'shortdesc': shortdesc,
                    'collected_at': collected_at}
            if video_url in video_urls:
                print("this video has already been added.")
            else:
                print(row)
                writer.writerow(row)
                video_urls.append(video_url)
        except:
            pass
    time.sleep(5)

    bot.execute_script('window.scrollTo(0,  document.getElementById("content").scrollHeight);')
    # bot.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    i += 1
f.close()
bot.close()
print("finished")

if __name__ == "__main__":
    pass
