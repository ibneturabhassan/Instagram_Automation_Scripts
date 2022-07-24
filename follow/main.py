import json
import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def follow_req(handle, self):
    self.get("https://www.instagram.com/"+handle)
    #text = driver.FindElement(By.TagName("title")).GetAttribute("textContent");
    if(self.title == 'Page not found • Instagram'):
        print('Page not found ' + str(handle))
        return 0
    time.sleep(3)
    #self.find_element_by_xpath("//button[text()='Follow']").click()
    try:
        self.find_element_by_xpath("//button[contains(., 'Follow')]").click()
        print('Followed: ' + str(handle))
        time.sleep(2)
        return 1
    except:
        print('Already Followed: ' + str(handle))
        return 0


    # try:
    #     print('error here')
    #     if (WebDriverWait(self, 5).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/div[1]/div/div[1]/div/div/div[1]/div[1]/section/main/div/header/section/div[1]/div[1]/div/div[2]/div/span/span[1]/button'))).text == 'Follow'):
    #         WebDriverWait(self, 5).until(EC.element_to_be_clickable((By.XPATH,
    #                                                                  '/html/body/div[1]/div/div[1]/div/div[1]/div/div/div[1]/div[1]/section/main/div/header/section/div[1]/div[1]/div/div[2]/div/span/span[1]/button'))).click()
    #         print('Followed: ' + str(handle))
    #         return 1
    #     else:
    #         raise Exception()
    # except:
    #     try:
    #         if (WebDriverWait(self, 3).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/div[1]/div/div[1]/div/div/div[1]/div[1]/section/main/div/header/section/div[1]/div[1]/div/div/button'))).text == 'Follow'):
    #             WebDriverWait(self, 3).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/div[1]/div/div[1]/div/div/div[1]/div[1]/section/main/div/header/section/div[1]/div[1]/div/div/button'))).click()
    #             print('Followed: ' + str(handle))
    #             return 1
    #         else:
    #             raise Exception()
    #     except:
    #         print('Already Followed: ' + str(handle))
    #         return 0
    #time.sleep(5)

COUNTER = 1
FOLLOW_REQ = 25
chrome_profiles_file = open('data/chrome_profiles.txt', 'r')
chrome_profile = chrome_profiles_file.readlines()
username=chrome_profile[0].split('\\')[2]
profile_name=chrome_profile[0].split('\\')[-1]
options = webdriver.ChromeOptions()
options.add_argument('--user-data-dir=C:\\Users\\' + username + '\\AppData\\Local\\Google\\Chrome\\User Data\\')
options.add_argument('--profile-directory=' + profile_name)
wd = webdriver.Chrome(options=options)


handles_file = open('data/list.txt', 'r')
handles = handles_file.readlines()
rems = handles.copy()

for handle in handles:
    if(follow_req(handle.strip('\n'), wd) == 1):
        COUNTER = COUNTER + 1
    rems.pop(0)
    if(COUNTER>=FOLLOW_REQ+1):
        break
handles_file.close()

with open('data/list.txt', 'w') as fp:
    for rem in rems:
        fp.write(rem)
fp.close()
wd.close()
print('Req sent:', COUNTER-1)