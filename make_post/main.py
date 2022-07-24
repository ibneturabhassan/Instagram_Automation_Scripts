import os
import random
import time
import re


import pyautogui
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def get_image():
    images = os.listdir('images') #list all the images
    return random.choice(images)

def remove_image(file_name):
    os.remove('images/'+file_name) #remove image

def get_caption():
    captions_file = open('data/captions.txt', 'r', encoding='UTF-8')
    captions = captions_file.read()
    captions = captions.split('-----')

    return random.choice(captions).strip()

def get_hashtags():
    hashtags_file = open('data/hashtags.txt', 'r')
    hashtags = hashtags_file.read()
    hashtags = hashtags.split(' ')
    hashtags = list(set(random.choices(hashtags, k=5)))
    hashtags_to_return = ''
    for hashtag in hashtags:
        hashtags_to_return = hashtags_to_return+hashtag+'\n'
    return hashtags_to_return

def deEmojify(text):
    regrex_pattern = re.compile(pattern = "["
        u"\U0001F600-\U0001F64F"  # emoticons
        u"\U0001F300-\U0001F5FF"  # symbols & pictographs
        u"\U0001F680-\U0001F6FF"  # transport & map symbols
        u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                           "]+", flags = re.UNICODE)
    return regrex_pattern.sub(r'',text)

def make_post(self):
    JS_ADD_TEXT_TO_INPUT = """
      var elm = arguments[0], txt = arguments[1];
      elm.value += txt;
      navigator.clipboard.writeText(elm.value);
      """
    self.get("https://www.instagram.com/")
    #self.driver.set_window_size(1552, 832)
    WebDriverWait(self, 4).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div[1]/div/div[1]/div/div/div/div[1]/div[1]/section/nav/div[2]/div/div/div[3]/div/div[3]/div/button/div"))).click()
    WebDriverWait(self, 4).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div[1]/div/div[2]/div/div/div[1]/div/div[3]/div/div/div/div/div/div/div/div/div[2]/div[1]/div/div/div[2]/div/button"))).click()
    #adding image
    time.sleep(1)
    image = get_image()
    pyautogui.write(os.getcwd()+'\\images\\'+image)
    time.sleep(3)
    pyautogui.press('enter')
    #next buttons
    WebDriverWait(self, 40).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/div[1]/div/div[2]/div/div/div[1]/div/div[3]/div/div/div/div/div/div/div/div/div[1]/div/div/div[3]/div/button'))).click()
    WebDriverWait(self, 40).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/div[1]/div/div[2]/div/div/div[1]/div/div[3]/div/div/div/div/div/div/div/div/div[1]/div/div/div[3]/div/button'))).click()
    #captions
    elem = WebDriverWait(self, 40).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div[1]/div/div[2]/div/div/div[1]/div/div[3]/div/div/div/div/div/div/div/div/div[2]/div[2]/div/div/div/div[2]/div[1]/textarea")))
    #wd.execute_script(JS_ADD_TEXT_TO_INPUT, elem, get_caption()+'\n'+get_hashtags())
    elem.send_keys(deEmojify(get_caption()+'\n'+get_hashtags()))
    #time.sleep(5)
    #time.sleep(5)
    WebDriverWait(self, 40).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div[1]/div/div[2]/div/div/div[1]/div/div[3]/div/div/div/div/div/div/div/div/div[1]/div/div/div[3]/div/button"))).click()
    flag = WebDriverWait(self, 40).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div[1]/div/div[2]/div/div/div[1]/div/div[3]/div/div/div/div/div/div/div/div/div[1]/div/div/div[1]/h1/div"))).text

    while(flag != 'Post shared'):
        flag = WebDriverWait(self, 40).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div[1]/div/div[2]/div/div/div[1]/div/div[3]/div/div/div/div/div/div/div/div/div[1]/div/div/div[1]/h1/div"))).text
        #print(flag)
    # time.sleep(15)
    remove_image(image)
    return 1

chrome_profiles_file = open('data/chrome_profiles.txt', 'r')
chrome_profile = chrome_profiles_file.readlines()
username=chrome_profile[0].split('\\')[2]
profile_name=chrome_profile[0].split('\\')[-1]
options = webdriver.ChromeOptions()
options.add_argument('--user-data-dir=C:\\Users\\' + username + '\\AppData\\Local\\Google\\Chrome\\User Data\\')
options.add_argument('--profile-directory=' + profile_name)
wd = webdriver.Chrome(options=options)
# wd.get('https://www.instagram.com/')
# #
for i in range(0, 5):
    make_post(wd)
    print(str('Post# ')+str(i)+str('  --- done!'))

wd.close()