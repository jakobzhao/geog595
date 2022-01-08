# Practical Exercise 2: Data collection using web crawler

**Instructor:** Bo Zhao, zhaobo@uw.edu; **Points Available** = 50

In this practical exercise, we will introduce how to collect Twitter data using a web crawler. A web crawler is a purposely designed bot for online data collection. In most cases, online data can be acquired through a dedicated API maintained by the data provider. If no API available, we can develop a customized crawler using a crawler library (e.g. Selenium, Scrapy, etc.). So, in this practical exercise, we will design two crawlers, one is a generic crawler to harvest data from youtube, and the other is to harvest data from Twitter API. Okay, let us get started!

## 1. Setup the Execution Environment on the Cloud

If you have used python for scientific research before, you must already experience the complexity of configuring the execution environment. So, in order not to bother by the environment configuration, we decide to execute the crawlers on Google Colab, which allows anybody to write and execute arbitrary python code through the browser, and is especially well suited to machine learning, data analysis and education. t is a hosted Jupyter notebook that requires no setup and has an excellent free version, which gives free access to Google computing resources such as GPUs and TPUs.

## 2. Develop a generic Twitter crawler using Selenium

This section will help you make a generic web crawler. If you are able to develop this generic crawler, the same developing procedure can be applied to crawling data from other websites. This crawler manipulates a browser using a python library named "Selenium". This library enables the crawler mimic how a human user visits and/or interacts with web pages. While viewing the web pages, the crawler monitors the data flows, parses the html structure, and extracts the requested data items. Below, we will introduce how to design a crawler to collect information from a group of youtube videos.

You can launch the youtube crawler by click this button. This button will enable you to open the file [03_bot/youtube.ipynb](03_bot/youtube.ipynb) on Google Colab.

For any python script, metadata are usually stated at the very beginning.

```python
# created on April 14, 2021
# modified on Jan 2, 2022
# @author:          Bo Zhao
# @email:           zhaobo@uw.edu
# @website:         https://hgis.uw.edu
# @organization:    Department of Geography, University of Washington, Seattle
# @description:     A demo of collecting data from YouTube.
```

To support Selenium, you will need to install a library named Kora, which is a collection of tools to make programming on Google Colab easier.

```Python
# Installing Kora to the remote google colab server. Kora is a collection of tools to make programming on Google Colab easier.
!pip install kora -q
```

the required python libraries for this crawler will be included. To execute the crawling task, we will use BeautifulSoup, time, datetime, csv, pandas and selenium. Since Google Colab has already pre-installed BeautifulSoup, time, datetime, csv, pandas, you do not need to install them.

```Python
from bs4 import BeautifulSoup
import time, datetime
import pandas as pd
# A bot can automate the collecting data process. A bot will imitate how an user browse a web page, and then acquire those useful information.
# For more information about how to operate a bot, please refer to the documentation of Selenium at https://selenium-python.readthedocs.io/
from kora.selenium import wd as bot
```

We plan to order the youtube crawler harvest the information of videos relevant to a keyword "Standing Rock". By studying how to search youtube videos using keyword, we find out that the expected videos can be visited by the url `https://www.youtube.com/results?search_query=standing+rock`. So a variable url is created to store the url. And next, we will use the bot to visit this url.

```Python
# The url where the data will be collected from.
url = "https://www.youtube.com/results?search_query=standing+rock"
# Input the targeting url to the bot, and the bot will load data from the url.
bot.get(url)
```

Declare global variables and assign initial values.

```Python
# An array to store all the video urls. If a video has been crawled, it would not be stored to the data frame.
video_urls = []
# An array to store the retrieved video details.
results = []
```

In order to harvest the information from the videos on the visited web page, you need to keep scrolling down the page, you can stop till the bottom of the page or determine how many times you want to operate the scroll on page behavior. For each scroll, please ask your bot take some rest, and then resume to work.

```Python

# variable i indicates the number of times that scrolls down a web page. In practice, you might want to develop different
# interaction approach to load and view the web pages.

for i in range(5):
    ... ...
    ... ...
    ... ...
    # it is very important to enable the bot take some rest, and then resume to work.
    time.sleep(5)
    # Let the bot scrolls down to the bottom of the content element, most of the time the bot needs to scroll down to the bottom of the page.
    # like this statement: bot.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    bot.execute_script('window.scrollTo(0,  document.getElementById("content").scrollHeight);')
```

In each scroll, the crawler will only parse the newly appeared videos. So, based on the testing, we find that each scroll will retrieve no more than 20 videos. To develop the locating strategy, we can use Chrome's Inspector to visually explore the elements of the opened web page and its corresponding source code.

In the inspector, you can find the HTML features of each video. For example, we find that the tag name of a video element is `ytd-video-renderer`, and each video element is also in the class of  `style-scope ytd-item-section-renderer`.

