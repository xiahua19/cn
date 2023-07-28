import socket
import threading

class MyServer:
    def __init__(self, host, port):
        self.host = host
        self.port = port

    def start(self):
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        try:
            server_socket.bind((self.host, self.port))
            server_socket.listen(5)
            print("服务器启动，等待客户端连接...")

            while True:
                # 等待客户端连接
                client_socket, address = server_socket.accept()
                print(f"建立来自 {address[0]}:{address[1]} 的新连接")

                # 创建新线程处理当前连接
                thread = threading.Thread(target=self.handle_message, args=(client_socket, address))
                thread.start()

        except Exception as e:
            print("发生异常:", e)

        finally:
            server_socket.close()
    
    def handle_message(self, client_socket, address):
        while True:
            message = client_socket.recv(1024).decode('utf-8')
            print("收到消息:", message)

            if message == "exit":
                break

            response = input("请输入回复消息:")
            client_socket.send(response.encode('utf-8'))

        client_socket.close()


if __name__ == '__main__':
    host = '127.0.0.1'  # 服务器IP地址
    port = 12345        # 服务器端口号

    server = MyServer(host, port)
    server.start()
