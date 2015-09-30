# encoding: utf-8

import Skype4Py
import sys
import commands
import time
import re

# variable
cheaklist = 0
flagrestert = 0

# Locate

def handler(msg, event):

    if event == u"RECEIVED":
        global flagrestert

        if flagrestert == 1:
            if msg.Body == u"Y":
                commands.getoutput("reboot")
                msg.Chat.SendMessage(u"【Minecraft】\n" + u"サーバーの強制再起動コマンドを送信しました")
                flagrestert = 0
            elif msg.Body == u"n":
                msg.Chat.SendMessage(u"【Minecraft】\n" + u"キャンセルしました")
                flagrestert = 0

        elif msg.Body == u"server-restart":
            commands.getoutput("/etc/init.d/minecraft restart")
            msg.Chat.SendMessage(u"サーバー再起動コマンドを送信しました")

        elif msg.Body == u"応答せよ":
            msg.Chat.SendMessage(u"呼んだか？")
        
        elif msg.Body == u"好きです":
            msg.Chat.SendMessage(u"ごめんなさい")

        elif msg.Body == u"うるせーよハゲ":
            msg.Chat.SendMessage(u"通知を一時停止するよ")

        elif msg.Body == u"server-list":
            cheaklist = commands.getoutput("/etc/init.d/minecraft command list")
            playercow = cheaklist[96]
            plmsg = u"【Minecraft】\n" + u"現在 " + playercow + u" ニートがオンラインです"
            msg.Chat.SendMessage(plmsg)

        elif msg.Body == u"server-status":
            checksv = commands.getoutput("/etc/init.d/minecraft status")
            msg.Chat.SendMessage(u"【Minecraft】\n" + checksv)

        elif msg.Body == u"server-ping":
            checksv = commands.getoutput("/etc/init.d/minecraft command ping")
            if checksv[53] == '[':
                msg.Chat.SendMessage(u"【Minecraft】\n" + u"応答を確認しました")
            else:
                msg.Chat.SendMessage(u"【Minecraft】\n" + u"サーバーが応答しませんでした。")

        elif msg.Body == u"server-save":
            commands.getoutput("/etc/init.d/minecraft command save-all")
            msg.Chat.SendMessage(u"【Minecraft】\n" + u"ワールドセーブコマンドを送信しました")

        elif msg.Body == u"server-tps":
            checktps = commands.getoutput("/etc/init.d/minecraft command tps")
            msg.Chat.SendMessage(u"【Minecraft】\n" + checktps)

        elif msg.Body == u"server-restart -f":
            msg.Chat.SendMessage(u"【Minecraft】\n" + u"プロセスを強制終了するため、ワールド破損やロールバックが発生する可能性があります。宜しいですか :Y/n")
            flagrestert = 1

        elif msg.Body == u"help":
            helpmsg = u"""
            【Minecraft】コマンドヘルプ
            help            : ヘルプの表示
            server-restart  : サーバー再起動
            [-f 強制]
            server-ping     : サーバー応答確認
            server-list     : 参加人数確認
            server-save     : ワールドセーブ
            server-tps      : サーバーTPS取得
            応答せよ         : Bot生存確認
            """
            msg.Chat.SendMessage(helpmsg)
            

def main():
    skype = Skype4Py.Skype(Transport='x11')
    skype.OnMessageStatus = handler
    skype.Attach()
    while True:
        time.sleep(1)

if __name__ == "__main__":
    main()
