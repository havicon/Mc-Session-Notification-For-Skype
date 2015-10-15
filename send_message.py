# -*- coding: utf-8 -*-
import Skype4Py

class sndmsg:
    def snd_s(msg): #skype送信

        skype = Skype4Py.Skype(Transport='x11')
        skype.Attach()

        for chat in skype.Chats :
            if chat.Name == '#harikaeshouta/$a71d731fc48d0544': # グループID
                chat.SendMessage(msg)

    def snd_t(msg):
        
