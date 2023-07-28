import socket
import random
import threading

class MyServer:
    def __init__(self, host, port):
        self.host = host
        self.port = port

    def start(self):
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

        try:
            server_socket.bind((self.host, self.port))
            print("服务器启动，等待客户端连接...")

            while True:  
                # Generate random number in the range of 0 to 10
                rand = random.randint(0, 10)
                # Receive the client packet along with the address it is coming from
                message, address = server_socket.recvfrom(1024)
                # Capitalize the message from the client
                message = message.upper()
                # If rand is less than 4, we consider the packet lost and don't respond
                if rand < 4:
                    continue
                # Otherwise, the server responds
                server_socket.sendto(message, address)

        except Exception as e:
            print("发生异常:", e)

        finally:
            server_socket.close()


if __name__ == '__main__':
    host = '127.0.0.1'  # 服务器IP地址
    port = 5678        # 服务器端口号

    server = MyServer(host, port)
    server.start()
