# encoding: utf-8
import sys
import commands
import time
from mcstatus import MinecraftServer
import SndMsg

def get_session():
    #状態取得
    server = MinecraftServer.lookup("192.168.3.4:25565")
    query = server.query()
    list_def = query.players.names

    time.sleep(5)

    query = server.query()
    status = server.status()
    list_much = query.players.names

    #マッチング
    set_join = set(list_much) - set(list_def)
    list_join = list(set_join)

    set_left = set(list_def) - set(list_much)
    list_left = list(set_left)

    list_def = list_much

    #ログインアウトされたか判断
    if len(list_join) == 0: #ログイン通知処理
        pass
    else:
        join_name = "{0}".format(", ".join(list_join))
        player_online = "{0}".format(status.players.online)

        if player_online == 0:
            online_player = u"#現在オンラインのニート無し"
        else:
            online_player = u"#現在" + player_online + u"ニートがオンライン"

        joinmsg = u"【Minecraft】\n" + join_name + u"さんがログインしました \n" + online_player

        SndMsg.snd_s(joinmsg)

    if len(list_left) == 0: #ログアウト通知処理
        pass
    else:
        left_name = "{0}".format(", ".join(list_left))
        player_online = "{0}".format(status.players.online)

        if player_online == 0:
            online_player = u"#現在オンラインのニート無し"
        else:
            online_player = u"#現在" + player_online + u"ニートがオンライン"

        leftmsg = u"【Minecraft】\n" + left_name + u"さんがログアウトしました \n" + online_player

        SndMsg.snd_s(leftmsg)
