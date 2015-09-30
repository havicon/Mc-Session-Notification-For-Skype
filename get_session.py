# encoding: utf-8
import sys
import commands
import time
from mcstatus import MinecraftServer

while True:
    #状態取得
    server = MinecraftServer.lookup("10.240.222.48:2525")
    query = server.query()
    list_def = query.players.names

    time.sleep(30)

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
    if len(list_join) == 0:
        pass
    else:
        join_name = "{0}".format(", ".join(list_join))
        player_online = "{0}".format(status.players.online)

        join_msg = commands.getoutput("python send_message.py " + join_name + " " + player_online + " 1")
	print(join_msg)

    if len(list_left) == 0:
        pass
    else:
        left_name = "{0}".format(", ".join(list_left))
        player_online = "{0}".format(status.players.online)

        left_msg = commands.getoutput("python send_message.py " + left_name + " " + player_online + " 2")
        print(left_msg)
