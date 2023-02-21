from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
import time

import os
########################    Functions     ########################
def send_message(msg):
    try:
        text_element_xpath = '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]/p'
        text_element = browser.find_element(By.XPATH, text_element_xpath)
        browser.execute_script(
            f'''
        const text = `{msg}`;
        const dataTransfer = new DataTransfer();
        dataTransfer.setData('text', text);
        const event = new ClipboardEvent('paste', {{
        clipboardData: dataTransfer,
        bubbles: true
        }});
        arguments[0].dispatchEvent(event)
        ''',
            text_element)

        text_element.send_keys
        # if 1030>len(msg)>500:
        #     time.sleep(1.5) 
        # elif len(msg)>1030:
        time.sleep(1) 
        # sendable_text=browser.find_element(By.XPATH,'//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div/p/span')
        # if 'Type a message' != sendable_text.text 
            # (Keys.ENTER)   
            # time.sleep(3)
            # text_element.send_Keys(Keys.ENTER)
        browser.find_element(By.XPATH,'//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[2]/button/span').click()
        

    except Exception as bug:
        print(f'Send_message failed!\n{bug}')
#####################################   Main Body  ########################################
capa = DesiredCapabilities.CHROME
capa["pageLoadStrategy"] = "none"
browser = None
chrome_options = Options()
# chrome_options.add_argument("--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36")
# chrome_options.add_argument("--headless") # creating a hidden browser
# chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument('--profile-directory=Default')
chrome_options.add_argument('--user-data-dir=C:/Temp/ChromeProfile')

if not browser:
            print('runing......................')
            browser = webdriver.Chrome(
                ChromeDriverManager().install(),
                options=chrome_options,
                desired_capabilities=capa
            )
browser = browser
browser.maximize_window()
browser.get('https://web.whatsapp.com/')
wait = WebDriverWait(browser, 600)
# clicking on mine
wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="side"]/div[1]/div/div/div[2]/div/div[2]')))
time.sleep(15)

while 1:
    try:
        all_chats = browser.find_elements(by=By.CLASS_NAME, value='lhggkp7q')
        for chat in all_chats:
            if 'cfzgl7ar' in chat.get_attribute('innerHTML'):
                chat.click()
                time.sleep(2)
                # detail = browser.find_element_by_xpath('//div[@class="_21nHd"]//span').text.split(' ')
                # user=detail[-1]
                try:
                        # getting latest message
                        all_messages_list = browser.find_elements(by=By.CLASS_NAME, value='focusable-list-item')
                        incoming_message = all_messages_list[-1].get_attribute('innerHTML')
                        # Detecting incoming_message type
                        if 'selectable-text copyable-text' in incoming_message:
                            print('Text Detected!')
                            latest_message=all_messages_list[-1].text.split('\n')
                            del latest_message[-1]
                            new_msg=''.join(map(str,latest_message)) # It's variable which have value of new message
                            print('New input message is : ',new_msg)

                            mykeywords = open("Keywords.txt", "r")
                            for line in mykeywords:
                                templist = line.split(", ")
                                for i in range(len(templist)):
                                    tempelement = templist[i]
                                    
                                    if (new_msg.find(tempelement) != -1):
                                        index = templist[-1]

                                    
                            mykeywords.close()
                            print(index) 

                            myresponses = open("Answers.txt", "r")
                            temp = 0 
                            for line in myresponses:
                                if temp == 0:
                                    if index == line:
                                        temp = 1
                                elif temp == 1:
                                    msg = line
                                    break 
                
                            send_message(msg)
                        else:
                            print('New message is not text.')
                            msg='Sorry\n*Please send me text only*'
                            send_message(msg)

                except Exception as bug:
                    print('Got some problem in detection of "latest_message"!')
                    print(bug)
                wait = WebDriverWait(browser, 600)
                browser.find_element(by=By.XPATH,value='//*[@id="main"]/header/div[3]/div/div[2]/div/div/span').click()
                wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/div/span[4]/div/ul/div/div/li[3]/div')))
                close_button = browser.find_element(by=By.XPATH,value='//*[@id="app"]/div/span[4]/div/ul/div/div/li[3]/div')
                close_button.click()
                print('sccesful')
                # send_message()

    except Exception as bug:
        print('there is some   error\n',bug)

''' 
mykeywords = open("Keywords.txt", "r")
Userinput = "RSA"
for line in mykeywords:
    templist = line.split(", ")
    for i in range(len(templist)):
        if templist[i] in Userinput:
            index = templist[-1]

          
mykeywords.close()
print(index) 

myresponses = open("Answers.txt", "r")
temp = 0 
for line in myresponses:
    if temp == 0:
        if index == line:
            temp = 1
    elif temp == 1:
        answer = line
        break 
print(answer)
'''
