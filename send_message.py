# -*- coding: utf-8 -*-
import Skype4Py
import sys

argvs = sys.argv
acnt = len(argvs)

if argvs[3] == 1:
    skype = Skype4Py.Skype(Transport='x11')
    skype.Attach()

    msg = msg = u"【Minecraft】\n" + argvs[1] + u"さんがログインしました \n" + u"#現在" + argvs[2] + u"ニートがオンライン"

    for chat in skype.Chats :
        if chat.Name == '#seasuta/$68c3bfe6bcf2c649': # 要書き換え
            chat.SendMessage(msg)

elif argvs[3] == 2:
    argvs = sys.argv
    acnt = len(argvs)

    skype = Skype4Py.Skype(Transport='x11')
    skype.Attach()

    msg = msg = u"【Minecraft】\n" + argvs[1] + u"さんがログアウトしました \n" + u"#現在" + argvs[2] + u"ニートがオンライン"

    for chat in skype.Chats :
        if chat.Name == '#seasuta/$68c3bfe6bcf2c649': # 要書き換え
            chat.SendMessage(msg)
