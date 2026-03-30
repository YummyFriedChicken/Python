  
from optparse import OptionParser  
import socket, sys  
  
# ip和端口是否开放  
def ip_port_opened(ip, port):  
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  
    try:  
        s.connect((ip, port))  
        return True  
    except:  
        return False  
  
 # 扫描  
def scan(ip, portlist):  
    for port in portlist:  
        if ip_port_opened(ip, port):  
            print("%s host %s port opened" % (ip, port))  
        else:  
            print("%s host %s port closed" % (ip, port))  
# 广泛扫描  
def rescan(ip, start, end):  
    for port in range(start, end + 1):  
        if ip_port_opened(ip, port):  
            print("%s host %s port opened" % (ip, port))  
        else:  
            print("%s host %s port closed" % (ip, port))  
  
def main():  
    usage = "usage:xxx.py -i ip地址 -p 端口"  
    # 初始化命令行参数解析器  
    parse = OptionParser(usage=usage)  
    parse.add_option("-i","--ip",type="string",dest="ipaddress",help="your target ip here")  
    parse.add_option("-p","--port",type="string",dest='port',help="your target port here")  
    #凡是以上parse.add_option定义过的，后面参数自动放进options，其余放进args  
    (options,args) = parse.parse_args()  
  
    ip = options.ipaddress  
    port = options.port  
  
    default = [21,22,23,25,53,80,110,443,1433,1521,3306,3389]  
  
    if ',' in port:     #xxx.py -i 127.0.0.1 -p 80,21,89  
        p = port.split(',')  
        portlist = []  
        for x in p:  
            portlist.append(int(x))  
        scan(ip,portlist)  
    elif '-' in port:   #xxx.py -i 127.0.0.1 -p 80-89  
        p = port.split('-')  
        StartPort = int(p[0])  
        EndPort = int(p[1])  
        rescan(ip,StartPort,EndPort)  
    elif 'all' in port:   #xxx.py -i 127.0.0.1 -p all  
        rescan(ip,1,65535)  
    elif 'default' in port: #xxx.py -i 127.0.0.1 -p default  
        scan(ip,default)  
  
if __name__ == '__main__':  
    main()