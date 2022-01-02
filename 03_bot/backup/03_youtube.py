# created on April 14, 2021
# @author:          Bo Zhao
# @email:           zhaobo@uw.edu
# @website:         https://hgis.uw.edu
# @organization:    Department of Geography, University of Washington, Seattle
# @description:     A demo of collecting data from YouTube.

from selenium import webdriver
from bs4 import BeautifulSoup
import time, datetime, csv

# The url where the data will be collected from.
url = "https://www.youtube.com/results?search_query=standing+rock"

# A bot can automate the collecting data process. A bot will imitate how an user browse a web page, and then acqure those
# useful information. Therefore, a bot needs to control a browser. Google has released the driver to enable software
# engineerer to control a chrome application. Please download the chromedrive from https://chromedriver.chromium.org/downloads.
# Please make sure you pick the right version (the version of the latest chrome browser is 89.X). the "executable_path"
# indicates the location where you store the driver.
bot = webdriver.Chrome(executable_path="C:\\workspace\chromedriver")

# Input the targeting url to the bot, and the bot will load data from the url.
bot.get(url)

# Create a csv file to store the structured data after processing.
csvfile = open("assets/videos.csv", "w", newline='', encoding="utf-8") # mode a, r, w

# All the fields of each data entry that I want to collect.
fieldnames = ['username', 'user_url', 'title', 'view_num', 'created_at', 'video_url', 'shortdesc', 'collected_at']

# Create a writer to write the structured data to the csv file.
writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

# Write the header to the csv file
writer.writeheader()

# An array to store all the video urls.
video_urls = []


# variable i indicates the number of times that scrolls down a web page. In practice, you might want to develop different
# interaction approach to load and view the web pages.

for i in range(5):

    # Create a document object model (DOM) from the raw source of the crawled web page.
    # Since you are processing a html page, 'html.parser' is chosen.
    soup = BeautifulSoup(bot.page_source, 'html.parser')

    # Capture all the video items using find_all or findAll method.
    # To view the information of the html elements you want to collect, you need to inspect the raw source using Chrome Inspector.
    # To test whether you find the right html elements, you can use the pycharm debugger to examine the returned data.
    videos = soup.find_all('ytd-video-renderer', class_="style-scope ytd-item-section-renderer")[-20:] # 20 indicates only process the newly-acquired 20 entries.

    # iterate and process each video entry.
    for video in videos:

        # I prefer use the "try-except" statement to enable the program run without pausing due to unexecpted errors.
        try:
            video_url = video.find("a", class_="yt-simple-endpoint inline-block style-scope ytd-thumbnail").attrs["href"]
            user_url = video.find("a", class_="yt-simple-endpoint style-scope yt-formatted-string").attrs["href"]
            username = video.find("a", class_="yt-simple-endpoint style-scope yt-formatted-string").text
            title = video.find("yt-formatted-string", class_="style-scope ytd-video-renderer").text
            view_num = video.find_all("span", class_="style-scope ytd-video-meta-block")[0].text.replace(" views", "")
            created_at = video.find_all("span", class_="style-scope ytd-video-meta-block")[0].text.replace(" ago", "")
            shortdesc = video.find("yt-formatted-string", id="description-text").text
            collected_at = datetime.datetime.now()

            # create a row in the dict format.
            row = {'video_url': video_url,
                    'user_url': user_url,
                    'username': username,
                    'title': title,
                    'view_num': view_num,
                    'created_at': created_at,
                    'shortdesc': shortdesc,
                    'collected_at': collected_at}

            # if a video has been added to the csvfile, this video would not be inserted to the csv file,
            # otherwise, this video will be inserted.
            if video_url in video_urls:
                print("this video has already been added.")
            else:
                print(row)
                writer.writerow(row)

                # add the video_url to the video_urls array.
                video_urls.append(video_url)
        except:
            pass

    # it is very important to enable the bot take some rest, and then resume to work.
    time.sleep(5)

    # Let the bot scrolls down to the bottom of the content element, most of the time the bot needs to scroll down to the bottom of the page.
    # like this statement: bot.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    bot.execute_script('window.scrollTo(0,  document.getElementById("content").scrollHeight);')

# close the csvfile object and the bot object.
csvfile.close()
bot.close()

# notify the completion of the program in the console.
print("finished")
