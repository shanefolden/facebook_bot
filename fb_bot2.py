from selenium import webdriver
from lxml import html
from lxml import etree
from lxml.etree import tostring
from twilio.rest import Client
import re
import time
from pynput.keyboard import Key, Controller
keyboard = Controller()
browser = webdriver.Chrome() #replace with .Firefox(), or with the browser of your choice
url = "https://www.facebook.com/groups/277641089244406/"
browser.get(url) #navigate to the page
time.sleep(2)
keyboard.type('shanesbot@gmail.com')
keyboard.press(Key.tab)
keyboard.release(Key.tab)
keyboard.type($password)
keyboard.press(Key.enter)
keyboard.release(Key.enter)
account_sid = your_account_sid
auth_token = your_auth_token
# time.sleep(15)
# keyboard.press(Key.tab)
# keyboard.release(Key.tab)
# keyboard.press(Key.space)
# keyboard.release(Key.space)
def sendMessage(text):
    client = Client(account_sid, auth_token)

    message = client.messages \
                    .create(
                         body=text,
                         from_='+12012524466',
                         to=your_number_here
                 )
    print(message.sid)


def do_everything(old_message):
    newPost = False
    innerHTML = browser.execute_script("return document.body.innerHTML") #returns the inner HTML as a string
    htmlElem = html.document_fromstring(innerHTML)
    root = htmlElem

    articles = (root.xpath("//div[@role='article']"))
    sicko = (root.xpath("//a[@rel='dialog']"))
    themcontent = (root.xpath("//div[@data-testid='post_message']"))
    body = themcontent[0].text_content()
    gotAuthor = False

    while not gotAuthor:
        try:
            author = sicko[17].text_content()
            gotAuthor = True;
        except IndexError as e:
            print("got indexError, trying again in 5 seconds")
            time.sleep(5)
    print("author ="+author)

    text = "\nAuthor: "+author+"\n"+body

    if body != old_message:
        sendMessage(text)
    time.sleep(60)
    reload()
    return body


def reload():
    keyboard.press(Key.cmd)
    keyboard.press('r')
    keyboard.release(Key.cmd)
    keyboard.release('r')
    print("yeetus")

str1 = ""
while True:
    str1 = do_everything(str1)
