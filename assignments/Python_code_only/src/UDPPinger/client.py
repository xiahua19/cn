import socket
from datetime import datetime

class MyClient:
    def __init__(self, server_ip, server_port):
        self.server_ip = server_ip
        self.server_port = server_port

    def start(self):
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        client_socket.settimeout(2)
        try:
            for i in range(10):
                message = "Ping " + str(i) + " " + str(datetime.now())
                client_socket.sendto(message.encode('utf-8'), (self.server_ip, self.server_port))

                response = client_socket.recv(1024).decode('utf-8')
                print("服务器回复:", response)

                if message == "exit":
                    break

        except socket.timeout:
            print("响应超时")

        finally:
            client_socket.close()

if __name__ == '__main__':
    server_ip = '127.0.0.1'  # 服务器IP地址
    server_port = 5678      # 服务器端口号

    client = MyClient(server_ip, server_port)
    client.start()
