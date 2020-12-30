
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os
import os.path as op
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip
import glob
class download:
    def __init__(self):
        self.links = []
        self.edits = []
        self.edit_req = True
        while 1:
            temp = input()
            if len(temp) == 0:
                break
            temp = temp.split()
            self.links.append(temp[0])
            self.edits.append((temp[1],temp[2]))
        
    def web_scrape(self):
        option = webdriver.ChromeOptions()
        driver_path = "C:\Program Files\chromedriver.exe"  # state the chromedriver path
        driver = webdriver.Chrome(driver_path, options=option)

        DOWNLOAD_URL = "https://mp3offline.org/"
        driver.get(DOWNLOAD_URL)
        os.chdir(r"C:\Users\user\Downloads")

        for i,j in zip(self.links,self.edits):
            search = driver.find_element_by_id('input')
            search.clear()
            search.send_keys(i)
            search.send_keys(Keys.RETURN)

            try:
                driver.switch_to.window(driver.window_handles[1])  # be careful this might change in future
                driver.close()
                driver.switch_to.window(driver.window_handles[0])
            except Exception :
                pass

            try:
                wait = WebDriverWait(driver, 10, poll_frequency=2)
                content = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "btr-320")))
                content.click()
                initial = glob.glob("*.mp3")
                while len(initial) == len(glob.glob("*.mp3")):
                    pass
                driver.execute_script("window.history.go(-1)")
                if self.edit_req == True:
                    self.edit(self.time_change(j[0]),self.time_change(j[1]))                
            except Exception:
                driver.quit()
                driver.get(DOWNLOAD_URL)

        driver.quit()
    def time_change(self,x):
        q = [int(i) for i in x.split(":")]
        time = 0
        val = 1
        for i in q[::-1]:
            time += i*val
            val = 60
        return time


    def edit(self,start_time,end_time) :
        #os.chdir(r"C:\Users\user\Downloads")
        latest_file  = max(os.listdir('.'),key = os.path.getctime)
        ffmpeg_extract_subclip(latest_file, start_time,end_time, targetname="C:/Users/user/Desktop/music/"+latest_file)

        

download().web_scrape()