**Note:** To open an inspector on Chrome, you can right click on the displaying web page. On the pop-up dropdown menu, click `Inspect`, and then the inspector will show up.

To locate a certain attribute of HTML element, you will need to use the syntax of beautiful soup. Beautiful Soup is also very important for destructuring html pages.Beautiful Soup is a Python library for pulling data out of HTML and XML files. It provides idiomatic ways of navigating, searching, and modifying the parse tree. If you are not familiar with Beautiful Soup, please go over the [`Quick Start` section of this documentation](https://www.crummy.com/software/BeautifulSoup/bs4/doc/#quick-start).

```Python
# Create a document object model (DOM) from the raw source of the crawled web page.
# Since you are processing a html page, 'html.parser' is chosen.
soup = BeautifulSoup(bot.page_source, 'html.parser')

# Capture all the video items using find_all or findAll method.
# To view the information of the html elements you want to collect, you need to inspect the raw source using Chrome Inspector.
videos = soup.find_all('ytd-video-renderer', class_="style-scope ytd-item-section-renderer")[-20:] # 20 indicates only process the newly-acquired 20 entries.
```

Then, you will process each video in the video list. I prefer use the "try-except" statement to enable the program run without pausing due to unexpected errors.

```python
for video in videos:

    # I prefer use the "try-except" statement to enable the program run without pausing due to unexpected errors.
    try:
        ... ...
        ... ...
    except:
        pass
```

For each video, we will extract the needed attributes, such as the video url, user url, username, title, number of views, the time when the video was created, short desc of the video, and when the video record was collected by the crawller.

```python
video_url = video.find("a", class_="yt-simple-endpoint inline-block style-scope ytd-thumbnail").attrs["href"]
user_url = video.find("a", class_="yt-simple-endpoint style-scope yt-formatted-string").attrs["href"]
username = video.find("a", class_="yt-simple-endpoint style-scope yt-formatted-string").text
title = video.find("yt-formatted-string", class_="style-scope ytd-video-renderer").text
view_num = video.find_all("span", class_="style-scope ytd-video-meta-block")[0].text.replace(" views", "")
created_at = video.find_all("span", class_="style-scope ytd-video-meta-block")[0].text.replace(" ago", "")
shortdesc = video.find("yt-formatted-string", id="description-text").text
collected_at = datetime.datetime.now()
```

Once the attributes are collected, you will create a row in the dict format. And append this newly acquired row to the results array

```python
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
    results.append(row)
```

To the end, you can terminate the bot when the task is completed

```python
# terminate the bot object.
bot.close()
```

Store the results as a pandas dataframe.

```python
# Store the results as a pandas dataframe
df = pd.DataFrame(results)

# notify the completion of the crawling in the console.
print("the crawling task is finished.")
```

Since the script is executed on Google Colab, we will store the data as a csv spreadsheet directly in Google Drive.

```python
# Create data on to Google Drive
from google.colab import drive
# Mount your Drive to the Colab VM.
drive.mount('/gdrive')

# the file path where to store the output csv on google drive
output_file = '/gdrive/My Drive/videos.csv'

# Save the dataframe as a csv file
df.to_csv(output_file, index=False)
```

When the csv is created successfully, you can download the csv file to your local computer.

```python
# download the csv to your local computer
from google.colab import files
files.download(output_file)
print("the csv has been downloaded to your local computer. The program has been completed successfully.")
```

![](img/tweet-csv.png)

## 3. Harvest geo-tagged tweets using a API-based Crawler

### 3.1 prerequisite libraries and Twitter developer token

In this section, we will make a Twitter crawler to collect geotagged tweets. This crawler is based on `Tweepy` - a python based library which wraps the Twitter API. Tweepy provides a series of data crawling strategies - Harvesting geotagged tweets is just one of them. If you are interested in composing a more complicated data collection strategy, please refer to its documentation at <https://tweepy.readthedocs.io/en/latest/index.html>.

If you want to use tweepy in your local computer, you need to install tweepy using on command prompt (if a windows user) or terminal (if a Mac or Linux user), as shown in the script below.

```powershell
pip install tweepy
```

> note: if you work on a Jupyter Notebook such as mybinder.org, we run the following code, as shown in the script below, to install a library.

```powershell
!python -m pip install tweepy
```

Although we also work on the Jupyter Notebook, we do not need to manually install tweepy because Google Colab has automatically incorporate it into its preloaded libraries.

To use the tweepy library, you need to register a Twitter developer account [here](https://developer.twitter.com/en/apply-for-access).

![](img/twitter_dev.png)

In order to register your account, you will be prompted to answer a series of questions. Please answer those that are required to fill in and you can ignore optional questions. Once you finish registering your account, you can apply for a Twitter app. First of all, you will need to click on `Developer Portal` which is located on the top right corner of the page.

![](img/dev_acc.png)

Then, you will enter developer portal. On the left bar, you can click on `Projects &  Apps` for checking the list of apps that you've created for getting Twitter API, but for now, the list should be empty. In order to register for Twitter API, click on `+ Create App` which is under the `Standalone Apps`.

![](img/creat_app.png)

You will be prompted to fill in the app details. Here, you are required to fill in: `App name`.

![](img/app_details.png)

After you fill in all the required fields, you may click on `Create`. Twitter takes some time to process your information to validate your access to the Twitter API. Then you will be able to see your keys and tokens.

Once you are registered, you could check your own keys and tokens again by click on your app-name which is under your app list. Go to the `App Detail` of the app you just created. Click on the tab `Keys and tokens`, and you should be able to see all the keys and tokens required to use the Twitter API.

![](img/app_keys.png)


## 3.2 Initiating the API object

As usual, we will import the needed libraries

```python
import tweepy
import pandas as pd
```

Copy and paste the keys and tokens you received into corresponding parameters in the code below:

```Python
consumer_key = "your_consumer_key"
consumer_secret = "your_consumer_secret"
access_token = "your_access_token"
access_token_secret = "your_access_token_secret"
```

Initiate a tweepy API object

```python
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, wait_on_rate_limit=True)
```

Define the search term and the date_since date as variables. We will harvest all the tweets that contains the keyword "#BLM". Also, the tweets must be sent in Capitol Hill at Seattle and since October 16th, 2020.

```python
search_words = "#BLM"
location = "47.6138893,-122.3107869,100mi"
date_since = "2020-10-16"
```

## 3.3 Data Harvest

Then, we input the parameters to the tweepy harvesting cursor, and we want to get back at most 1000 tweets for one single query.

```python
# Collect tweets
tweets = tweepy.Cursor(api.search, q=search_words, geocode=location, lang="en", since=date_since).items(1000)
```

We first create an empty array to store the retrieved data. As how we process each video in the first crawler we designed, we use the similar strategy to process each tweet, and store them in a pandas data frame.

```python
# create an array to store the result
result = []

# Iterate and print tweets
for tweet in tweets:
    row = {
        'username': tweet.author.name,
        'userid': tweet.author.id,
        'profile_location': tweet.author.location,
        'created_at': str(tweet.author.created_at),
        'text': tweet.text,
        'retweet_count': tweet.retweet_count,
        'source': tweet.source,
        'coordinates': tweet.coordinates
    }
    result.append(row)
    print(row)

# Store the results as a pandas dataframe
df = pd.DataFrame(result)

# notify the completion of the crawling in the console.
print("the crawling task is finished.")
```

In the end, we can store the tweets as a csv file to Google drive or download to the local computer.

```python
# Create data on to Google Drive
from google.colab import drive
# Mount your Drive to the Colab VM.
drive.mount('/gdrive')
  
df.to_csv(output_file, index=False)


# download the csv to your local computer
from google.colab import files
files.download(output_file)
print("the csv has been downloaded to your local computer. The program has been completed successfully.")
```
```

To retrieve geo-tagged tweets, three bounding boxes are defined. After initializing the stream listener, a stream object is created out of `tweepy.Stream object`. Then, the LOCATION array is passed to the stream filter method. By doing so, the geo-tagged are filtered and collected.

```Python
LOCATIONS = [-124.7771694, 24.520833, -66.947028, 49.384472,  # Contiguous US
               -164.639405, 58.806859, -144.152365, 71.76871,  # Alaska
               -160.161542, 18.776344, -154.641396, 22.878623]  # Hawaii
stream_listener = StreamListener(time_limit=60, file=output_file)
stream = tweepy.Stream(auth=myauth, listener=stream_listener)
stream.filter(locations=LOCATIONS)
```

Notably, the filter not only acquires geotagged tweets but also other kinds of tweets according to the input filter strategy.
tweepy allows you to filter tweets through a keyword. By choosing a keyword related to the timely topic like "coronavirus", you can obtain data that gives you an insight into the public perception of the topic.

```python
stream.filter(track=['coronavirus'], is_async=True)
```

Additionally, to use filters to stream tweets by a specific user. The following parameter is an array of IDs. For example, the Twitter ID for the white house is `822215673812119553`, and you can collect tweets from this specific account. We will not be changing this parameter in this lab exercise, but consider how you can utilize this function if this is something that you would like to link to your final project.

```python
stream.filter(follow=["2211149702"])
```

However, these different filtering parameter returns different data structures, and they store different information about the tweets. For this reason, keyword filtering does not return plenty of geotagged tweets. If you are changing the keyword parameter, you should run this crawler for a longer duration. To do so, simply change the `time_limit` parameter. For example, if you want to run this crawler for 5 minutes, set it to 300. If you are trying to use a less common keyword, the chance is you will not have a sufficient amount of data. In that case, consider running this crawler for even longer.

```python
stream_listener = StreamListener(time_limit=60, file=output_file)
```

The `on_data` function will handle data processing and output. In general, this function terminated after `self.limit` second. To process each record `data`, the captured `data` is converted to a JSON variable `datajson`. We will mainly output six variables, in terms of id, username, created_at, lng, lat, and text. Notably, If the geotag is a single point, the lat and lng will be captured directly from the `coordinates`. If the geotag is a place, the lat and lng will capture the centroid of the bounding box. Similarity, a new CSV file named `tweets.csv` is created under [the assets folder](assets/).

In a lot of actual work environments, it is common to use a database to store information. We are using CSV files as data storage to simplify our tasks. If you would like to know more about using a database to store information, you can learn more [here](https://github.com/jakobzhao/geog458/blob/master/labs/lab02/database/pe.md).

```Python
def on_data(self, data):
    """This is called when data are streamed in."""
    if (time.time() - self.start_time) < self.limit:
        datajson = json.loads(data)
        print (datajson)
        id = datajson['id']
        username = datajson['user']['screen_name']
        created_at = datajson['created_at']
        text = datajson['text'].strip().replace("\n", "")

        # process the geo-tags
        if datajson['coordinates'] == None:
            bbox = datajson['place']['bounding_box']['coordinates'][0]
            lng = (bbox[0][0] + bbox[2][0]) / 2.0
            lat = (bbox[0][1] + bbox[1][1]) / 2.0
        else:
            lng = datajson['coordinates']['coordinates'][0]
            lat = datajson['coordinates']['coordinates'][1]

        record = '%d, %s, %s, %f, %f, %s \n' % (id, username, created_at, lng, lat, text)
        print (record)
        self.f.write(record)
    else:
        self.f.close()
        print ("finished.")
        return False
```

In addition to run the crawler script [02_geosearch.py](02_geosearch.py) on pycharm, you can also run the python notebook version on an online Jupyter server Binder.org. Click the button to launch the Binder Server. [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/jakobzhao/geog595.git/master?filepath=03_bot%2F02_geosearch.ipynb). The instructor will show you how to run it on binder in class.

> Besides, you can run the script 04_geosearch.py on Binder by clicking this [link](https://mybinder.org/v2/gh/jakobzhao/geog595.git/master?filepath=03_bot%2F04_geosearch.ipynb).

## 4. Deliverable

You are expected to walk through this instruction, execute the two pieces of python scripts, and more importantly, develop your own crawler to collect some data from the web. Ideally, this data will be related to research question you have stated in your [statement of intent](../01_intro/soi.md).

To submit your deliverable, please create a new github repository, and submit the url of the GitHub to the **Canvas Dropbox** of this practical exercise. The file structure of this github repository should look like below.

```powershell
[your_repository]
    │ [your_crawler].py
    │readme.md
    ├─assets
    │      tweets.csv
    │      geotags.csv
    │      [your_dataset].csv
```

Here are the grading criteria:

1\. Execute both `youtube.py` and `tweets.py` with different keywords, and save the results to `videos.csv` and `tweets.csv` in the `assets` folder of the newly-created repository. (POINT 5 for each)

2\. Develop a web crawler to harvest data from a website other than Youtube. This python script should save in the root of the repository. (POINT 20)

3\. Export a sample of the results to the `assets` folder of the repository. (POINT 5)

4\. In the `readme.md` file, write an instruction to introduce the crawler and its usages. You can refer to  [https://github.com/shawn-terryah/Twitter_Geolocation](https://github.com/shawn-terryah/Twitter_Geolocation). (POINT 15)


**Note:** Lab assignments are required to be submitted electronically to Canvas unless stated otherwise. Efforts will be made to have them graded and returned within one week after they are submitted.Lab assignments are expected to be completed by the due date. ***A late penalty of at least 10 percentage units will be taken off each day after the due date.*** If you have a genuine reason(known medical condition, a pile-up of due assignments on other courses, ROTC,athletics teams, job interview, religious obligations etc.) for being unable to complete work on time, then some flexibility is possible. However, if in my judgment you could reasonably have let me know beforehand that there would likely be a delay, and then a late penalty will still be imposed if I don't hear from you until after the deadline has passed. For unforeseeable problems,I can be more flexible. If there are ongoing medical, personal, or other issues that are likely to affect your work all semester, then please arrange to see me to discuss the situation. There will be NO make-up exams except for circumstances like those above.