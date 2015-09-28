# encoding: utf-8

import Skype4Py
import time

def handler(msg, event):
    if event == u"RECEIVED":
        if msg.Body == u"ボット":
            msg.Chat.SendMessage(u"|ΦωΦ) ...")

def main():
    skype = Skype4Py.Skype(Transport='x11')
    skype.OnMessageStatus = handler
    skype.Attach()
    while True:
        time.sleep(1) 

if __name__ == "__main__":
    main()
