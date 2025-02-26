from selenium.webdriver.common.keys import Keys
import undetected_chromedriver as uc
import time

driver = uc.Chrome()

chrome_path = "C:\Program Files\Google\Chrome\Application\chrome.exe"

def openSnapchat():
    driver.switch_to.window(driver.window_handles[0])

def openTikTok():
    driver.switch_to.window(driver.window_handles[1])

def sendTikTok():
    openTikTok()
    thisTikTok = driver.current_url
    openSnapchat()
    time.sleep(0.25)
    chatBox = driver.find_element("xpath", '//*[@placeholder="Send a chat"]')
    chatBox.send_keys(thisTikTok)
    chatBox.send_keys(Keys.ENTER)
    time.sleep(0.25)

def nextTiktok():
    openTikTok()
    driver.find_element("xpath", "//html").send_keys(Keys.DOWN)
    time.sleep(1)

driver.get("https://web.snapchat.com/")
input("Please log into Snapchat and press enter")
chatURL = input("Please enter the URL of the chat to send TikToks to: ")
driver.get(chatURL)

driver.execute_script("window.open('https://www.tiktok.com/', '_blank')")
input("Please open tiktok and enter")
openTikTok()
input("Please log into TikTok and press enter")

while True:
    sendTikTok()
    nextTiktok()