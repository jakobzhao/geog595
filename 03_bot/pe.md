# Praticial Exercise 2: Twitter data collection using web crawler

**Meeting:** Wednesdays, 2:30 - 5:20, SMI 109

**Instructor:** Bo Zhao, SMI 416B, Office hours by appointment

**Contact:** 206.685.3846, zhaobo@uw.edu, jakobzhao (skype/wechat)

In this pratical exercise, we will introduce how to collect Twitter data using a web crawler. A web crawler is a purposely designed bot for online data collection. In most cases, online data can be acquired through a dedicated API maintained by the data provider. If no avaliable API, we can use a crawler library (e.g. Selenium, Scrapy, etc.) to develop a customized crawler. Below, we will develop two crawlers to harvest twitter data. The first one is made with a python library named 'Selenium'; and the other one tries to collect data from Twitter API. Okay, let us get started!

# 1. Environment setup

To setup the working environment, you will need to install Anocanda and PyCharm.

**Python:** is an interpreted, high-level, general-purpose programming language. Its language constructs and object-oriented approach aim to help programmers write clear, logical code for small and large-scale projects. Please install a python library, the version of which needs to be greater than 3.0.

Instead of installing Python, you can install  **Anaconda** - a customized python wrapper for  for scientific computing (data science, machine learning applications, large-scale data processing, predictive analytics, etc.), that aims to simplify package management and deployment. Package versions are managed by the package management system conda. The Anaconda distribution includes data-science packages suitable for Windows, Linux, and MacOS. Check https://www.anaconda.com/distribution/ to download an Anaconda package. Please make sure you choose the Python 3.X version.

**PyCharm:** is an integrated development environment (IDE) for the Python language. It is developed by the Czech company JetBrains. It provides code analysis, a graphical debugger, an integrated unit tester, integration with GitHub, and supports web development as well as Data Science with Anaconda. PyCharm is cross-platform, with Windows, macOS and Linux versions. The Community Edition is released under the Apache License, it is free to use. Check https://www.jetbrains.com/pycharm/ to download and install PyCharm.

The exercise will highly depend on your proficiency on using PyCharm, if you are not familiar with it, please walk over the following tutorials:

- [Create and run your first Python project](https://www.jetbrains.com/help/pycharm/creating-and-running-your-first-python-project.html);
- [Debug your first Python application](https://www.jetbrains.com/help/pycharm/debugging-your-first-python-application.html); and
- Skim over this tutorial on [using git on PyCharm](https://www.jetbrains.com/help/pycharm/using-git-integration.html).

# 2. Develop a generic Twitter crawler using Selenium

In this section, we will make a generic web cralwer. As a generic crawler, the same developing procedure can be applied to crawling data from any website. This crawler manipulates a browser using a python library named "Selenium". This library enables the crawler mimic how a human user visits and/or interacts with web pages. While viewing the web pages, the crawler monitors the data flows, parses the html structure, and extracts the requested data items. Below, we will introduce how to design a crawler to collect tweets of a specific topic.

Above all, please install two required python libraries, in terms of selenium and BeautifulSoup. Selenium is the library to manipulate web browser, and beautifulSoup is for destructure html pages. To install, please execute the following script on command prompt (if a windows user) or terminal (if a Mac or Linux user).

```powershell
pip install selenium
pip install beautifulsoup4
```

Once you have these two libraries installed, please try to execute the script `01_twsearch.py` under the [02_cyber folder](./) on PyCharm. We will give a step-by-step instructon of this piece of python script.



 To do so, the crawler will anchor to the Twitter search interface and input a keyword.



https://twitter.com/search?q=seattle&src=typed_query&f=live

# 3. Develop a Twitter crawler upon Twitter API


twitter search
