#!/usr/bin/env python
# coding: utf-8

# In[10]:


from selenium import webdriver
path = "C:\Program Files\chromedriver.exe"  # state the chromedriver path 

driver = webdriver.Chrome(path) '''we are stating the path  where chromedriver.exe is present 
which the webdriver can use to  perform operations on chrome '''

driver.get("https://selenium-python.readthedocs.io/")
    


# In[8]:


from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time
option = webdriver.ChromeOptions()
#option.headless = True


driver_path  = "C:\Program Files\chromedriver.exe"  # state the chromedriver path 
driver = webdriver.Chrome(driver_path,options = option)

DOWNLOAD_URL = "https://mp3offline.org/"
#aded
#d\aded
driver.get(DOWNLOAD_URL)



search = driver.find_element_by_id('input')
search.clear()
search.send_keys("https://www.youtube.com/watch?v=P-3GOo_nWoc")
search.send_keys(Keys.RETURN)
time.sleep(5)
    


try:

    driver.switch_to.window(driver.window_handles[1]) # be careful this might change in future
    driver.close()
    driver.switch_to.window(driver.window_handles[0])
    
    wait = WebDriverWait(driver, 10,poll_frequency = 2)
    content = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "btr-320")))
    
    content.click()  

    name = driver.title
    check(name)
finally:
    driver.quit()


# In[7]:


import os
import os.path as op
def check(name):
    
    title = change(name)+".mp3"
    title = title.replace('"','')
    os.chdir(r"C:\Users\user\Downloads")
    while op.exists(title) == False:
        pass
    print("completed downloading")
        
#check(name)   


# In[45]:


t = 'Joseph Joestar "Oh No" and "Oh My God" Compilation.mp3'
q = t.replace('"','')
q,t


# In[6]:


def change(x):
    x = x.lstrip("Download")
    x = x.strip("MP3")
    x = x.rstrip()
    title = x.lstrip()
    return title


# In[7]:


content = driver.find_element_by_class_name('btr-320')
content.click()


# In[1]:



from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os
import time
# function to take care of downloading file
def enable_download_headless(browser,download_dir):
    browser.command_executor._commands["send_command"] = ("POST", '/session/$sessionId/chromium/send_command')
    params = {'cmd':'Page.setDownloadBehavior', 'params': {'behavior': 'allow', 'downloadPath': download_dir}}
    browser.execute("send_command", params)

# instantiate a chrome options object so you can set the size and headless preference
# some of these chrome options might be uncessary but I just used a boilerplate
# change the <path_to_download_default_directory> to whatever your default download folder is located
chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--window-size=1920x1080")
chrome_options.add_argument("--disable-notifications")
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--verbose')
chrome_options.add_experimental_option("prefs", {
        "download.default_directory": "C:\\Users\\user\\Downloads",
        "download.prompt_for_download": False,
        "download.directory_upgrade": True,
        "safebrowsing_for_trusted_sources_enabled": False,
        "safebrowsing.enabled": False
})
chrome_options.add_argument('--disable-gpu')
chrome_options.add_argument('--disable-software-rasterizer')

# initialize driver object and change the <path_to_chrome_driver> depending on your directory where your chromedriver should be
driver = webdriver.Chrome(chrome_options=chrome_options, executable_path="C:\Program Files\chromedriver.exe")

# change the <path_to_place_downloaded_file> to your directory where you would like to place the downloaded file
download_dir = "C:\\Users\\user\\Downloads"

# function to handle setting up headless download
enable_download_headless(driver, download_dir)

# get request to target the site selenium is active on
driver.get("https://mp3offline.org/3LRTUrl3A4U")

# initialize an object to the location on the html page and click on it to download
search_input =  driver.find_element_by_class_name('btr-320')
search_input.click()
time.sleep(300)

