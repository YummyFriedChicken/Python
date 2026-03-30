# /usr/bin/python  
# coding:UTF-8  
  
#客户端程序  
import socket  
from socket import *  
  
client = socket(AF_INET,SOCK_STREAM)  
client.connect(("0.0.0.0",8080))  
  
  
def main():  
    while True:  
        msg = input(">>:").strip()  
        if not msg:continue  
        client.send(msg.encode("utf-8"))  
        msg = client.recv(1024)  
        print(msg.decode("utf-8"))  
  
  
if __name__ == '__main__':  
    main()