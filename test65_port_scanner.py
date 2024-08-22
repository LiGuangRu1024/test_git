# @time     ：2024/8/19 14:51
# @author   : 莉光哈哈哈
# @file     : test65_port_scanner.py
# @software : PyCharm
'''
端口扫描器-----了解网络设备开放的服务端口，用于网络安全评估和渗透测试
'''
import socket
import sys


# 定义扫描函数
def scan_port(host, port):
    try:
        # 创建一个socket对象
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # 设置超时时间
        sock.settimeout(1)

        # 尝试连接到主机的端口
        result = sock.connect_ex((host, port))

        if result == 0:
            print(f"Port {port}:OPEN")
        else:
            print(f"Port {port}:CLOSED")

        sock.close()
    except socket.error:
        print(f"Failed to connect to {host} on port {port}")
        sys.exit()


def main():
    if len(sys.argv) != 3:
        print("Usage: python portscanner.py<host><start_port>-<end_port>")
        sys.exit()

    host = sys.argv[1]
    port_range = sys.argv[2].split('-')
    start_port = int(port_range[0])
    end_port = int(port_range[1])

    for port in range(start_port, end_port + 1):
        scan_port(host, port)


if __name__ == '__main__':
    main()


'''
使用方法---在命令行中运行端口扫描器。例如扫描 example.com 的 1 到 100 号端口：python portscanner.py example.com 1-100
'''