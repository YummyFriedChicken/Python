# 客户端程序  
import socket


def main():
    tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    dest_ip = input("从哪个服务器下载:")
    dest_port = int(input("请输入下载的port:"))
    tcp_socket.connect((dest_ip, dest_port))

    down_file_name = input("请输入要下载的文件名:")
    # 把文件名发给服务器  
    tcp_socket.send(down_file_name.encode("utf-8"))
    # 接收下载文件，1M  
    recv_data = tcp_socket.recv(1024 * 1024)
    # 保存数据文件  
    with open("new_" + down_file_name, "wb") as f:
        f.write(recv_data)
    tcp_socket.close()

if __name__ == '__main__':
    main()