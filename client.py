from email import message
import socket
from dhooks import Webhook


webhook_info = Webhook("https://discord.com/api/webhooks/1014892779794612224/4xOHq2QjPQst9rBao-wZ6rkDgSyMAg-0LPCOUbqofZwxjNzPPGrfSSKU4wuB4E7LCbS5")

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host, port = "127.0.0.1", 4000
client_socket.connect((host, port))

name = input("Enter an username: ")

if __name__ == "__main__":

    while True:
        message = input("message: ")
        client_socket.send(f"{name}: {message}".encode("utf-8"))
        webhook_info.send(f"{name}: {message}")