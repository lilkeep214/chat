from distutils.log import info
import socket
import select
import pyfiglet
import time
from datetime import datetime
from dhooks import Webhook

webhook_info = Webhook("https://discord.com/api/webhooks/1014892779794612224/4xOHq2QjPQst9rBao-wZ6rkDgSyMAg-0LPCOUbqofZwxjNzPPGrfSSKU4wuB4E7LCbS5")

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host, port = "127.0.0.1", 4000
server.bind((host, port))
server.listen(4)

client_connected=True
socket_objs = [server]

server_title = pyfiglet.figlet_format("Welcome")
print(server_title)

while client_connected:
    readed_list, accessible_listWrited, exception = select.select(socket_objs, [], socket_objs)

    for socket_obj in readed_list:

        if socket_obj is server:
            client, adress = server.accept()
            socket_objs.append(client)
        
        else:

            sended_inforamtions = socket_obj.recv(128).decode("utf-8")

            if sended_inforamtions:
                print(sended_inforamtions)
            
            else:
                socket_objs.remove(socket_obj)
                print("someonse is disconnected.")
                print(f"{len(socket_objs) - 1} persons are connected.")
                
                with open("logs.txt", "a") as file:
                    file.write(str(datetime.now()) + f": One user leaved the chat, {len(socket_objs) - 1} person.s remaining.\n")

                    webhook_info.send(str(datetime.now()) + f": One user leaved the chat, {len(socket_objs) - 1} person.s remaining.\n")
        
